# 亚马逊云科技【黑客松大赛·初赛】计算机视觉赛题——从图像中检测人

目标检测是在图像中找到特定类别的物体并用边界框标记出来的任务。本次比赛，我们进行人(person)的检测。

## 数据准备

本次比赛我们采用[COCO](https://cocodataset.org/) 2017的目标检测图片集，只评测其中的person类别检测结果。由于COCO的test set并不公开，我们将原有validation set切分为新的validation set和test set。请运行:

```bash
bash prepare_data.sh
```

运行结束后，在`data/`文件夹中会包含`train2017/`, `val2017/`两个图片文件夹（由于我们将原有validation set切分为新的validation set和test set，测试图片也在val2017中），训练集和验证集的标注文件`train_gt.json`, `val_gt.json`以及测试集图片信息`test.json`。

## 数据格式
标注文件的数据格式遵从COCO的原有格式。`.json`录入后包含`'info', 'licenses', 'images', 'annotations', 'categories'`信息。`test.json`不包含`annotations`信息。

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
参赛者可通过解析`coco_url`字段提取出图片在`data/`文件夹中的相对路径，比如`val2017/000000397133.jpg`。

annotations中的每一条annotation对应于一个物体，包含其边界框，所在图片的image_id，类别等，例如：

```json
{
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
其中score表示对该物体的置信度。示例提交文件如[链接](https://github.com/cocodataset/cocoapi/blob/master/results/instances_val2014_fakebbox100_results.json)中所示。

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
