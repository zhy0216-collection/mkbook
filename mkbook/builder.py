import os
import shutil

from jinja2 import Environment, FileSystemLoader

from config import THEME_PATH, CONTENT_PATH, OUTPUT_PATH
from model import Chapter, Section, Theme
from utils import force_copy
from logger import logger

class FlatBuilder(object):
    def __init__(self, book_path):
        self.env = Environment(loader=FileSystemLoader(THEME_PATH))
        self.flat_page_template = self.env.get_template('flat-page.html')
        self.theme = Theme(THEME_PATH)
        self.chapter_list = []

        self.render_dict = {
            "theme": self.theme

        }

        self.parse_chapter()

    def parse_chapter(self):
        for file_name in os.listdir(CONTENT_PATH):
            if file_name.startswith("."):
                continue

            abs_file_path = os.path.join(CONTENT_PATH, file_name)
            chapter = Chapter(abs_file_path)
            chapter.url = "/content/%s"%chapter.folder_name
            logger.debug("chapter:%s" % chapter)
            self.chapter_list.append(chapter)

        self.chapter_list.sort(key=lambda x:x.index)
        self.render_dict["chapter_list"] = self.chapter_list
        logger.debug("self.render_dict:%s" % self.render_dict)


    def build(self):
        if not os.path.exists(OUTPUT_PATH):
            os.makedirs(OUTPUT_PATH)

        cur_theme_static_folder = os.path.join(self.theme.path, "statics")
        target_theme_static_folder = os.path.join(OUTPUT_PATH, "statics")

        force_copy(cur_theme_static_folder, target_theme_static_folder)
        target_content_path = os.path.join(OUTPUT_PATH, "content")

        force_copy(CONTENT_PATH, target_content_path)

        content = self.flat_page_template.render(**self.render_dict)
        target_file = os.path.join(OUTPUT_PATH, "index.html")
        with open(target_file, 'w') as f:
            f.write(content)






