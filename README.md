# PY-GOTURN

This is the **python** implementation of **GOTURN: Generic Object Tracking Using Regression Networks.**

**[Learning to Track at 100 FPS with Deep Regression Networks](http://davheld.github.io/GOTURN/GOTURN.html)**,
<br>
[David Held](http://davheld.github.io/),
[Sebastian Thrun](http://robots.stanford.edu/),
[Silvio Savarese](http://cvgl.stanford.edu/silvio/),
<br>

### Outputs

|Car           |  Sunshade |
|------------------------|-------------------------|
|![](https://github.com/nrupatunga/PY-GOTURN/blob/goturn-0.1/output/movie_2.gif)  | ![](https://github.com/nrupatunga/PY-GOTURN/blob/goturn-0.1/output/movie_1.gif) | 


### Why implementation in python, when [C++ code](https://github.com/davheld/GOTURN) is already available?

* Easy to understand the overall pipeline of the algorithm in detail
* Easy to experiment new ideas
* Easy to debug and visualize the network with tools like [visdom](https://github.com/facebookresearch/visdom)
* Little effort in portability to other OS

### Functionalites added so far
- [X] Training the deep network on Imagenet and ALOV dataset

- [X] Test code for VOT


### How to train your own tracker

You need to download the following datasets first 

* *__ALOV dataset__* - The ALOV video dataset can be downloaded here: http://alov300pp.joomlafree.it/

* *__Imagenet dataset__* - Download the DET dataset (47GB) and bounding box annotations (15MB) from [Imagenet](http://www.image-net.org/download-images). Extract the training images and the annotations.

Once you extracted the dataset please make the following changes in __train_tracker.sh__:


**IMAGENET_FOLDER**: this folder should contain **images** and **gt**. The folder structure is as shown below.

|images           | gt  |
|------------------------|-------------------------|
|![](https://github.com/nrupatunga/PY-GOTURN/blob/goturn-0.1/doc/images/imagenet_images.jpg)  | ![](https://github.com/nrupatunga/PY-GOTURN/blob/goturn-0.1/doc/images/imagenet_gt.jpg) | 

**ALOV_FOLDER**: this folder should contain **images** and **gt**. The folder structure is as shown below.


|images           | gt  |
|------------------------|-------------------------|
|![](https://github.com/nrupatunga/PY-GOTURN/blob/goturn-0.1/doc/images/alov_images.jpg)  | ![](https://github.com/nrupatunga/PY-GOTURN/blob/goturn-0.1/doc/images/alov_gt.jpg) | 
