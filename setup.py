import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os"],
    "excludes": ["tkinter"],
    "path": sys.path + ['src'],
    "include_files": ["./src/assets"]
}
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Space invader",
    version="0.0.1",
    description="Space invader",
    options={"build_exe": build_exe_options},
    executables=[Executable("./src/index.py", base=base,
                            targetName="Space-evolution", icon="src/assets/images/menu/start.jpg")]
)
