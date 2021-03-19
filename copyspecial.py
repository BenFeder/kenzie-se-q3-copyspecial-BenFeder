#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Benjamin Feder"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    file_list = os.listdir(dirname)
    special_file_list = []
    special_pattern = r'__\w+__'
    for files in file_list:
        abs_files = os.path.abspath(os.path.join(dirname, files))
        special_find = re.findall(special_pattern, abs_files)
        if special_find:
            special_file_list.append(abs_files)
    return special_file_list


def copy_to(path_list, dest_dir):
    """Gets absolute paths of special files and copies to destination dir"""
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    for files in path_list:
        shutil.copy(files, dest_dir)


def zip_to(path_list, dest_zip):
    """Gets absolute paths of special files and zips them to destination dir"""
    args = ['zip', '-j', dest_zip]
    args.extend(path_list)
    subprocess.run(args)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='get file from directory')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).
    special_files = get_special_paths(ns.from_dir)
    if ns.todir:
        copy_to(special_files, ns.todir)
    elif ns.tozip:
        zip_to(special_files, ns.tozip)
    else:
        for files in special_files:
            print(files)
        parser.print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
