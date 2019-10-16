# -*- coding:utf-8 -*-

from __future__ import print_function

"""
修改图片的名字, 统一名字为 "prefix_date_index_suffix.jpg”, 并且去除坏图
    --inputImagesPath 图片存储路径 [required]
    --rename set "--rename" to start rename image
    --date 时间  [default: 1234]
    --prefix 图片前缀，默认为label的名字
    --suffix 图片后缀
    --ext 图片的格式 [default = jpg]

Version:
    - 20180413      V1.1
    - 20180523      V1.2
    - 20180929      V1.3 add '" "' to path for mv

Todo:
    -
"""

import os
import argparse
import cv2
import numpy as np

from collections import defaultdict


def parse_args():
    parser = argparse.ArgumentParser(description="md5 process check image")
    parser.add_argument('--inputImagesPath', type=str, required=True)
    parser.add_argument('--rename', action='store_true',
                        help='set "--rename" to rename image')
    parser.add_argument('--date', type=str, default='1234',
                        help='time, "1234" by default')
    parser.add_argument('--ext', type=str, default='jpg',
                        help='图片的格式, "jpg" by default')
    return parser.parse_args()


def checkValidImages(file_path):
    try:
        img = cv2.imread(file_path)
    except:
        img = None
    if np.shape(img) == () or np.shape(img)[2] == 4:
        print("ERROR INFO : %s can't read" % file_path)
        return False
    return True


def checkFileIsImages(file_path):
    if ('JPEG' in file_path.upper()) or ('JPG' in file_path.upper()) \
            or ('PNG' in file_path.upper()) or ('BMP' in file_path.upper()):
        return True
    return False


def getAllImages(base_path=None):
    all_image_list = []
    for parent, dirnames, filenames in os.walk(base_path):
        for f in filenames:
            image_path_name = os.path.join(parent, f)
            #if checkFileIsImages(image_path_name) and checkValidImages(image_path_name):
            all_image_list.append(image_path_name)
            #else:
                # print("%s isn't image"%(image_path_name))
             #   pass
    return all_image_list


# os.walk()获得多层路径所有的图片


def getAllImagesWithGroup(basePath=None):
    """
    获得所有类别目录下的所有图片，并且以字典的形式返回图片路径
    """
    all_image_list_with_group = defaultdict(list)
    for parent, dirnames, filenames in os.walk(basePath):
        for f in filenames:
            image_path_name = os.path.join(parent, f)
           # if checkFileIsImages(image_path_name) and checkValidImages(image_path_name):
            dir = os.path.split(image_path_name)[0]
            label = dir.split('/')[-1]
            all_image_list_with_group[label].append(image_path_name)
            #else:
             #   print("%s isn't image" % image_path_name)
              #  pass
    return all_image_list_with_group


def rename_image(original_name, new_name):
    cmd_str = "mv '{}' '{}'".format(original_name, new_name)
    # print cmd_str
    if args.rename:
        result_flag = os.system(cmd_str)


def rename_process_with_label(all_image_list_with_group, date, ext):
    for label in all_image_list_with_group.keys():
        num = 0
        for imagePath in all_image_list_with_group[label]:
            path_prefix = os.path.split(imagePath)[0]
            new_name = (label + '_{}_{:0>5}' +
                        '.' + ext).format(date, num)
            num += 1
            rename_image(imagePath, os.path.join(path_prefix, new_name))


def rename_process(all_images_path_list):
    for image_path in all_images_path_list:
        # 获得图片的label信息
        image_path = os.path.abspath(image_path)
        image_name, suffix = os.path.splitext(image_path)
        # 定义图片的新名字
        new_name = image_name + '.jpg'
        original_name = image_path
        if suffix != '.jpg':
            rename_image(original_name, new_name)


args = parse_args()


def main():
    # allImagesPathList = getAllImages(basePath=args.inputImagesPath)
    # rename_process(allImagesPathList)
    all_image_list_with_group = getAllImagesWithGroup(
        basePath=args.inputImagesPath)
    rename_process_with_label(all_image_list_with_group,
                              args.date, args.ext)


if __name__ == '__main__':
    print('Start processing')
    main()
    print('End ...')