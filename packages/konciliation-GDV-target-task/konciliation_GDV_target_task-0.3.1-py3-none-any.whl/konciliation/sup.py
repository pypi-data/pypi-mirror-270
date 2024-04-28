# -*- coding: utf-8 -*-

import os

class Global:
    root = None
    output_dir = None
    images = None
    images_len = None
    image_meta = None
    images_indexes = None
    images_indexes_len = None


def mkdir_with_p(path: str):
    os.makedirs(path, exist_ok=True)


def get_files_list(dir_path: str) -> list:
    return [os.path.join(path, name) for path, subdirs, files in os.walk(dir_path) for name in files]


def get_data_from_img_name(image_name: str) -> "(real, pred, p_of_0, p_of_1, p_of_2, p_of_3, p_of_4)":
    image_name = os.path.basename(image_name)
    image_name, _ = os.path.splitext(image_name)
    this_img_meta = Global.image_meta[image_name]
    real, pred = this_img_meta["real"], this_img_meta["pred"]
    p_of_0, p_of_1, p_of_2 = this_img_meta["p_of_0"], this_img_meta["p_of_1"], this_img_meta["p_of_2"]
    p_of_3, p_of_4 = this_img_meta["p_of_3"], this_img_meta["p_of_4"]
    return (real, pred, p_of_0, p_of_1, p_of_2, p_of_3, p_of_4)


def get_img_path_by_id(image_id: int, folder: str) -> str or None:
    files = get_files_list(folder)
    for file_i in files:
        file_i_name = os.path.basename(file_i)
        if file_i_name == f"{image_id}.png":
            return file_i
    return None


def if_to_consider(image_meta: dict) -> bool:
    # return True
    real, pred = image_meta["real"], image_meta["pred"]
    ps = [image_meta["p_of_0"], image_meta["p_of_1"], image_meta["p_of_2"], image_meta["p_of_3"], image_meta["p_of_4"]]
    if real != pred:
        f = False
        for p_i in ps:
            if p_i >= 85.0:
                f = True
                break
        if f:
            return True
    for i in range(len(ps)):
        for j in range(i+1, len(ps)):
            if ps[i] >= 35.0 and ps[j] >= 35.0:
                return True
    return False


def is_int(s: str) -> bool:
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True
