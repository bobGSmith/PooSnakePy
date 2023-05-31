from setuptools import setup 

setup(
    name='PooSnake',
    version='1.0.0',
    description='play poosnake in terminal',
    url='https://github.com/bobGSmith/PooSnakePy',
    author='Bob G Smith',
    author_email="bobbyatopk@gmail.com",
    license='MIT',
    packages=["PooSnake"],
    install_requires = ["curses-windows; os_name == 'nt'"]
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8'
    ]
)

__version__ = '1.0.0'
__author__ 'Bob G Smith'