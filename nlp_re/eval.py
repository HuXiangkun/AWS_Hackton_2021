import sys
import json

def evaluate(predictions, ground_truths):
    assert len(predictions) == len(ground_truths)
    correct_re = 0
    re_cnt = 0
    gt_cnt = 0
    for pred, gt in zip(predictions, ground_truths):
        _pred = []
        for p in pred:
            if p not in _pred:
                _pred.append(p)
        for p in _pred:
            if p in gt:
                correct_re += 1
        re_cnt += len(_pred)
        gt_cnt += len(gt)
    if re_cnt <= 0:
        return 0.
    p = correct_re / re_cnt
    r = correct_re / gt_cnt
    f1 = 2 * p * r / (p + r)

    return f1

if __name__ == "__main__":
    pred_file = sys.argv[1]
    gt_file = sys.argv[2]

    predictions = json.load(open(pred_file))
    ground_truths = json.load(open(gt_file))
    f1 = evaluate(predictions, ground_truths)
    print(f'F1 score: {f1}')
