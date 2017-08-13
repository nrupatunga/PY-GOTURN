## How to test on VOT dataset

You need to download the following datasets first 

**VOT** - The VOT video dataset can be downloaded here: http://www.votchallenge.net/vot2014/dataset.html

Once you extracted the dataset please make the following changes in __show_tracker_vot.sh__

**DEPLOY_PROTO**: Path to deploy prototxt

**CAFFE_MODEL**: Path to trained caffe model

**TEST_DATA_PATH**: Path to VOT folder

The folder structure is shown below

|VOT           |
|------------------------|
|![](https://github.com/nrupatunga/PY-GOTURN/blob/goturn-0.1/doc/images/vot.jpg)|

Run the following command
```
bash show_tracker_vot.sh

```
