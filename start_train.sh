#!/bin/sh

floyd run --gpu --env tensorflow-1.13 --data lianchun227/datasets/family_data/6:family_data 'bash train.sh'

