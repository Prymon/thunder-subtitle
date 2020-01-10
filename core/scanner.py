import os


def scan_files_in_dir(dir_path, callback):
    dir_path = os.path.abspath(dir_path)
    try:
        if not os.path.isdir(dir_path) or not os.path.exists(dir_path):
            print(f"invalid dir {dir_path}")
            return
        for files in os.listdir(dir_path):
            next_path = dir_path + "/" + files
            if os.path.isfile(next_path):
                callback(next_path)
            if os.path.isdir(next_path):
                scan_files_in_dir(next_path, callback)
    except Exception:
        print("scan meets error")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    def cb(path):
        print("..." + path)


    scan_files_in_dir("./", cb)
