
from cx_Freeze import *

includefiles=['mine.ico']

base = None
if sys.platform=='win32':
    base='win32GUI'

shortcut_table=[
    [
        'DesktopShortcut',  #shortcut
        'DesktopFolder',    #Diretory_
        'Typing Booster...', #name
        'TARGETDIR',        #component_
        '[TARGETDIR]:Typing Booster.exe',  #target
        None, #argument
        None, #description
        None, #hotkey
        None, #icon
        None, #icondex
        None, #showcmd
         'TARGETDIR' #wkdir
    ]
]
msi_data= {'shortcut':shortcut_table}
bdist_msi_options= {'data': msi_data}
setup(
    version = "0.1",
    description='Typing Booster...',
    author='Mohammed Huzaifa',
    name='Typing Booster',
    options={"build_exe":{'include_files':includefiles},'bdist_msi':bdist_msi_options},
    executables=[
        Executable(
            script='typing speed.py',
            base=base,
            icon='mine.ico',
        )
    ]
)


