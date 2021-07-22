# 亚马逊云科技【黑客松大赛·复赛】NLP赛题——RDF-to-Text

## 数据文件格式

RDF-to-Text任务是给定一个知识图谱（rdf三元组列表），生成该知识图谱的文本描述。三元组的内容为`(头实体, 关系, 尾实体)`。

本赛题的数据存放于JSON格式的文件中。数据的格式如下：
```json
[
    {
        "text": "The text that describes the rdf triples",
        "rdf": [
            ["head entity", "relation name", "tail entity"],
            ...
        ]
    },
    ...
]
```

该赛题的任务是给定`"rdf"`，生成`"text"`中的内容。

该文件夹的数据文件有`train.json`, `dev.json`, `test.json`，分别为训练集，开发集和测试集。其中测试集中没有`"text"`字段，选手需要生成测试集中的文本提交给主办方。提交的格式为：

```json
[
    "Text for example 0",
    "Text for example 1",
    ...
]
```

具体可以参考文件夹中`dev_gt.json`的格式。

## 评测脚本

文件夹中的`eval.py`为本次比赛的评测脚本，选手可以调用脚本中的`evaluate`函数，或者将dev集的预测按照上述格式输出到文件中，如`dev_pred.json`中，然后运行脚本得到开发集的性能：
```bash
python eval.py dev_pred.json dev_gt.json
```
