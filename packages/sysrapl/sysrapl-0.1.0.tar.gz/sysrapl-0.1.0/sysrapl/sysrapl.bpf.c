/* sysrapl.bpf.c
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

#include "vmlinux.h"

#include <bpf/bpf_core_read.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_tracing.h>

#include "sysrapl.h"

const volatile pid_t filter_pid = 0;
const volatile bool has_rapl_cores = false;
const volatile bool has_rapl_pkg = false;
const volatile bool has_rapl_ram = false;
const volatile bool has_rapl_gpu = false;
const volatile bool has_rapl_psys = false;

struct {
  __uint(type, BPF_MAP_TYPE_PERF_EVENT_ARRAY);
  __uint(max_entries, 1);
  __type(key, int);
  __type(value, int);
} rapl_cores SEC(".maps");

struct {
  __uint(type, BPF_MAP_TYPE_PERF_EVENT_ARRAY);
  __uint(max_entries, 1);
  __type(key, int);
  __type(value, int);
} rapl_pkg SEC(".maps");

struct {
  __uint(type, BPF_MAP_TYPE_PERF_EVENT_ARRAY);
  __uint(max_entries, 1);
  __type(key, int);
  __type(value, int);
} rapl_ram SEC(".maps");

struct {
  __uint(type, BPF_MAP_TYPE_PERF_EVENT_ARRAY);
  __uint(max_entries, 1);
  __type(key, int);
  __type(value, int);
} rapl_gpu SEC(".maps");

struct {
  __uint(type, BPF_MAP_TYPE_PERF_EVENT_ARRAY);
  __uint(max_entries, 1);
  __type(key, int);
  __type(value, int);
} rapl_psys SEC(".maps");

struct {
  __uint(type, BPF_MAP_TYPE_HASH);
  __type(key, tid_t);
  __type(value, u64);
} syscall_start SEC(".maps");

struct {
  __uint(type, BPF_MAP_TYPE_RINGBUF);
  __uint(max_entries, 4096 * sizeof(sysrapl_data_t));
} ringbuffer SEC(".maps");

SEC("tracepoint/raw_syscalls/sys_enter")
int sys_enter(struct trace_event_raw_sys_enter *args) {
  u64 id, syscall_entry_ns;
  pid_t pid;
  tid_t tid;

  syscall_entry_ns = bpf_ktime_get_ns();

  id = bpf_get_current_pid_tgid();
  pid = id >> 32;
  tid = id;

  if (pid != filter_pid)
    return 0;

  bpf_map_update_elem(&syscall_start, &tid, &syscall_entry_ns, 0);

  return 0;
}

SEC("tracepoint/raw_syscalls/sys_exit")
int sys_exit(struct trace_event_raw_sys_exit *args) {
  sysrapl_data_t *data;
  u64 id, *syscall_entry_ns, syscall_exit_ns;
  pid_t pid;
  tid_t tid;

  syscall_exit_ns = bpf_ktime_get_ns();

  id = bpf_get_current_pid_tgid();
  pid = id >> 32;
  tid = id;

  if (pid != filter_pid)
    return 0;

  syscall_entry_ns = bpf_map_lookup_elem(&syscall_start, &tid);
  if (syscall_entry_ns == NULL)
    return 0;

  data = bpf_ringbuf_reserve(&ringbuffer, sizeof(*data), 0);
  if (!data)
    return 1;

  data->type = SYSRAPL_EVENT_SYS;
  data->err = 0;

  data->sys.syscall_id = BPF_CORE_READ(args, id);
  data->sys.syscall_start_ns = *syscall_entry_ns;
  data->sys.syscall_exit_ns = syscall_exit_ns;
  data->sys.cpu = bpf_get_smp_processor_id();
  data->sys.tid = tid;

  bpf_ringbuf_submit(data, 0);

  return 0;
}

SEC("perf_event")
int collect_rapl_info(struct bpf_perf_event_data *ctx) {
  struct bpf_perf_event_value event_buf;
  sysrapl_data_t *data;

  data = bpf_ringbuf_reserve(&ringbuffer, sizeof(*data), 0);
  if (!data)
    return 1;

  data->type = SYSRAPL_EVENT_RAPL;
  data->err = 0;

  data->rapl.time_ns = bpf_ktime_get_ns();
  data->rapl.rapl_cores = 0;
  data->rapl.rapl_pkg = 0;
  data->rapl.rapl_ram = 0;
  data->rapl.rapl_gpu = 0;
  data->rapl.rapl_psys = 0;

  if (has_rapl_cores) {
    data->err =
        bpf_perf_event_read_value(&rapl_cores, BPF_F_CURRENT_CPU, &event_buf,
                                  sizeof(struct bpf_perf_event_value));
    data->rapl.rapl_cores = event_buf.counter;
  }

  if (has_rapl_pkg) {
    data->err =
        bpf_perf_event_read_value(&rapl_pkg, BPF_F_CURRENT_CPU, &event_buf,
                                  sizeof(struct bpf_perf_event_value));
    data->rapl.rapl_pkg = event_buf.counter;
  }

  if (has_rapl_ram) {
    data->err =
        bpf_perf_event_read_value(&rapl_ram, BPF_F_CURRENT_CPU, &event_buf,
                                  sizeof(struct bpf_perf_event_value));
    data->rapl.rapl_ram = event_buf.counter;
  }

  if (has_rapl_gpu) {
    data->err =
        bpf_perf_event_read_value(&rapl_gpu, BPF_F_CURRENT_CPU, &event_buf,
                                  sizeof(struct bpf_perf_event_value));
    data->rapl.rapl_gpu = event_buf.counter;
  }

  if (has_rapl_psys) {
    data->err =
        bpf_perf_event_read_value(&rapl_psys, BPF_F_CURRENT_CPU, &event_buf,
                                  sizeof(struct bpf_perf_event_value));
    data->rapl.rapl_psys = event_buf.counter;
  }

  bpf_ringbuf_submit(data, 0);

  return 0;
}

char LICENSE[] SEC("license") = "GPL";
