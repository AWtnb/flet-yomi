# README

[Flet](https://flet.dev/) desktop-app to extract Japanese reading with [SudachiPy](https://github.com/WorksApplications/SudachiPy) .

![img](./images/demo.png)

## Build

1. Install SudachiPy, SudachiDict-core, PyInstaller:

    ```
    pip install sudachipy sudachidict_core pyinstaller
    ```

1. Create a directory named `assets` in the same directory as `main.py`.

    ```
    .\
    │  main.py
    │  sudachi.py
    │
    └─assets
    ```

1. Find `sudachipy` and `sudachidict_core` folder inside Python site-package folder and copy them into `assets` folder.

    ```
    .\
    │  main.py
    │  sudachi.py
    │
    └─assets
        ├─sudachidict_core
        │  └─...
        │
        └─sudachipy
            └─...
    ```

1. Run below command.

    ```
    pyinstaller --onefile --name yomi --add-data assets\sudachidict_core;sudachidict_core --add-data assets\sudachipy;sudachipy --noconsole main.py
    ```

    + Use `pyinstaller` command instead of `flet pack` because `flet` command does not accept multiple `--add-data`.

---

When running a build using pyinstaller installed with `pip install pyinstaller`, the generated `.exe` file may be considered a virus by Windows Defender.
In this case, using a locally built pyinstaller may solve the problem.

Steps:

1. `git clone https://github.com/pyinstaller/pyinstaller`
1. `cd .\pyinstaller\bootloader\`
1. `python .\waf all`
    + Visual Studio C++ compiler is required for build.
        + It can be installed with [Scoop](https://scoop.sh/) : `scoop install vcredist2015` .
    + In my environment, 2015 and 2022 were installed. If just installing vcredist2015 results in error, try installing the latest version as well.
1. `pip install .`

This will build pyinstaller in the python site-package folder.
The folder used for the build is no longer used, so you can delete it.
