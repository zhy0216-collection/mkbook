import udid

_filename_re = re.compile(r"(\d+)\.(.+)")

def gen_id():
    return uuid.uuid4().hex

def parse_filename(filename):
    result = _folder_re.findall(filename)
    if len(result) > 0:
        return result[0]
    else:
        return (0, filename)