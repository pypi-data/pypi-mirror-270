from setuptools import setup

setup(
    name="pycheckers",
    version="0.0.2",
    install_requires=[
        "graphics.py",
    ],
    packages=["pycheckers"],
    entry_points={
        "console_scripts": [
            "checkers = pycheckers.host:main",
        ],
    },
)
