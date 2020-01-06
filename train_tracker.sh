IMAGENET_FOLDER='/media/nthere/datasets/ISLVRC2014_Det/dummy'
ALOV_FOLDER='/media/nthere/datasets/ALOV/'
INIT_CAFFEMODEL='./nets/tracker_init.caffemodel'
TRACKER_PROTO='./nets/tracker.prototxt'
SOLVER_PROTO='./nets/solver.prototxt'

python2 -m goturn.train.train \
--imagenet $IMAGENET_FOLDER \
--alov $ALOV_FOLDER \
--init_caffemodel $INIT_CAFFEMODEL \
--train_prototxt $TRACKER_PROTO \
--solver_prototxt $SOLVER_PROTO \
--lamda_shift 5 \
--lamda_scale 15 \
--min_scale -0.4 \
--max_scale 0.4 \
--gpu_id 1
