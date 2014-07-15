from jinja2 import Environment, FileSystemLoader

from config import THEME_PATH, CONTENT_PATH, OUTPUT_PATH

class FlatBuilder(object):
    def __init__(self, book_path):
        self.env = Environment(loader=FileSystemLoader(THEME_PATH))
        self.flat_page_template = self.env.get_template('flat-page.html')
        self.theme = Theme(THEME_PATH)

        self.render_dict = {
            "theme": self.theme

        }

    def build(self):
        content = self.flat_page_template.render(**self.render_dict)
        target_file = os.path.join(OUTPUT_PATH, "index.html")
        with open(target_file, 'w') as f:
            f.write(content)






