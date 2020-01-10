import requests


def check_is_chinese(str_or_bytes):
    if type(str_or_bytes) == bytes:
        new_str = str_or_bytes.decode('utf-8', errors='ignore')
        if check_contains_chinese(new_str):
            return True
        new_str = str_or_bytes.decode('gbk', errors='ignore')
        if check_contains_chinese(new_str):
            return True
    elif check_contains_chinese(str_or_bytes):
        return True
    return False


def check_contains_chinese(unicode_str):
    for c in unicode_str:
        if '\u4e00' <= c <= '\u9fa5':
            return True
    return False


if __name__ == '__main__':
    url1 = 'http://subtitle.v.geilijiasu.com/D8/BA/D8BAA139D8A49C5BC26C1326CF6DE5FF10157006.srt'

    r1 = requests.get(url1)
    print(check_is_chinese(r1.content))
    print(r1.content.decode('gbk'))
