"""
create a toy voc dataset.
sample 300 images from train set and 300 from valid set, and reduce their
segmentation classes.
reduce classes by putting 'bottle', 'chair', 'pottedplant', 'sofa', 'tvmonitor',
'bird', 'cat', 'dog', 'cow', 'horse',  'sheep' into 'background'.
the original voc dataset should be in data/VOCdevkit/VOC2012
the processed segmentation annotations should be in
data/VOCdevkit/toyVOC2012/ImageSets/Segmentation
and sampled pictures should be in data/VOCdevkit/toyVOC2012/JPEGImages
"""
