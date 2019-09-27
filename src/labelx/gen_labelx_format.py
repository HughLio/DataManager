# -*- coding:utf-8 -*-
from __future__ import print_function

"""
Version:
    - V1.0 initialization 
    - V1.1 support create json with multiple label, support sort json with label name 10/09/18
    - V1.2 support create json without label 
    - V1.3 support set default label 

Todo:
    - support perfix (like:http://*bkt/*/)
    - suport labelmap (ex: map 0, 1, 2 to pulp, sexy, normal)
"""

import os
import json
import argparse


parser = argparse.ArgumentParser(description='convert url label list to json')
parser.add_argument('url_label', help='url label file path', type=str)
parser.add_argument('-m', '--multiple_label',
                    help='add -m to create json with multiple labels', action='store_true')
parser.add_argument('-s', '--sort',
                    help='add -s to sort json with labels', action='store_true')
parser.add_argument('-wol', '--without_label',
                    help='add -wol to create json without label', action='store_true')
parser.add_argument('-df', '--default_label',
                    help='set default label', type=str, default=None)
parser.add_argument('-type' ,'--dataset_type', choices=['cls', 'det'],
                        help='default is general', default='cls', type=str)
args = parser.parse_args()


def make_labelX_json(url=None, label=None):
    """
    url, type, <source_url>, <ops>,
    label:
        [{
        "data": [{"class": "normal"}],
        "version": "1",
        "type": "classification",
        "name": "terror" / "pulp" / "general"
        }]
    """
    if label:
        data = [{"class": label}]
    else:
        data = []
    if args.dataset_type == 'cls':
        label_json = {"data": data,
                  "type": "classification", "name": 'pulp'}
    elif args.dataset_type == 'det':
        label_json = {"data": data,
                      "type": "detection", "name": 'general'}
    ava_json = {"url": url, "label": [label_json]}
    return ava_json


def write_to_json(json_lists, output):
    # 输出到文件中
    with open(output, 'w') as fi:
        for json_list in json_lists:
            json.dump(json_list, fi)  # 不使用indent
            fi.write('\n')


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def main():
    labelmap = ["pulp", "sexy", "normal"]
    input_file = args.url_label
    json_lists = []
    if args.without_label:
        with open(input_file, 'r') as f:
            for line in f:
                uri = line.strip().split('\t')[0]
                json_list = make_labelX_json(uri, None)
                json_lists.append(json_list)

    elif args.default_label:
        with open(input_file, 'r') as f:
            for line in f:
                uri = line.strip().split('\t')[0]
                json_list = make_labelX_json(
                    uri, args.default_label)
                json_lists.append(json_list)

    elif args.multiple_label:
        with open(input_file, 'r') as f:
            for line in f:
                uri, label1, label2 = line.strip().split('\t')
                json_list = make_labelX_json(uri, label1)
                second = {"class": label2}
                json_list['label'][0]['data'].append(second)
                json_lists.append(json_list)
        if args.sort:
            label = json_lists[0]['label'][0]['data'][0]['class']
            if represents_int(label.split('_')[0]):
                json_lists = sorted(json_lists, key=lambda k: int(
                    k['label'][0]['data'][0]['class'].split('_')[0]))
            else:
                json_lists = sorted(
                    json_lists, key=lambda k: k['label'][0]['data'][0]['class'])
    else:
        with open(input_file, 'r') as f:
            for line in f:
                uri, label = line.strip().split(' ')
                json_list = make_labelX_json(uri, labelmap[int(label)])
                json_lists.append(json_list)
        if args.sort:
            label = json_lists[0]['label'][0]['data'][0]['class']
            print(label)
            if represents_int(label.split('_')[0]):
                json_lists = sorted(json_lists, key=lambda k: int(
                    k['label'][0]['data'][0]['class'].split('_')[0]))
            else:
                json_lists = sorted(
                    json_lists, key=lambda k: k['label'][0]['data'][0]['class'])

    output = os.path.splitext(input_file)[0] + '.json'
    write_to_json(json_lists, output)
    print("Save file: {}".format(output))


if __name__ == '__main__':
    main()