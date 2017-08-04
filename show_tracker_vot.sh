DEPLOY_PROTO='/home/nrupatunga/Work-2017/DeepLearning/Code/GOTURN/nets/tracker.prototxt'
CAFFE_MODEL='/home/nrupatunga/Work-2017/DeepLearning/Code/GOTURN/nets/trained_models/caffenet_train_iter_150000.caffemodel'
TEST_DATA_PATH='/media/nrupatunga/data/datasets/VOT/VOT2014/vot2014/'

python -m goturn.test.show_tracker_vot \
--p $DEPLOY_PROTO \
--m $CAFFE_MODEL \
--i $TEST_DATA_PATH \
--g 0
