"""Setup file for rypm."""

from pathlib import Path
from setuptools import setup, find_packages

from rypm import __main__ as main

PKG = "rypm"

preq = Path("requirements.txt").read_text(encoding="utf-8").splitlines()

setup(
    name=PKG,
    version=main.__version__,
    description="Ryuuzaki Ryuusei Plugin Manager",
    long_description="Manage and install additional plugins for Ryuuzaki Ryuusei Discord bot.",
    url="https://github.com/ryuuRyuusei/rypm",
    author="nattadasu",
    author_email="hello@nattadasu.my.id",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    package_dir={PKG: "rypm"},
    python_requires=">=3.10",
    install_requires=preq,
    entry_points={
        "console_scripts": [
            "rypm = rypm.__main__:main"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Communications :: Chat",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="ryuuzaki ryuusei discord bot plugin manager",
    project_urls={
        "Bug Reports": "https://github.com/ryuuRyuusei/rypm/issues",
        "Source": "https://github.com/ryuuRyuusei/rypm",
    },
)
