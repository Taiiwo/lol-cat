from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\taiiwo\AppData\Local\Programs\Python\Python35\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\taiiwo\AppData\Local\Programs\Python\Python35\tcl\tk8.6'

buildOptions = dict(
    includes = ["queue"],
    packages = [],
    excludes = [],
    include_files =  [
        r"C:\Users\taiiwo\AppData\Local\Programs\Python\Python35\DLLs\tcl86t.dll",
        r"C:\Users\taiiwo\AppData\Local\Programs\Python\Python35\DLLs\tk86t.dll"
    ]
)

setup(name = "lolcat" ,
    version = "0.1" ,
    description = "" ,
    options = dict(build_exe = buildOptions),
    executables = [Executable("lolcat.py")]
)
