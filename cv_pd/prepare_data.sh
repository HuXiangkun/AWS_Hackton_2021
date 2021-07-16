mkdir data
cd data
wget http://images.cocodataset.org/zips/train2017.zip
unzip train2017.zip
rm train2017.zip
mv train2017 train
wget http://images.cocodataset.org/zips/val2017.zip
unzip val2017.zip
rm val2017.zip
mv val2017 val
wget https://dgl-data.s3.us-west-2.amazonaws.com/dataset/hackathon2021/test.json
wget https://dgl-data.s3.us-west-2.amazonaws.com/dataset/hackathon2021/train_gt.json
wget https://dgl-data.s3.us-west-2.amazonaws.com/dataset/hackathon2021/val_gt.json
mkdir test
python prepare_test_set.py
cd ..
