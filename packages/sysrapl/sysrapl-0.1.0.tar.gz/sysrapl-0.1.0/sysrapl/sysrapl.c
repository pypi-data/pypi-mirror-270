/* sysrapl.c
 *
 * Copyright 2023 Ondřej Míchal
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include <bpf/bpf.h>
#include <bpf/libbpf.h>
#include <err.h>
#include <fcntl.h>
#include <linux/perf_event.h>
#include <signal.h>
#include <stdarg.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/syscall.h>
#include <sys/sysinfo.h>
#include <sys/wait.h>
#include <time.h>
#include <unistd.h>

#include "sysrapl.h"
#include "sysrapl.skel.h"

struct sysrapl_perf_event_domain {
  char *name;
  char *path;
  char *events[RAPL_EVENT_COUNT];
};

static struct sysrapl_perf_event_domain rapl_domain = {
    "power",
    "/sys/devices/power",
    {
        "energy-cores",
        "energy-pkg",
        "energy-ram",
        "energy-gpu",
        "energy-psys",
    },
};

static bool poll = true;

static void handle_sigint(int signo, siginfo_t *info, void *ctx) {
  poll = false;
}

static int handle_ring_buffer(void *ctx, void *data, size_t data_sz) {
  sysrapl_data_t *sysrapl_data = (sysrapl_data_t *)data;
  int *output_fd = (int *)ctx;

  if (sysrapl_data->err != 0) {
    char buf[BUFSIZ];

    libbpf_strerror(sysrapl_data->err, buf, BUFSIZ);
    warnx("There was an error %d: %s", sysrapl_data->err, buf);

    return 1;
  }

  if (sysrapl_data->type == SYSRAPL_EVENT_SYS) {
    dprintf(*output_fd, "%d %d %d %ld %llu %llu\n", sysrapl_data->type,
            sysrapl_data->sys.cpu, sysrapl_data->sys.tid,
            sysrapl_data->sys.syscall_id, sysrapl_data->sys.syscall_start_ns,
            sysrapl_data->sys.syscall_exit_ns);
  }
  
  if (sysrapl_data->type == SYSRAPL_EVENT_RAPL) {
    dprintf(*output_fd, "%d %llu %llu %llu %llu %llu %llu\n",
            sysrapl_data->type, sysrapl_data->rapl.time_ns,
            sysrapl_data->rapl.rapl_cores, sysrapl_data->rapl.rapl_pkg,
            sysrapl_data->rapl.rapl_ram, sysrapl_data->rapl.rapl_gpu,
            sysrapl_data->rapl.rapl_psys);
  }

  return 0;
}

static int get_rapl_perf_event(struct sysrapl_perf_event_domain *event_domain,
                               char *event_name, struct perf_event_attr *attr) {
  FILE *f = NULL;
  char line_buf[BUFSIZ];
  char domain_type_path[BUFSIZ];
  char event_path[BUFSIZ];
  char *event_type_str, *event_config_str;
  int event_type, event_config;

  memset(attr, 0, sizeof(struct perf_event_attr));

  if (snprintf(domain_type_path, BUFSIZ, "%s/type", event_domain->path) < 0)
    return -1;

  if (snprintf(event_path, BUFSIZ, "%s/events/%s", event_domain->path,
               event_name) < 0)
    return -1;

  f = fopen(domain_type_path, "r");
  if (f == NULL)
    return -1;

  if (fgets(line_buf, BUFSIZ, f) == NULL)
    return -1;

  fclose(f);

  event_type_str = strtok(line_buf, "\n");
  event_type = strtol(event_type_str, NULL, 10);

  f = fopen(event_path, "r");
  if (f == NULL)
    return -1;

  memset(line_buf, 0, BUFSIZ);
  if (fgets(line_buf, BUFSIZ, f) == NULL)
    return -1;

  fclose(f);

  strtok(line_buf, "=");
  event_config_str = strtok(NULL, "\n");
  event_config = strtol(event_config_str, NULL, 16);

  attr->size = sizeof(struct perf_event_attr);
  attr->type = event_type;
  attr->config = event_config;
  attr->read_format = PERF_FORMAT_GROUP;
  attr->disabled = 1;

  return 0;
}

static int attach_perf_event_sampling(const struct bpf_program *prog,
                                      int frequency, struct bpf_link *link) {
  struct perf_event_attr attr;
  char errbuf[BUFSIZ];
  int fd = 0;

  memset(&attr, 0, sizeof(struct perf_event_attr));

  attr.type = PERF_TYPE_SOFTWARE;
  attr.config = PERF_COUNT_SW_CPU_CLOCK;
  attr.freq = 1;
  attr.sample_period = frequency;

  fd = syscall(SYS_perf_event_open, &attr, -1, 0, -1, 0);
  if (fd < 0) {
    warn("failed to open SW_CPU_CLOCK perf event");
    return -1;
  }

  link = bpf_program__attach_perf_event(prog, fd);
  if (link == NULL) {
    libbpf_strerror(errno, errbuf, BUFSIZ);
    warnx("failed to attach perf event to eBPF program: %s", errbuf);
    return -1;
  }

  return 0;
}

/**
 * @brief sysrapl_profile creates, configures and launches eBPF programs for
 * energy profiling of a process.
 *
 * @param opts structure for configuring the profiling process
 *
 * @return int (0 on success, -1 on error)
 */
int sysrapl_profile(struct sysrapl_profile_opts *opts) {
  struct bpf_link *perf_event_link = NULL;
  struct bpf_map *rapl_event_maps[RAPL_EVENT_COUNT] = {NULL, NULL, NULL, NULL};
  struct ring_buffer *rb = NULL;
  struct sysrapl *skel = NULL;
  bool *switches[RAPL_EVENT_COUNT] = {NULL, NULL, NULL, NULL, NULL};
  int perf_event_fds[RAPL_EVENT_COUNT] = {-1, -1, -1, -1, -1};
  int perf_event_group_fd = -1, output_fd;
  int err, ret;

  // RAPL counters are not specific to different CPU cores.
  const int rapl_cpu = 0;

  // Because this function is a part of a larger profiling process and that the
  // function operates by design indefinitely, a custom SIGINT signal handler
  // needs to be set up.
  struct sigaction act = {0};
  act.sa_sigaction = &handle_sigint;
  act.sa_flags = 0;
  if (sigaction(SIGINT, &act, NULL) == -1) {
    errx(EXIT_FAILURE, "failed to attach SIGINT signal handler");
  }

  // libbpf documentation suggests the use of a strict mode to enforce a "libbpf 1.0" mode.
  libbpf_set_strict_mode(LIBBPF_STRICT_DIRECT_ERRS | LIBBPF_STRICT_CLEAN_PTRS);

  // Prepare the output file for raw profiling output
  output_fd = open(opts->output_file, O_WRONLY | O_APPEND | O_CREAT | O_TRUNC);
  if (output_fd < 0) {
    errx(EXIT_FAILURE, "failed to open output file %s: %s", opts->output_file,
         strerror(errno));
    goto cleanup_sysrapl;
  }

  // Start the bootstrapping of a eBPF program using the 4 loading steps
  // For more info, see https://libbpf.readthedocs.io/en/latest/libbpf_overview.html#bpf-app-lifecycle-and-libbpf-apis.
  skel = sysrapl__open();
  if (!skel) {
    errx(EXIT_FAILURE, "failed to open BPF sysrapl: %s", strerror(errno));
    goto cleanup_sysrapl;
  }

  // Set read-only parameters used to adjust the behaviour of a eBPF program
  skel->rodata->filter_pid = opts->filter_pid;

  // Resize maps to fit the number of CPUs
  bpf_map__set_max_entries(skel->maps.syscall_start, get_nprocs_conf());

  // Assign eBPF maps to the matching RAPL domain
  rapl_event_maps[0] = skel->maps.rapl_cores;
  switches[0] = &skel->rodata->has_rapl_cores;

  rapl_event_maps[1] = skel->maps.rapl_pkg;
  switches[1] = &skel->rodata->has_rapl_pkg;

  rapl_event_maps[2] = skel->maps.rapl_ram;
  switches[2] = &skel->rodata->has_rapl_ram;

  rapl_event_maps[3] = skel->maps.rapl_gpu;
  switches[3] = &skel->rodata->has_rapl_gpu;

  rapl_event_maps[4] = skel->maps.rapl_psys;
  switches[4] = &skel->rodata->has_rapl_psys;

  // Check the presence of the different RAPL domains and perf events for the
  // available ones.
  for (int i = 0; i < RAPL_EVENT_COUNT; i++) {
    struct perf_event_attr attr;
    char *curr_event = NULL;

    curr_event = rapl_domain.events[i];

    fprintf(stderr, "Checking event %s/%s\n", rapl_domain.name, curr_event);

    if (get_rapl_perf_event(&rapl_domain, curr_event, &attr)) {
      warnx("failed to get RAPL perf event %s/%s: %s", rapl_domain.name,
            curr_event, strerror(errno));
      continue;
    }

    perf_event_fds[i] = syscall(SYS_perf_event_open, &attr, -1, rapl_cpu,
                                perf_event_group_fd, 0);
    if (perf_event_fds[i] == -1) {
      warnx("failed to open perf event %s/%s: %s", rapl_domain.name, curr_event,
            strerror(errno));
      continue;
    }

    // Set the counter of the perf event to 0
    ioctl(perf_event_fds[i], PERF_EVENT_IOC_RESET, 0);
    ioctl(perf_event_fds[i], PERF_EVENT_IOC_DISABLE, 0);

    // Since we can group events, let's group.
    if (i == 0)
      perf_event_group_fd = perf_event_fds[i];

    *switches[i] = true;
  }

  // Load the eBPF programs into memory
  err = sysrapl__load(skel);
  if (err) {
    errx(EXIT_FAILURE, "failed to load and verify BPF sysrapl: %s",
         strerror(errno));
    goto cleanup_sysrapl;
  }

  if (!opts->enable_syscalls) {
    bpf_program__set_autoload(skel->progs.sys_enter, false);
    bpf_program__set_autoload(skel->progs.sys_exit, false);
  }

  // Prepare ringbuffer for data exchange between user-space and kernel-space.
  rb = ring_buffer__new(bpf_map__fd(skel->maps.ringbuffer), handle_ring_buffer,
                        &output_fd, NULL);
  if (!rb) {
    errx(EXIT_FAILURE, "failed to create ring buffer");
    goto cleanup_sysrapl;
  }

  // RAPL energy consumption counters are sampled at a set rate. Use the CPU
  // clock perf event and attach the eBPF program to it to launch it
  // periodically.
  if (attach_perf_event_sampling(skel->progs.collect_rapl_info, opts->frequency,
                                 perf_event_link) != 0) {
    errx(EXIT_FAILURE, "failed to attach to perf event");
    goto cleanup_sysrapl;
  }

  // Put the file descriptors of the different RAPL perf events into maps that
  // the eBPF program can use in order to read their value.
  for (int i = 0; i < RAPL_EVENT_COUNT; i++) {
    char errbuf[BUFSIZ];

    if (perf_event_fds[i] == -1)
      continue;

    ret = bpf_map__update_elem(rapl_event_maps[i], &rapl_cpu, sizeof(int),
                               &perf_event_fds[i], sizeof(int), BPF_ANY);
    if (ret < 0) {
      libbpf_strerror(ret, errbuf, BUFSIZ);
      warnx("failed to add perf event fd to eBPF map: %s", errbuf);
      goto cleanup_sysrapl;
    }
  }

  // Delay before the profiling should happen as close to the actuall beginning
  // of the profiling.
  if (opts->delay > 0) {
    struct timespec timeout = {.tv_sec = opts->delay, .tv_nsec = 0};
    nanosleep(&timeout, NULL);
  }

  for (int i = 0; i < RAPL_EVENT_COUNT; i++) {
    if (perf_event_fds[i] == -1)
      continue;

    ioctl(perf_event_fds[i], PERF_EVENT_IOC_ENABLE, 0);
  }

  // Attach the loaded eBPF programs to the different tracepoints/probes/.. to
  // make them active.
  err = sysrapl__attach(skel);
  if (err) {
    errx(EXIT_FAILURE, "failed to attach BPF sysrapl: %s", strerror(errno));
    goto cleanup_sysrapl;
  }

  // Poll data from ring buffer providing data from the eBPF program.
  while (poll) {
    err = ring_buffer__poll(rb, 100);
    // ring_buffer__poll has its own SIGINT handler
    if (err == -EINTR)
      break;

    if (err < 0)
      errx(EXIT_FAILURE, "error while polling ring buffer: %d", err);

    if (waitpid(opts->filter_pid, NULL, WNOHANG) == opts->filter_pid)
      break;
  }

  ring_buffer__free(rb);
cleanup_sysrapl:
  sysrapl__destroy(skel);

  return EXIT_SUCCESS;
}
