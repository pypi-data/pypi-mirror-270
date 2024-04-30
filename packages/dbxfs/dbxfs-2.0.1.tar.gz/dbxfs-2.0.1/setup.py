#!/usr/bin/env python3

# This file is part of dbxfs.

# dbxfs is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# dbxfs is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with dbxfs.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dbxfs",
    version='2.0.1',
    author="Rian Hunter",
    author_email="rian@alum.mit.edu",
    description="User-space file system for Dropbox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://thelig.ht/code/dbxfs',
    license="GPL3",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Filesystems',
    ],
    packages=["dbxfs"],
    package_data={"dbxfs": ["py.typed"]},
    python_requires='>=3.11',
    install_requires=[
        # dropbox changes so often that we
        # just put a lower bound to avoid
        # dbxfs being uninstallable in the future
        # if dropbox=11 goes away.
        "dropbox>=11.25.0",
        "platformdirs>=4.1.0,<5",
        "userspacefs>=3.1.0,<4",
        "block_tracing>=1.0.1,<2",
        "privy>=6.0,<7",
        "sentry_sdk>=1.39,<2",
        'pywin32;sys_platform=="win32"',
    ],
    extras_require={
        'safefs': ["safefs"],
    },
    entry_points={
        'console_scripts': [
            "dbxfs=dbxfs.main:main",
        ],
    },
)
