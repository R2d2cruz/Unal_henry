# from setuptools import setup
#
# setup(
#     name='Horarios UNAL',
#     version='1.0.0',
#     author='Carlos Arturo Cruz Useche\nDiego Alejandro Campos Méndez\nKaren Fonseca Sánchez\nHenry Salomón Suárez López',
#     scripts=['__main__.py'],
#     # packing=[],
#     install_requires=['pyqueue==2.0.0', 'kivy==1.11.1', 'grid==0.7.1']
# )
import cx_Freeze

executables = [
    cx_Freeze.Executable('__main__.py')
]

cx_Freeze.setup(
    name='Horarios UNAL',
    version='1.0.0',
    options={'build_exe': {'packages': [],
                           'include_files': [
        'ProgramObjects/'
    ]}},
    executables=executables
)

# python setup.py build
