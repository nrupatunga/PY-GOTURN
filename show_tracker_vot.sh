DEPLOY_PROTO='../nets/tracker.prototxt'		 
CAFFE_MODEL='../nets/_iter_100000.caffemodel'		
TEST_DATA_PATH='/media/nrupatunga/Data-Backup/DL/goturn/vot2014'		

python -m goturn.test.show_tracker_vot \
	--p $DEPLOY_PROTO \
	--m $CAFFE_MODEL \
	--i $TEST_DATA_PATH \
	--g 0
