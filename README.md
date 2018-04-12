# PY-GOTURN

### News
I'm back on working on this codebase again, can expect the following
changes on the development branch **goturn-dev**

- [X] Code clean up

- [ ] Bug fixes, if any

- [ ] Try to add much better interface for easy debugging -
Visualization of training, understanding different modules of the code.

- [ ] Documentation or blog on the code.

**NOTE:** Please switch to **goturn-0.1** branch to try out stable
version. 

---

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

To train your own tracker, please follow the [guide](https://github.com/nrupatunga/PY-GOTURN/blob/goturn-0.1/how_to_train.md)

### How to test on VOT dataset

To test your own tracker on VOT2014, please follow the [guide](https://github.com/nrupatunga/PY-GOTURN/blob/goturn-0.1/how_to_test.md)

### Contact
Please write to me at nrupatunga.tunga@gmail.com, if you have any suggestions or any new functionality you like to see. 
