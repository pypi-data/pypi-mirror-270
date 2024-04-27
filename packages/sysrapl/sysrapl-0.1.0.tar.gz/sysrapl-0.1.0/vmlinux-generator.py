#!/bin/env python3

import os
import subprocess
import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]}: wrong arguments", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} [OUTPUT]", file=sys.stderr)
    sys.exit(1)

output_file = sys.argv[1]

with open(output_file, mode="w") as f:
    output = subprocess.run(
        ["bpftool", "btf", "dump", "file", "/sys/kernel/btf/vmlinux", "format", "c"],
        check=True,
        stdout=f,
    )

sys.exit(0)
