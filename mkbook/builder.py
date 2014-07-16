import os
import shutil

from jinja2 import Environment, FileSystemLoader

from config import THEME_PATH, CONTENT_PATH, OUTPUT_PATH
from model.theme import Theme

class FlatBuilder(object):
    def __init__(self, book_path):
        self.env = Environment(loader=FileSystemLoader(THEME_PATH))
        self.flat_page_template = self.env.get_template('flat-page.html')
        self.theme = Theme(THEME_PATH)

        self.render_dict = {
            "theme": self.theme

        }

    def build(self):
        if not os.path.exists(OUTPUT_PATH):
            os.makedirs(OUTPUT_PATH)

        cur_theme_static_folder = os.path.join(self.theme.path, "statics")
        print "cur_theme_static_folder:%s"%cur_theme_static_folder
        target_theme_static_folder = os.path.join(OUTPUT_PATH, self.theme.name, "statics")
        print "target_theme_static_folder:%s"%target_theme_static_folder
        shutil.copytree(cur_theme_static_folder, target_theme_static_folder)

        content = self.flat_page_template.render(**self.render_dict)
        target_file = os.path.join(OUTPUT_PATH, "index.html")
        with open(target_file, 'w') as f:
            f.write(content)






