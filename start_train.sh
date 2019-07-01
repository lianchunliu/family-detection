#!/bin/sh

floyd run --gpu --env tensorflow-1.13 --data lianchun227/datasets/family_data/3:family_data --data lianchun227/datasets/family_model/1:family_model 'bash train.sh'

