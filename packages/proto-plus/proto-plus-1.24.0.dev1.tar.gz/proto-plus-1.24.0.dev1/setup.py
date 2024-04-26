# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import re
import os

from setuptools import find_namespace_packages, setup

PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

version = None

with open(os.path.join(PACKAGE_ROOT, "proto/version.py")) as fp:
    version_candidates = re.findall(r"(?<=\")\d+.\d+.\d+.dev\d+", fp.read())
    assert len(version_candidates) == 1
    version = version_candidates[0]

with io.open(os.path.join(PACKAGE_ROOT, "README.rst")) as file_obj:
    README = file_obj.read()

setup(
    name="proto-plus",
    version=version,
    license="Apache 2.0",
    author="Google LLC",
    author_email="googleapis-packages@google.com",
    url="https://github.com/googleapis/proto-plus-python.git",
    packages=find_namespace_packages(exclude=["docs", "tests"]),
    description="Beautiful, Pythonic protocol buffers.",
    long_description=README,
    platforms="Posix; MacOS X",
    include_package_data=True,
    install_requires=("protobuf >= 3.19.0, <5.0.0dev",),
    extras_require={
        "testing": [
            "google-api-core >= 1.31.5",
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
)
