# thanks to [weaming/thunder-subtitle](https://github.com/weaming/thunder-subtitle)
# scan files > 50MB and download subtitle from thunder service

# dependency(use python 3.*)

## 1. install conda
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda-latest-Linux-x86_64.sh
install：https://www.jianshu.com/p/edaa744ea47d

## 2. enter conda
source $conda_home/bin/activate
conda create -n python37 python=3.7
pip install request

## 3. run

```shell
cd $thunder-subtitle
./main.py [scan_path] [overwrite]

eg:
./main.py /volume1/z/movie
./main.py /volume1/z/movie overwrite
```
