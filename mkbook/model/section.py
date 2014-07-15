
from mkbook.utils import gen_id, parse_filename


class Section(object):

    def __init__(self, filename):
        self.id = gen_id()
        self.filename = filename
        self.title = ""
        self.index = 0
        self.content = ""

        self._parse_filename()

    def _parse_filename(self):
        self.index, self.title = parse_filename(self.folder_name)

