/* sysrapl.h
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

#include <stdbool.h>

#pragma once

#define RAPL_EVENT_COUNT 5

enum sysrapl_event_type {
  SYSRAPL_EVENT_SYS = 0,
  SYSRAPL_EVENT_RAPL = 1,
};

typedef struct sysrapl_event_t {
  enum sysrapl_event_type type;
  __u32 err;

  union {
    struct {
      long syscall_id;
      __u64 syscall_start_ns;
      __u64 syscall_exit_ns;
      __u32 cpu;
      __u32 tid;
    } sys;

    struct {
      __u64 time_ns;
      __u64 rapl_cores;
      __u64 rapl_pkg;
      __u64 rapl_ram;
      __u64 rapl_gpu;
      __u64 rapl_psys;
    } rapl;
  };
} sysrapl_data_t;

struct sysrapl_profile_opts {
  char *output_file;
  __s64 delay;
  __s64 filter_pid;
  __s64 frequency;
  bool enable_syscalls;
};

int sysrapl_profile(struct sysrapl_profile_opts *opts);
