# -*- coding: utf-8 -*-
import json
import os
import sys

base_dir = os.path.dirname(__file__)
sys.path.insert(0, base_dir)


from . import __version__
from .main_widget import entry_point
from .sup import Global, get_files_list, mkdir_with_p, if_to_consider


def preparing():
    Global.root = base_dir

    Global.output_dir = os.path.join(Global.root, "output")

    Global.images = {}
    ds_path = "dataset_GDV_first_stage_class_v3"
    ds_path = os.path.join(Global.root, ds_path)
    ds_path = os.path.abspath(ds_path)
    files = get_files_list(ds_path)
    files = sorted(files, reverse=False)
    files.remove(os.path.join(ds_path, "README.md"))
    for file_i in files:
        file_i_id, _ = os.path.splitext(os.path.basename(file_i))
        file_i_id = int(file_i_id)
        Global.images[file_i_id] = file_i
    Global.images_len = len(Global.images)

    json_path = "imgs_considered.json"
    json_path = os.path.join(Global.root, json_path)
    json_path = os.path.abspath(json_path)
    s = ""
    with open(json_path, "r", encoding="utf-8") as fd:
        s = fd.read()
    Global.image_meta = json.loads(s)

    Global.images_indexes = []
    for id_i in range(1, Global.images_len+1):
        meta_i = Global.image_meta[f"{id_i}"]
        if if_to_consider(meta_i):
            Global.images_indexes.append(id_i)
    Global.images_indexes_len = len(Global.images_indexes)

    needed_dirs = [os.path.join(Global.output_dir, dir_i) for dir_i in ["0", "1", "2", "3", "4"]]
    [mkdir_with_p(dir_i) for dir_i in needed_dirs]


def main():
    preparing()

    print("main entered")
    entry_point()
