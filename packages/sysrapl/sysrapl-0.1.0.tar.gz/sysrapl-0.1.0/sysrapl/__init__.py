# __init__.py
#
# Copyright 2023 Ondřej Míchal
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

RAPL_DOMAIN_LIST = ["psys", "pkg", "cores", "gpu", "ram"]
# TODO: The values can differ across architectures and CPU generations. Read
# them from powercap sysfs.
RAPL_MAX_VALUE = 262143328850
RAPL_SCALE = (
    # FIXME: This is... just wrong. But it's the easiest as well.
    # The original value on my Skylake CPU is 2.3283064365386962890625e-10. The
    # adjusted value then is the way to scale Joules to nanojoules. To get
    # joules again, multiply by 10^9.
    0.23283064365386962890625
)
