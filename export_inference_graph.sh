#!/bin/sh


python object_detection/export_inference_graph.py \
    --input_type image_tensor \
    --pipeline_config_path /floyd/home/family-detection/ssd_mobilenet_v2_coco.config \
    --trained_checkpoint_prefix /floyd/input/family_model/model.ckpt \
    --output_directory /floyd/home/family_export_inference_graph
