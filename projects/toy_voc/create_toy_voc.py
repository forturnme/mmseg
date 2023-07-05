"""
create a toy voc dataset.
sample 300 images from train set and 300 from valid set, and reduce their
segmentation classes.
reduce segmentation annotation classes by putting 'bottle', 'chair', 
'pottedplant', 'sofa', 'tvmonitor',
'bird', 'cat', 'dog', 'cow', 'horse',  'sheep' into 'background'.
the original voc dataset should be in data/VOCdevkit/VOC2012
the processed segmentation annotations should be in
data/VOCdevkit/toyVOC2012/ImageSets/Segmentation
and sampled pictures should be in data/VOCdevkit/toyVOC2012/JPEGImages
"""
import os
import random
import shutil
import xml.etree.ElementTree as ET

import numpy as np
from PIL import Image

def mkdir_if_not_exist(dir_name):
    if not os.path.exists(os.path.join(*dir_name)):
        os.makedirs(os.path.join(*dir_name))

# read original data set images and annotations, then sample 300 images from
# them and copy, paste them to new folder
def read_images_labels(root='./data/VOCdevkit/VOC2012', train=True):
    txt_fname = root + '/ImageSets/Segmentation/' + (
        'train.txt' if train else 'val.txt')
    with open(txt_fname, 'r') as f:
        images = f.read().split()
    data = [os.path.join(root, 'JPEGImages', i+'.jpg') for i in images]
    label = [os.path.join(root, 'SegmentationClass', i+'.png') for i in images]
    return data, label

def copy_images_labels(data, label, output_dir):
    mkdir_if_not_exist(output_dir)
    for i in range(len(data)):
        shutil.copy(data[i], output_dir)
        shutil.copy(label[i], output_dir)

def read_voc_seg_annotations(root='./data/VOCdevkit/VOC2012', train=True):
    txt_fname = root + '/ImageSets/Segmentation/' + (
        'train.txt' if train else 'val.txt')
    with open(txt_fname, 'r') as f:
        images = f.read().split()
    segs = [os.path.join(root, 'SegmentationClass', i+'.png') for i in images]
    return segs

# reduce classes by putting 'bottle', 'chair', 'pottedplant', 'sofa', 'tvmonitor',
# 'bird', 'cat', 'dog', 'cow', 'horse',  'sheep' into 'background'.
def reduce_classes(root='./data/VOCdevkit/VOC2012', train=True):
    # modified pallete
    