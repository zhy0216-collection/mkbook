import os



class Theme(object):
    def __init__(self, theme_url, name=None):
        self.path = theme_url
        self.base_path, self.name = os.path.split(theme_url)
        self.name = name or self.name
        self.css_list = []
        self.js_list = []

        



















