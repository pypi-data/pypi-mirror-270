#!/home/russell/projects/sphinxcontrib-cldomain/dist/export/python/virtualenvs/tools/isort/bin/python3.9 -sE

if __name__ == "__main__":
    import os
    import sys

    venv_dir = os.path.abspath(os.path.dirname(__file__))
    venv_bin_dir = os.path.join(venv_dir, "bin")
    shebang_python = '/home/russell/projects/sphinxcontrib-cldomain/dist/export/python/virtualenvs/tools/isort/bin/python3.9'
    python = os.path.join(venv_bin_dir, os.path.basename(shebang_python))

    def iter_valid_venv_pythons():
        # Allow for both the known valid venv pythons and their fully resolved venv path
        # version in the case their parent directories contain symlinks.
        for python_binary in (python, shebang_python):
            yield python_binary
            yield os.path.join(
                os.path.realpath(os.path.dirname(python_binary)),
                os.path.basename(python_binary)
            )

    def sys_executable_paths():
        exe = sys.executable
        executables = {exe}
        while os.path.islink(exe):
            exe = os.readlink(exe)
            if not os.path.isabs(exe):
                exe = os.path.join(venv_bin_dir, exe)

            if os.path.dirname(exe) == venv_bin_dir and exe not in executables:
                executables.add(exe)
            else:
                # We've either followed relative links inside the bin/ dir out of the bin
                # dir to the original venv seed Python binary or we've walked around a loop
                # of symlinks once; either way, we've found all valid venv python binaries.
                break
        return executables

    current_interpreter_blessed_env_var = "_PEX_SHOULD_EXIT_VENV_REEXEC"
    if (
        not os.environ.pop(current_interpreter_blessed_env_var, None)
        and sys_executable_paths().isdisjoint(iter_valid_venv_pythons())
    ):
        sys.stderr.write("Re-execing from {}\n".format(sys.executable))
        os.environ[current_interpreter_blessed_env_var] = "1"
        os.execv(python, [python, "-sE"] + sys.argv)

    pex_file = os.environ.get("PEX", None)
    if pex_file:
        pex_file_path = os.path.realpath(pex_file)
        sys.argv[0] = pex_file_path
        os.environ["PEX"] = pex_file_path
        try:
            from setproctitle import setproctitle

            setproctitle("{python} {pex_file} {args}".format(
                python=sys.executable, pex_file=pex_file, args=" ".join(sys.argv[1:]))
            )
        except ImportError:
            pass

    ignored_pex_env_vars = [
        "{}={}".format(name, value)
        for name, value in os.environ.items()
        if name.startswith(("PEX_", "_PEX_", "__PEX_")) and name not in (
            # These are used inside this script / the PEX_EXTRA_SYS_PATH.pth site-packages
            # file.
            "_PEX_SHOULD_EXIT_VENV_REEXEC",
            "PEX_EXTRA_SYS_PATH",
            "PEX_VENV_BIN_PATH",
            "PEX_INTERPRETER",
            "PEX_SCRIPT",
            "PEX_MODULE",
            # This is used when loading ENV (Variables()):
            "PEX_IGNORE_RCFILES",
            # And ENV is used to access these during PEX bootstrap when delegating here via
            # a --venv mode PEX file.
            "PEX_ROOT",
            "PEX_VENV",
            "PEX_PATH",
            "PEX_PYTHON",
            "PEX_PYTHON_PATH",
            "PEX_VERBOSE",
            "PEX_EMIT_WARNINGS",
            # This is used by the vendoring system.
            "__PEX_UNVENDORED__",
            # These are _not_ used at runtime, but are present under CI and simplest to add
            # an exception for here and not warn about in CI runs.
            "_PEX_TEST_PYENV_ROOT",
            "_PEX_PIP_VERSION",
            # This is used by Pex's Pip to inject runtime patches dynamically.
            "_PEX_PIP_RUNTIME_PATCHES",
            # These are used by Pex's Pip venv to provide foreign platform support and work
            # around https://github.com/pypa/pip/issues/10050.
            "_PEX_PATCHED_MARKERS_FILE",
            "_PEX_PATCHED_TAGS_FILE",
            # These are used by Pex's Pip venv to implement universal locks.
            "_PEX_PYTHON_VERSIONS_FILE",
            "_PEX_TARGET_SYSTEMS_FILE",
        )
    ]
    if ignored_pex_env_vars:
        sys.stderr.write(
            "Ignoring the following environment variables in Pex venv mode:\n"
            "{}\n\n".format(
                os.linesep.join(sorted(ignored_pex_env_vars))
            )
        )

    os.environ["VIRTUAL_ENV"] = venv_dir

    # A Python interpreter always inserts the CWD at the head of the sys.path.
    sys.path.insert(0, "")

    bin_path = os.environ.get("PEX_VENV_BIN_PATH", 'false')
    if bin_path != "false":
        PATH = os.environ.get("PATH", "").split(os.pathsep)
        if bin_path == "prepend":
            PATH.insert(0, venv_bin_dir)
        elif bin_path == "append":
            PATH.append(venv_bin_dir)
        else:
            sys.stderr.write(
                "PEX_VENV_BIN_PATH must be one of 'false', 'prepend' or 'append', given: "
                "{!r}\n".format(
                    bin_path
                )
            )
            sys.exit(1)
        os.environ["PATH"] = os.pathsep.join(PATH)

    PEX_EXEC_OVERRIDE_KEYS = ("PEX_INTERPRETER", "PEX_SCRIPT", "PEX_MODULE")
    pex_overrides = {
        key: os.environ.get(key) for key in PEX_EXEC_OVERRIDE_KEYS if key in os.environ
    }
    if len(pex_overrides) > 1:
        sys.stderr.write(
            "Can only specify one of {overrides}; found: {found}\n".format(
                overrides=", ".join(PEX_EXEC_OVERRIDE_KEYS),
                found=" ".join("{}={}".format(k, v) for k, v in pex_overrides.items())
            )
        )
        sys.exit(1)
    if True:
        for key in list(os.environ):
            if key.startswith("PEX_"):
                if key == "PEX_EXTRA_SYS_PATH":
                    # We always want sys.path additions to propagate so that the venv PEX
                    # acts like a normal Python interpreter where sys.path seen in
                    # subprocesses is the same as the sys.executable in the parent process.
                    os.environ["__PEX_EXTRA_SYS_PATH__"] = os.environ.get(
                        "PEX_EXTRA_SYS_PATH"
                    )
                del os.environ[key]

    pex_script = pex_overrides.get("PEX_SCRIPT") if pex_overrides else None
    if pex_script:
        script_path = os.path.join(venv_bin_dir, pex_script)
        os.execv(script_path, [script_path] + sys.argv[1:])

    pex_interpreter = pex_overrides.get("PEX_INTERPRETER", "").lower() in ("1", "true")
    PEX_INTERPRETER_ENTRYPOINT = "code:interact"
    entry_point = (
        PEX_INTERPRETER_ENTRYPOINT
        if pex_interpreter
        else pex_overrides.get("PEX_MODULE", 'isort.main:main' or PEX_INTERPRETER_ENTRYPOINT)
    )
    if entry_point == PEX_INTERPRETER_ENTRYPOINT and len(sys.argv) > 1:
        args = sys.argv[1:]

        python_options = []
        for index, arg in enumerate(args):
            # Check if the arg is an expected startup arg
            if arg.startswith("-") and arg not in ("-", "-c", "-m"):
                python_options.append(arg)
            else:
                args = args[index:]
                break

        # The pex was called with Python interpreter options, so we need to re-exec to
        # respect those:
        if python_options:
            # Find the installed (unzipped) PEX entry point.
            main = sys.modules.get("__main__")
            if not main or not main.__file__:
                # N.B.: This should never happen.
                sys.stderr.write(
                    "Unable to resolve PEX __main__ module file: {}\n".format(main)
                )
                sys.exit(1)

            python = sys.executable
            cmdline = [python] + python_options + [main.__file__] + args
            sys.stderr.write(
                "Re-executing with Python interpreter options: "
                "cmdline={cmdline!r}\n".format(cmdline=" ".join(cmdline))
            )
            os.execv(python, cmdline)

        arg = args[0]
        if arg == "-m":
            if len(args) < 2:
                sys.stderr.write("Argument expected for the -m option\n")
                sys.exit(2)
            entry_point = module = args[1]
            sys.argv = args[1:]
            # Fall through to entry_point handling below.
        else:
            filename = arg
            sys.argv = args
            if arg == "-c":
                if len(args) < 2:
                    sys.stderr.write("Argument expected for the -c option\n")
                    sys.exit(2)
                filename = "-c <cmd>"
                content = args[1]
                sys.argv = ["-c"] + args[2:]
            elif arg == "-":
                content = sys.stdin.read()
            else:
                file_path = arg if os.path.isfile(arg) else os.path.join(arg, "__main__.py")
                with open(file_path) as fp:
                    content = fp.read()

            ast = compile(content, filename, "exec", flags=0, dont_inherit=1)
            globals_map = globals().copy()
            globals_map["__name__"] = "__main__"
            globals_map["__file__"] = filename
            locals_map = globals_map
            exec(ast, globals_map, locals_map)
            sys.exit(0)

    module_name, _, function = entry_point.partition(":")
    if not function:
        import runpy
        runpy.run_module(module_name, run_name="__main__", alter_sys=True)
    else:
        import importlib
        module = importlib.import_module(module_name)
        # N.B.: Functions may be hung off top-level objects in the module namespace,
        # e.g.: Class.method; so we drill down through any attributes to the final function
        # object.
        namespace, func = module, None
        for attr in function.split("."):
            func = namespace = getattr(namespace, attr)
        sys.exit(func())
