# README

[Flet](https://flet.dev/) desktop-app to extract Japanese reading with [SudachiPy](https://github.com/WorksApplications/SudachiPy) .

![img](./images/demo.png)

## Build

Create venv.

```
python -m venv .venv
```

Install packages (inside venv):

```
.\.venv\Scripts\activate

python -m pip install flet
python -m pip install sudachipy
python -m pip install sudachidict_core
```

Build pyinstaller locally (`.exe` generated with pip-installed pyinstaller is often considered as virus by security soft):

1. Clone pyinstaller from Github.

    ```
    git clone https://github.com/pyinstaller/pyinstaller
    ```

1. Move to installed dir.

    ```
    cd .\pyinstaller\bootloader\
    ```

1. Run command:

    ```
    python .\waf all
    ```

    - **Build would fail, but it is ignorable.**
    - Visual Studio C++ compiler is required for build.
        - It can be installed with [Scoop](https://scoop.sh/) : `scoop install vcredist2015` .
    - In my environment, 2015 and 2022 were installed. If just installing vcredist2015 results in error, try installing the latest version as well.
1. Move to `pyinstaller` directory

    ```
    cd ..
    ```


1. Install locally build pyinstaller.

    ```
    pip install .
    ```

1. Delete `pyinstaller` folder.
    - This folder is used only for package build and no longer used.

1. Run pyinstaller

    ```
    pyinstaller --onefile --name yomi --collect-data sudachidict_core --collect-data sudachipy --noconsole main.py
    ```

    - If error was raised around pathlib, uninstall it: `python -m pip uninstall pathlib -y`
    - After build, re-install: `python -m pip install pathlib`



---

[Sudachi](https://github.com/WorksApplications/Sudachi/) and [SudachiDict](https://github.com/WorksApplications/SudachiDict) are both licensed under the [Apache License, Version2.0](http://www.apache.org/licenses/LICENSE-2.0.html) .
