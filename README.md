# PY-GOTURN

This is the **python** implementation of **GOTURN: Generic Object Tracking Using Regression Networks.**

**[Learning to Track at 100 FPS with Deep Regression Networks](http://davheld.github.io/GOTURN/GOTURN.html)**,
<br>
[David Held](http://davheld.github.io/),
[Sebastian Thrun](http://robots.stanford.edu/),
[Silvio Savarese](http://cvgl.stanford.edu/silvio/),
<br>

### Why implementation in python, when C++ code is already available?

* Easy to understand the overall pipeline of the algorithm in detail
* Easy to experiment new ideas
* Easy to debug and visualize the network with tools like [visdom](https://github.com/facebookresearch/visdom)
* Easy portability to windows/linux, without having to worry about building third party libraries.

### Outputs

|Car           |  Sunshade |
|------------------------|-------------------------|
|![](https://github.com/nrupatunga/PY-GOTURN/blob/goturn-0.1/output/movie_2.gif)  | ![](https://github.com/nrupatunga/PY-GOTURN/blob/goturn-0.1/output/movie_1.gif) | 
