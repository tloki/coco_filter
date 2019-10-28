#!/usr/bin/env bash

import os.path

DIR = "/Users/loki/Datasets/COCO2017/labels/val2014_display"
CLS = [63, 64, 68]
#      tvmonitor, laptop, cellphone

cls_map = {63: "0", 64: "0", 68: "0"}
offset = -1

imgs = entries = os.listdir(DIR)
mx = -1
split = " "

for label_file in imgs:
    with open(os.path.join(DIR, label_file), "r") as input_file:
        lines = input_file.readlines()

    new_lines = []
    for line in lines:
        delete = True

        for cls in CLS:
            if line.startswith(str(cls + offset) + split):
                delete = False
                break

        if not delete:
            old_index = int(line.split(split)[0])
            new_index = str(cls_map[int(old_index - offset)])

            rest = line[len(split) + len(str(old_index))::]

            new_lines.append(new_index + split + rest)

    if len(new_lines) > 0:
        print(os.path.join(DIR, label_file))
        with open(os.path.join(DIR, label_file), "w") as f:
            for line in new_lines:
                    f.write(line)
    else:
        os.remove(os.path.join(DIR, label_file))