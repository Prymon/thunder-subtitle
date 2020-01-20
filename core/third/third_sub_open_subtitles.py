from core.third.third_sub_factory import BaseSub

'''
refers:
- https://github.com/emericg/OpenSubtitlesDownload
- https://www.opensubtitles.org/zh/search/subs
'''


class ThirdSubOpenSubtitles(BaseSub):
    def search_and_save_sub_by_abs_movie_path(file_abs_path: str) -> (str, str):
        # TODO
        # python core/third/OpenSubtitlesDownload.py --cli -s hash test.mkv
        pass
