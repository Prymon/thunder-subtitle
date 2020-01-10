#!/usr/bin/env python3
# coding: utf-8
import os
import sys

import requests

from core.scanner import scan_files_in_dir
from core.subtitle import search


def check_file_is_movie(file_path):
    return os.path.exists(file_path) and os.path.isfile(file_path) and os.path.getsize(file_path) > 50000000


def file_path_to_subtitle_file_path(file_path, subtitle_name):
    suffix = ".ass"
    if subtitle_name.rfind('.') != -1 and subtitle_name.rfind('.') != len(subtitle_name) - 1:
        suffix = subtitle_name[subtitle_name.rfind('.'):]
    file_path = file_path if file_path.rfind(".") == -1 else file_path[:file_path.rfind(".")]
    return file_path + suffix


def download_file(url, save_path):
    try:
        r = requests.get(url)
        with open(save_path, "wb") as code:
            code.write(r.content)
    except BaseException as e:
        print(f"download {url} to {save_path} failed..")
        return


def check_subtitle_exists(file_path):
    movie_name = os.path.basename(file_path)
    movie_dir = os.path.dirname(file_path)
    movie_name = movie_name if movie_name.rfind(".") == -1 else movie_name[:movie_name.rfind(".")]
    for suffix in '.ass', '.srt', '.smi', '.ssa', '.sub':
        sub_name = movie_name + suffix
        sub_path = movie_dir + "/" + sub_name
        if os.path.exists(sub_path) and os.path.isfile(sub_path):
            return True
    return False


def process(file_path):
    try:
        if not check_file_is_movie(file_path):
            return
        # check if already has subtitle
        if check_subtitle_exists(file_path):
            print(f"subtitle exists {file_path}")
            return
        # download
        search_result = search(file_path)
        if not search_result:
            return
        subtitle_name, download_url = search_result[0], search_result[1]
        subtitle_file_path = file_path_to_subtitle_file_path(file_path, subtitle_name)
        if not os.path.exists(subtitle_file_path):
            print(f"download sub from {download_url} to {subtitle_file_path}")
            download_file(download_url, subtitle_file_path)
    except Exception:
        print("downloads meets error")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    argv = sys.argv
    if len(sys.argv) < 2:
        print("input movie dir path")
        exit(1)
    path = argv[1]
    scan_files_in_dir(path, process)
    process(path)
