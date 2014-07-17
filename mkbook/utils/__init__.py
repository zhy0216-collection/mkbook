import re
import shutil
import os
import uuid

_filename_re = re.compile(r"(\d+)\.(.+)")

def gen_id():
    return uuid.uuid4().hex

def parse_filename(filename):
    result = _filename_re.findall(filename)
    if len(result) > 0:
        return int(result[0][0]), result[0][1].strip()
    else:
        return (0, filename)

def get_create_time(filename):
    return os.path.getctime(filename)

def force_copy(original_path, target_path):
    if os.path.exists(target_path):
        shutil.rmtree(target_path)

    shutil.copytree(original_path, target_path)

