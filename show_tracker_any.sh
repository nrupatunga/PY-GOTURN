DEPLOY_PROTO='./nets/tracker.prototxt'		 
CAFFE_MODEL='./nets/tracker.caffemodel'		
TEST_DATA_PATH='/media/nthere/datasets/pegan'		

python2 -m goturn.test.show_tracker_any \
	--p $DEPLOY_PROTO \
	--m $CAFFE_MODEL \
	--i $TEST_DATA_PATH \
	--g 0
