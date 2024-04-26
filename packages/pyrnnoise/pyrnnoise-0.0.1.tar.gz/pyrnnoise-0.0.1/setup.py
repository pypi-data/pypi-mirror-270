# Copyright (c) 2024 Zhendong Peng (pzd17@tsinghua.org.cn)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from setuptools import setup, find_packages


with open("requirements.txt", encoding="utf8") as f:
    requirements = f.readlines()

if sys.platform == "darwin":
    OS = "Operating System :: POSIX :: MacOS"
elif sys.platform.startswith("win"):
    OS = "Operating System :: Microsoft :: Windows"
elif sys.platform.startswith("linux"):
    OS = "Operating System :: POSIX :: Linux"
else:
    OS = "Operating System :: OS Independent"

setup(
    name="pyrnnoise",
    version=open("VERSION", encoding="utf8").read(),
    author="Zhendong Peng",
    author_email="pzd17@tsinghua.org.cn",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    description="PyRNNoise",
    url="https://github.com/pengzhendong/pyrnnoise",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "denoise = pyrnnoise.cli:main",
        ]
    },
    classifiers=[
        OS,
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ],
)
