#!/usr/bin/env python3
# coding: utf-8
import sys

from core.subtitle import *

if __name__ == '__main__':
    argv = sys.argv
    if len(sys.argv) < 2:
        print("input movie dir path")
        exit(1)
    path = argv[1]
    cid = cid_hash_file(path)
    url = get_info_url(cid)
    print(f"get hash ${cid} from file ${path}")
    print(f"request from ${url}")
    result = search(path)
    print(f"result ${result}")