import os
import json
import shutil

with open('test.json', 'r') as f:
    data = json.load(f)

for img in data['images']:
    val_path = os.path.join('val', img['file_name'])
    test_path = os.path.join('test', img['file_name'])
    assert os.path.exists(val_path)
    shutil.move(val_path, test_path)
