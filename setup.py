from setuptools import setup

setup(
    name='Horarios UNAL',
    version='1.0.0',
    author='Carlos Arturo Cruz Useche\nDiego Alejandro Campos Méndez\nKaren Fonseca Sánchez\nHenry Salomón Suárez López',
    scripts=['__main__.py'],
    # packing=[],
    install_requires=['pyqueue==2.0.0', 'kivy==1.11.1', 'grid==0.7.1']
)
