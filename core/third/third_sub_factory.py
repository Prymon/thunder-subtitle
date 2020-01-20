import requests

def all_sub_providers():
    return []

class BaseSub(object):
    def __init__(self):
        super().__init__()

    def search_and_save_sub_by_abs_movie_path(file_abs_path: str) -> (str, str):
        '''
        search subtitle by movie hash
        then save besides movie file
        implement me
        '''
        return None

    def _file_path_to_subtitle_file_path(file_path, subtitle_name):
        suffix = ".ass"
        if subtitle_name.rfind('.') != -1 and subtitle_name.rfind('.') != len(subtitle_name) - 1:
            suffix = subtitle_name[subtitle_name.rfind('.'):]
        file_path = file_path if file_path.rfind(".") == -1 else file_path[:file_path.rfind(".")]
        return file_path + suffix

    def _check_is_chinese(download_url):
        def check_contains_chinese(unicode_str):
            for c in unicode_str:
                if '\u4e00' <= c <= '\u9fa5':
                    return True
            return False

        r = requests.get(download_url)
        content_bytes = r.content
        if type(content_bytes) == bytes:
            new_str = content_bytes.decode('utf-8', errors='ignore')
            if check_contains_chinese(new_str):
                return True
            new_str = content_bytes.decode('gbk', errors='ignore')
            if check_contains_chinese(new_str):
                return True
        elif check_contains_chinese(content_bytes):
            return True
        return False
