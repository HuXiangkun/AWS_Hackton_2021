import argparse
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

parser = argparse.ArgumentParser()

parser.add_argument('--gt', type=str, required=True)
parser.add_argument('--pred', type=str, required=True)
parser.add_argument('--anntype', type=str, default='bbox')

args = parser.parse_args()

cocogt = COCO(args.gt)
cocopred = cocogt.loadRes(args.pred)

cocoeval = COCOeval(cocogt, cocopred, args.anntype)
cocoeval.params.catIds = [1]
cocoeval.evaluate()
cocoeval.accumulate()
cocoeval.summarize()
