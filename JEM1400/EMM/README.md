EMMonitor

paddle_env
conda create --name paddle_env python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

[paddleOCR](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.4/doc/doc_ch/quickstart.md)
conda activate paddle_env
nvcc --version
python3 -m pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple
--or-- python3 -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
pip install "paddleocr>=2.0.1"
pip3 install -U https://paddleocr.bj.bcebos.com/whl/layoutparser-0.0.0-py3-none-any.whl
