IMAGENET_FOLDER='/home/nrupatunga/Work-2017/DeepLearning/Code/GOTURN/goturn-debug/imagenet/'
ALOV_FOLDER='/home/nrupatunga/Work-2017/DeepLearning/Code/GOTURN/goturn-debug/VOT/'
INIT_CAFFEMODEL='/home/nrupatunga/Work-2017/DeepLearning/Code/GOTURN/nets/models/weights_init/tracker_init.caffemodel'
TRACKER_PROTO='/home/nrupatunga/Work-2017/DeepLearning/Code/GOTURN/nets/tracker.prototxt'
SOLVER_PROTO='/home/nrupatunga/Work-2017/DeepLearning/Code/GOTURN/nets/solver.prototxt'

python -m goturn.train.train \
--imagenet $IMAGENET_FOLDER \
--alov $ALOV_FOLDER \
--init_caffemodel $INIT_CAFFEMODEL \
--train_prototxt $TRACKER_PROTO \
--solver_prototxt $SOLVER_PROTO \
--lamda_shift 5 \
--lamda_scale 15 \
--min_scale -0.4 \
--max_scale 0.4 \
--gpu_id 0 
