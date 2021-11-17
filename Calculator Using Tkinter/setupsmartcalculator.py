from cx_Freeze import *
import sys

includefiles = ['calc.ico']
base=None

if sys.platform == "win32":
    base = 'Win32GUI'

shortcut_table=[
    (
    "DesktopShortcut",
    "DesktopFolder",
    "My Calculator",
    "TARGETDIR",
    "[TARGETDIR]\calculator.exe",
    None,
    None,
    None,
    None,
    None,
    None,
    "TARGETDIR",
    )
]
msi_data={"Shortcut":shortcut_table}

bdist_msi_options={'data':msi_data}
setup(
    version="1.0",
    description="My Calculator",
    author="Somesh Bang",
    name="My Calculator",
    options={'build_exe':{'include_files':includefiles},'bdist_msi_':bdist_msi_options,},
    executables=[
        Executable(script="calculator.py",
        base=base,
        icon='calc.ico'
        )
    ]
)
