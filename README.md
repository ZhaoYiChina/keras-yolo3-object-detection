# keras-yolo3-object-detection

## Introduction

基于keras-yolo3，实现目标检测。系统配置：
1. windows 10
2. pycharm 2020.1.1 (Professional Edition)
3. python 3.6.8
4. keras 2.1.6
5. tensorflow 1.8.0
6. yolo 3

---

## Quick Start

1. 下载keras yolov3 的权重和配置组合文件（yolo.h5）
```
链接：https://pan.baidu.com/s/1RLj5IQFL9dAJ1hdd7BDy2A 
提取码：kxew 
```
2. Run YOLO detection.
```
python yolo_vedio.py --image
#输入当前目录下需要检测的图像名称带扩展名
```

## Training


## Some issues to know
1. 注意看 .gitignore 文件，其中包含不上传的代码和文件目录
    1. log 训练日志，包含训练期间生成的权重文件，可直接使用
    2. VOCdevkit 标注好的数据集，采用labelImg进行标注
    3. yolov3.weights 适用于Darknet的权重文件，和yolov3.cfg文件可转换成yolo.h5文件
    4. model_data/yolo.h5 yolov3的keras权重及配置组合文件，太大，根据上述云盘下载即可
    5. .idea/* _pycache_/* pycharm工程自带文件

