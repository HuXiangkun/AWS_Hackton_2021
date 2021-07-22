# 亚马逊云科技【黑客松大赛·复赛】计算机视觉赛题——从图像中检测人体关键点

本次比赛，我们进行人体关键点的检测。

## 数据准备

本次比赛我们采用[COCO](https://cocodataset.org/) 2017的人体关键点图片集。由于COCO的test set并不公开，我们将原有validation set切分为新的validation set和test set。请运行:

```bash
bash prepare_data.sh
```

运行结束后，在`data/`文件夹中会包含`train/`, `val/`, `test/`三个图片文件夹，训练集和验证集的标注文件`train_gt.json`, `val_gt.json`以及测试集图片信息`test.json`。

## 数据格式
标注文件的数据格式遵从COCO的原有格式。`.json`录入后包含`'info', 'licenses', 'images', 'annotations', 'categories'`信息。`test.json`不包含`annotations`信息。

其中images是一个list，每条数据包含图片大小，路径等相关信息，例如：

```json
{
    'license': 4,
    'file_name': '000000397133.jpg',
    'folder': 'val',
    'height': 427,
    'width': 640,
    'date_captured': '2013-11-14 17:02:52',
    'flickr_url': 'http://farm7.staticflickr.com/6116/6255196340_da26cf2c9e_z.jpg',
    'id': 397133
}
```
参赛者可通过解析`folder`和`file_name`字段组合出图片在`data/`文件夹中的相对路径，比如`val/000000397133.jpg`。

annotations中的每一条annotation对应于一个物体，包含其边界框，所在图片的image_id，类别等，例如：

```json
{
    'num_keypoints': 1,
    'area': 13769.89065,
    'keypoints': [0,0,0,0, ..., 603, 68, 2, 0,0,0,...,0]
    'image_id': 37670,
    'bbox': [436.85,23.73,203.15,161.8],
    'category_id': 1,
    'id': 448259
}
```

## 提交格式

提交文件的格式与标注文件格式类似，依然存于json中，读入后是一个list，每一个entry表示一个物体，具体格式例如：

```json
{
    "image_id": int,
    "category_id": int,
    "keypoints": [x1,y1,v1,...,xk,yk,vk],
    "score": float,
}
```

其中keypoints是一组`x,y,v`值，表示每个关键点在图上的x,y坐标和是否可见，目前建议将所有的v都设为1，同时score表示对该物体的置信度。示例提交文件如[链接](https://github.com/cocodataset/cocoapi/blob/master/results/person_keypoints_val2014_fakekeypoints100_results.json)中所示。

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
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets= 20 ] = 0.010
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets= 20 ] = 0.010
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets= 20 ] = 0.010
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets= 20 ] = 0.010
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets= 20 ] = 0.010
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 20 ] = 0.001
 Average Recall     (AR) @[ IoU=0.50      | area=   all | maxDets= 20 ] = 0.002
 Average Recall     (AR) @[ IoU=0.75      | area=   all | maxDets= 20 ] = 0.001
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets= 20 ] = 0.001
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets= 20 ] = 0.002
```

其中，第一行`(AP) @[ IoU=0.50:0.95 | area=   all | maxDets= 20 ]`是我们最终选用的评比指标。
