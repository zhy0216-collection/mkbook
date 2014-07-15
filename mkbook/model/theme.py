import os



class Theme(object):
    def __init__(self, theme_url, title=None):
        self.base_path, name = os.path.split(theme_url)
        self.title = title or name
        self.css_list = None
        self.js_list = None

        



















