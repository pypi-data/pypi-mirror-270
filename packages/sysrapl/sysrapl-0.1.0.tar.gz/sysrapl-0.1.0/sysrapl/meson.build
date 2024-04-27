sysrapl_bpf_sources = files(
  'sysrapl.bpf.c',
)

sysrapl_bpf_object = custom_target('sysrapl-bpf-object',
  command: [
    cc.cmd_array()[0],
    '-g',
    '-O2',
    '-c',
    '-I', meson.project_build_root(),
    '-I', meson.project_build_root() / 'src',
    '-target',
    'bpf',
    '-o',
    '@OUTPUT@',
    '@INPUT@'
  ],
  depends: vmlinux,
  input: sysrapl_bpf_sources,
  output: 'sysrapl.o',
)

sysrapl_bpf_skeleton = custom_target('sysrapl-bpf-skel',
  capture: true,
  command: [
    bpftool,
    'gen',
    'skeleton',
    '@INPUT@'
  ],
  depends: sysrapl_bpf_object,
  input: sysrapl_bpf_object,
  output: 'sysrapl.skel.h',
)

sysrapl_bpf_skeleton_dep = declare_dependency(
  sources: sysrapl_bpf_skeleton
)

sysrapl_sources = files(
  'sysrapl.c',
)

sysrapl_deps = [
  dependency('libbpf', version: '>=1.0'),
]

inc = include_directories('.')

libsysrapl_install_dir = py3.get_install_dir() / 'sysrapl'

libsysrapl = shared_library('sysrapl',
  sysrapl_sources,
  dependencies: [sysrapl_deps, sysrapl_bpf_skeleton_dep],
  include_directories: inc,
  install: true,
  install_dir: libsysrapl_install_dir,
)

sysrapl_py_conf_data = configuration_data({
  'SYSRAPL_LIB_PATH': libsysrapl_install_dir / 'libsysrapl.so',
})

sysrapl_files = files(
  '__init__.py',
  '__main__.py',
  'cli.py',
  'profile.py',
  'report.py',
)

py3.install_sources(
  sysrapl_files,
  subdir: 'sysrapl',
)

