# 亚马逊云科技【黑客松大赛·初赛】计算机视觉赛题——从图像中检测人

目标检测在图像中找到特定类别的物体并用边界框标记出来。本次比赛，我们进行人(person)的检测。

## 数据准备

本次比赛我们采用[COCO](https://cocodataset.org/) 2017的目标检图片集，只评测其中的person类别检测结果。由于COCO的test set并不公开，本次比赛我们将原有validation set切分为新的validation set和test set。请运行:

```bash
bash prepare_data.sh
```

运行结束后，在`data/`文件夹中会包含`train/`, `val/`和`test/`三个图片文件夹，以及训练集和验证集的标注文件`train.json`, `val.json`。

## 数据格式
标注文件的数据格式遵从COCO的原有格式。`.json`录入后包含`'info', 'licenses', 'images', 'annotations', 'categories'`信息。

其中images是一个list，每条数据包含图片大小，路径等相关信息，例如：

```json
{
    'license': 4,
    'file_name': '000000397133.jpg',
    'coco_url': 'http://images.cocodataset.org/val2017/000000397133.jpg',
    'height': 427,
    'width': 640,
    'date_captured': '2013-11-14 17:02:52',
    'flickr_url': 'http://farm7.staticflickr.com/6116/6255196340_da26cf2c9e_z.jpg',
    'id': 397133
}
```

annotations中的每一条annotation对应于一个物体，包含其边界框，所在图片的image_id，类别等，例如：

```json
{
    'segmentation': [[510.66, 423.01, 511.72, 420.03, 510.45, 416.0, 510.34, 413.02, 510.77, 410.26, 510.77, 407.5, 510.34, 405.16, 511.51, 402.83, 511.41, 400.49, 510.24, 398.16, 509.39, 397.31, 504.61, 399.22, 502.17, 399.64, 500.89, 401.66, 500.47, 402.08, 499.09, 401.87, 495.79, 401.98, 490.59, 401.77, 488.79, 401.77, 485.39, 398.58, 483.9, 397.31, 481.56, 396.35, 478.48, 395.93, 476.68, 396.03, 475.4, 396.77, 473.92, 398.79, 473.28, 399.96, 473.49, 401.87, 474.56, 403.47, 473.07, 405.59, 473.39, 407.71, 476.68, 409.41, 479.23, 409.73, 481.56, 410.69, 480.4, 411.85, 481.35, 414.93, 479.86, 418.65, 477.32, 420.03, 476.04, 422.58, 479.02, 422.58, 480.29, 423.01, 483.79, 419.93, 486.66, 416.21, 490.06, 415.57, 492.18, 416.85, 491.65, 420.24, 492.82, 422.9, 493.56, 424.39, 496.43, 424.6, 498.02, 423.01, 498.13, 421.31, 497.07, 420.03, 497.07, 415.15, 496.33, 414.51, 501.1, 411.96, 502.06, 411.32, 503.02, 415.04, 503.33, 418.12, 501.1, 420.24, 498.98, 421.63, 500.47, 424.39, 505.03, 423.32, 506.2, 421.31, 507.69, 419.5, 506.31, 423.32, 510.03, 423.01, 510.45, 423.01]],
    'area': 702.1057499999998,
    'iscrowd': 0,
    'image_id': 289343,
    'bbox': [473.07, 395.93, 38.65, 28.67],
    'category_id': 18,
    'id': 1768
}
```

## 提交格式

提交文件的格式与标注文件格式类似，依然存于json中，读入后是一个list，每一个entry表示一个物体，具体格式例如：

```json
{
    "image_id": int,
    "category_id": int,
    "bbox": [x,y,width,height],
    "score": float,
}
```
其中score表示对该物体的置信度。

## 本地评测

文件夹中的`eval.py`为本次比赛的评测脚本。我们将使用COCO的评测工具。首先需要安装[COCOAPI](https://github.com/cocodataset/cocoapi.git):

```bash
pip install pycocotools
```

安装完成后运行：

```bash
python eval.py --gt gt.json --pred pred.json
```

程序将会输出不同IoU匹配标准，不同物体大小区间的"mean average precision"，简称AP，例如:

```bash
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.007
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.008
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.008
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.006
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.004
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.004
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.001
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.002
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.002
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.003
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.001
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.001
```

其中，第一行`(AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ]`是我们最终选用的评比指标。
