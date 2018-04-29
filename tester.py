#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a module to test md5sum performance on different machines
"""

__author__ = "flyingbot91"
__copyright__ = "Copyright 2018"
__date__ = "2018/04/29"
__credits__ = ["flyingbot91"]
__license__ = " GPLv3"
__version__ = "0.0.1"
__maintainer__ = "flyingbot91"
__email__ = "flyingbot91@gmx.com"
__status__ = "Development"

import os

workdir = os.getcwd()


def create_file(filepath, filesize):
    """
    Create
    :param filepath: (str) Fully-qualified file path
    :param filesize: Filesize (in bytes)
    :return:
    """

    with open(filepath, 'wb') as bigfile:
        bigfile.seek(filesize)
        bigfile.write('0')


def main():
    filesizes = [1024, 1024*1024, 1024*1024, 5*1024*1024]
    for filesize in filesizes:
        create_file(os.path.join(workdir, str(filesize)), filesize)


if __name__ == '__main__':
    main()
