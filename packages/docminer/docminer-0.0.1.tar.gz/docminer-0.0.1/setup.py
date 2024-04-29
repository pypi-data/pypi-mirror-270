# -*- coding: utf-8 -*-
# Author: ZKH
# Date：2021/3/23
from distutils.core import setup

from setuptools import find_packages

if __name__ == "__main__":
    setup(
        name="docminer",
        version="0.0.1",
        author="wangzhe",
        author_email="wang91zhe@163.com",
        description="Non OCR document parsing",
        url="https://www.yunquna.com/",
        long_description="支持PDF、Word、Excel等文档解析",
        long_description_content_type="text/markdown",
        include_package_data=True,
        py_modules=[],
        package_data={},
        packages=find_packages(),
        install_requires=[],
        entry_points={
            "console_scripts": [],
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    )
