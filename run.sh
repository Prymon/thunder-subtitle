#! /bin/bash
echo "activate conda"
source /volume1/z/service/share/conda/bin/activate
conda -V
python -V
echo "begin to run"
sleep 1
cd $(dirname $0);
python main.py /volume1/z/电影/
python main.py /volume1/z/剧集/
python main.py /volume1/z/垃圾箱/
python main.py /volume1/z/rss/
