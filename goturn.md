# Single Object Tracking using GOTURN

## Introduction 

Reading through deep learning papers during my work, I found it
interesting how deep learning can be used to estimate the bound box
around the object of interest (eg. **Fast R-CNN**), and extending this
idea to regress the bounding box from frame to frame in a video. It is
also quite intuitive that how such idea can also be incorporated to
other tasks such as object tracking and video segmentation

Stumbling upon, I came across _David Held's GOTURN_ paper, in which
authors proposed a real time(on GPU) neural network for single object
tracking.

Some of the core ideas of the paper is to 

* To train a end to end network in offline mode, while some of the
previous object tracking algorithms are trained in online mode

* How to leverage large amount of videos and image database available
these days to train the network for object tracking, technically to
learn the relationship between object motion and appearance


## What is Single Object Tracking ?

Before we jump on to details, let us understand what do we mean by
'Single Object Tracking'. Basically, if we mark the object of our
interest in one frame of the video, the goal is to track the same object
in the subsequent frames of the videos. Figure below gives the pictorial
definition of it. 
