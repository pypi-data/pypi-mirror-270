# sysrapl

Profiler of energy use of system calls.

> This project is the result of my bachelor's thesis. It was created as a collector for the [Perun](https://github.com/Perfexionists/perun)
> project but is also usable usable standalone.

## Dependencies

- `python` >= 3.6
- `libbpf` >= 1.0
- Linux kernel built with `CONFIG_DEBUG_INFO_BTF=y` option

> clang is required due to lack of support for BPF in GCC.

## Build

### Build dependencies

- `meson` >= 0.56
- `clang/LLVM` >= 10
- `bpftool`

### Build instructions

```shell
# Project installation
$ CC=clang pip install .
$ CC=clang pip install .[dev,report] # Install also optional dependencies

# Documentation build
$ pdoc -d numbpy sysrapl
```

## Links

- Code repository - [https://gitlab.com/martymichal/sysrapl](https://gitlab.com/martymichal/sysrapl)
- Issue tracker - [https://gitlab.com/martymichal/sysrapl/~/issues](https://gitlab.com/martymichal/sysrapl/~/issues)
- Perun - [https://github.com/Perfexionists/perun](https://github.com/Perfexionists/perun)
- Thesis summary - [https://www.vut.cz/en/students/final-thesis/detail/146746](https://www.vut.cz/en/students/final-thesis/detail/146746)

## Citing

When using or referencing this project, consider using the following citation:

```
MÍCHAL, Ondřej. Analysis of software resource consumption. Brno, 2023. Bachelor’s thesis. Brno University of Technology, Faculty of Information Technology. Supervisor Ing. Jiří Pavela
```

## License

This project is licensed under [GNU GPLv3 license](./COPYING).
