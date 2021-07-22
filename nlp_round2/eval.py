import sys
import json
from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction


def evaluate(references, hypothesis):
    # check for empty lists
    references_, hypothesis_ = [], []
    for i, refs in enumerate(references):
        refs_ = [ref for ref in refs if ref.strip() != '']
        if len(refs_) > 0:
            references_.append([ref.split() for ref in refs_])
            hypothesis_.append(hypothesis[i].split())

    chencherry = SmoothingFunction()
    return corpus_bleu(references_, hypothesis_, smoothing_function=chencherry.method3)


if __name__ == '__main__':
    pred_file = sys.argv[1]
    gt_file = sys.argv[2]

    predictions = json.load(open(pred_file))
    ground_truths = json.load(open(gt_file))

    print(evaluate(ground_truths, predictions))

