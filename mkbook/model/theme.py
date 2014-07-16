import os

from mkbook.config import HOST_URL

join = os.path.join

class Theme(object):
    def __init__(self, theme_url, name=None):
        self.path = theme_url
        self.base_path, self.name = os.path.split(theme_url)
        self.name = name or self.name

        statics_folder = join(self.path, "statics")
        css_folder = join(statics_folder, "css")
        js_folder = join(statics_folder, "js")
        self.css_list = [ join(HOST_URL, "statics", "css", _) for _  in os.listdir(css_folder)]
        self.js_list = [ join(HOST_URL, "statics", "js", _) for _  in os.listdir(css_folder)]

        



















