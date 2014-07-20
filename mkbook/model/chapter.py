import copy
import re
import os

from mkbook.utils import (gen_id, parse_filename, get_create_time)
from mkbook.logger import logger

class Chapter(object):

    def __init__(self, folder_url):
        self.id = gen_id()
        self.title = ""
        self.url = ""
        self.index = 0
        self.section_list = []
        self.folder_url = folder_url
        self.folder_name = self.filename = os.path.split(folder_url)[1]
        self.is_folder = True
        self.create_time = get_create_time(folder_url)
        self._parse_chapter_folder_name()

    def _parse_chapter_folder_name(self):
        self.index, self.title = parse_filename(self.folder_name)

    def add_section(self, section):
        self.section_list.append(section)

    def build(self, render_dict):
        if not self.is_folder:
            return

        logger.debug("build chapter page here")
        result = copy.copy(render_dict)
        result["cur_chapter"] = self



    def __str__(self):
        return "<Chapter: %s, %s>" % (self.title, self.index)

