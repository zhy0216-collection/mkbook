import os

from mkbook.utils import gen_id, parse_filename, get_create_time


class Section(object):

    def __init__(self, file_url):
        self.id = gen_id()
        self.folder_name, self.filename = os.path.split(file_url)
        self.title = ""
        self.index = 0
        self.content = ""
        self.create_time = get_create_time(file_url)
        
        self._parse_filename()

    def _parse_filename(self):
        self.index, self.title = parse_filename(self.filename)

