#!/bin/sh

#git clone https://github.com/floydhub/object-detection-template family-detection

#cd  family-detection

export PYTHONPATH=".:/floyd/home/family-detection:/floyd/home/family-detection/slim:$PYTHONPATH"
python object_detection/legacy/train.py --train_dir=/floyd/home/family_detection_train/ --pipeline_config_path=/floyd/home/family-detection/ssd_mobilenet_v2_coco.config
