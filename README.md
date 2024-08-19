# README

[Flet](https://flet.dev/) desktop-app to extract Japanese reading with [SudachiPy](https://github.com/WorksApplications/SudachiPy) .

![img](./images/demo.png)

## Build

Create venv.

```
python -m venv .venv
```

Install packages:

```
python -m pip install flet
python -m pip install sudachipy
python -m pip install sudachidict_core
```

### Steps

1. Enter venv ([Skippable on VSCode.](https://github.com/microsoft/vscode-python/wiki/Activate-Environments-in-Terminal-Using-Environment-Variables))

    ```
    .\.venv\Scripts\activate
    ```

1. Run:

    ```
    pyinstaller --onefile --name yomi --collect-data sudachidict_core --collect-data sudachipy --noconsole main.py
    ```

    - If error was raised around pathlib, uninstall it: `python -m pip uninstall pathlib -y`
    - After build, re-install: `python -m pip install pathlib`

1. Exit from venv ([Skippable on VSCode.](https://github.com/microsoft/vscode-python/wiki/Activate-Environments-in-Terminal-Using-Environment-Variables))

    ```
    deactivate
    ```

---

When running a build using pyinstaller installed with `pip install pyinstaller`, the generated `.exe` file may be considered a virus by Windows Defender.
In this case, using a locally built pyinstaller may solve the problem.

Steps (**run below inside venv**):

1. `git clone https://github.com/pyinstaller/pyinstaller`
1. `cd .\pyinstaller\bootloader\`
1. `python .\waf all`
    - There may be error, but it is ignorable.
    - Visual Studio C++ compiler is required for build.
        - It can be installed with [Scoop](https://scoop.sh/) : `scoop install vcredist2015` .
    - In my environment, 2015 and 2022 were installed. If just installing vcredist2015 results in error, try installing the latest version as well.
1. `cd ..` (move to `pyinstaller` directory)
1. `pip install .`

This will build pyinstaller in the python site-package folder.
The folder used for the build is no longer used, so you can delete it.

---

[Sudachi](https://github.com/WorksApplications/Sudachi/) and [SudachiDict](https://github.com/WorksApplications/SudachiDict) are both licensed under the [Apache License, Version2.0](http://www.apache.org/licenses/LICENSE-2.0.html) .