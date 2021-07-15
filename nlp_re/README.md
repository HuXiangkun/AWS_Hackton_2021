# 亚马逊云科技【黑客松大赛·初赛】NLP赛题——关系抽取

## 数据文件格式

关系抽取任务是给定一段文本和其中标明的实体，判断实体之间的关系。本赛题的数据存放于Json格式的文件中。数据的格式如下：

```json
[
    {
        "relations": [ // 由列表构成，列表里每个元素是一个三元组，分别为头实体，关系名，尾实体
            [
                ["List", "of", "tokens", "for", "head", "entity"],
                "relation name",
                ["List", "of", "tokens", "for", "tail", "entity"]
            ],
            ...
        ]
    }, 
    {
        "text": "The text that contains entities and implies their relations"
    },
    {
        "entities": [ // 文本中的实体，列表中的每个元素都是一个token list
            ["List", "of", "tokens", "for", "entity_0"],
            ...
        ]
    },
    ...
]
```

文本中会出现`<ENT_0>`、 `<ENT_1>`等等这类的token，它们指代`"entities"`中的实体，`<ENT_i>`就是指代`"entities"`中第`i`个实体。

该赛题的任务是给定`"text"`和`"entities"`，预测`"entities"`中各实体之间的关系。关系的Label存放在`"relations"`中。

该文件夹的数据文件有`train.json`, `dev.json`, `test.json`，分别为训练集，开发集和测试集。其中测试集中没有`"relations"`字段，选手需要预测出测试集中的实体关系提交给主办方。提交的格式为：

```json
[
    [ // 第0条数据的关系列表，列表里每个元素是一个三元组，分别为头实体，关系名，尾实体
        [
                ["List", "of", "tokens", "for", "head", "entity"],
                "relation name",
                ["List", "of", "tokens", "for", "tail", "entity"]
            ],
            ...
    ],
    ...
]
```

具体可以参考文件夹中`dev_gt.json`的格式。

## 评测脚本

文件夹中的`eval.py`为本次比赛的评测脚本，选手可以调用脚本中的`evaluate`函数，或者将dev集的预测按照上述格式输出到文件中，如`dev_pred.json`中，然后运行脚本得到开发集的性能：
```bash
python eval.py dev_pred.json dev_gt.json
```
