import re
import os

from mkbook.utils import (gen_id, parse_filename, get_create_time)

class Chapter(object):

    def __init__(self, folder_url):
        self.id = gen_id()
        self.title = ""
        self.index = 0
        self.section_list = []
        self.folder_name = os.path.split(folder_url)[1]
        self.create_time = get_create_time(folder_url)
        self._parse_chapter_folder_name()

    def _parse_chapter_folder_name(self):
        self.index, self.title = parse_filename(self.folder_name)

