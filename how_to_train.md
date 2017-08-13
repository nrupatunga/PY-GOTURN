### How to train your own tracker

You need to download the following datasets first 

* *__ALOV dataset__* - The ALOV video dataset can be downloaded here: http://alov300pp.joomlafree.it/

* *__Imagenet dataset__* - Download the DET dataset (47GB) and bounding box annotations (15MB) from [Imagenet](http://www.image-net.org/download-images). Extract the training images and the annotations.

Once you extracted the dataset please make the following changes in __train_tracker.sh__:


**IMAGENET_FOLDER**: this folder should contain **images** and **gt** (annotations). The folder structure is as shown below.

|images           | gt  |
|------------------------|-------------------------|
|![](https://github.com/nrupatunga/PY-GOTURN/blob/goturn-0.1/doc/images/imagenet_images.jpg)  | ![](https://github.com/nrupatunga/PY-GOTURN/blob/goturn-0.1/doc/images/imagenet_gt.jpg) | 

**ALOV_FOLDER**: this folder should contain **images** and **gt** (annotations). The folder structure is as shown below.


|images           | gt  |
|------------------------|-------------------------|
|![](https://github.com/nrupatunga/PY-GOTURN/blob/goturn-0.1/doc/images/alov_images.jpg)  | ![](https://github.com/nrupatunga/PY-GOTURN/blob/goturn-0.1/doc/images/alov_gt.jpg) | 

**INIT_CAFFEMODEL**: Path to [pretrained model](http://cs.stanford.edu/people/davheld/public/GOTURN/weights_init/tracker_init.caffemodel)

**TRACKER_PROTO**: Path to tracker.prototxt

**SOLVER_PROTO**: Path to solver.prototxt


Run the following command
```
bash train_tracker.sh

```

