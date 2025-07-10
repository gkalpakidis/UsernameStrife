from setuptools import setup, find_packages

setup(
    name="username-strife",
    version="0.1",
    description="A username combination generator for AD-style naming conventions.",
    author="Georgios Kalpakidis",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "username-strife=username-strife.cli:main",
        ],
    },
)