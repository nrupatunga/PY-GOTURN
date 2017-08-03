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


### Why implementation in python, when C++ code is already available?

* Easy to understand the overall pipeline of the algorithm in detail
* Easy to experiment new ideas
* Easy to debug and visualize the network with tools like [visdom](https://github.com/facebookresearch/visdom)
* little effort in portability to other OSes

### Functionalites added
- [X] Training the deep network on Imagenet and ALOV dataset

- [X] Test code for VOT
