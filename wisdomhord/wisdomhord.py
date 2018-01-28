import os.path
import re
import itertools

def hladan(file_path):
    return wisdomhord(file_path)

class wisdomhord(object):

    meta = {}
    keys = []
    _key_row = 0
    _column_lengths = {}

    row_regex = '\[ (.*?)\ ]'

    def __new__(self, file_path):
        self = object.__new__(self)

        if os.path.isfile(file_path):
            self.file_path = file_path
            self.open_hord()
            return self
        else:
            raise ValueError("{} does not exist".format(file_path))

    def open_hord(self):
        with open(self.file_path) as hord:
            for line_index, line in enumerate(hord):
                if line[:2] == '//':
                    self._add_to_meta(line[2:])
                if line[0] == '[':
                    self._add_to_keys(line)
                    self._key_row = line_index
                    break

    def _add_to_meta(self, line):
        values = line.split('::', 1)
        self.meta[values[0].strip()] = values[1].strip()

    def _add_to_keys(self, line):
        keys_definition = re.search(self.row_regex, line).group(1)
        for key in keys_definition.split(' | '):
            stripped_key = key.strip().upper()
            self._column_lengths[stripped_key] = len(key)
            self.keys.append(stripped_key)

    def get_rows(self, limit=None, cols=None):
        def format_row(line, cols):
            row = {}
            row_definition = re.search(self.row_regex, line).group(1)
            for idx, col in enumerate(row_definition.split(' | ')):
                if cols is None:
                    row[self.keys[idx]] = col.strip()
                elif self.keys[idx] in cols:
                    row[self.keys[idx]] = col.strip()
            return row

        if limit is not None:
            limit = self._key_row + 1 + limit

        rows = []
        with open(self.file_path) as hord:
            for line in itertools.islice(hord, self._key_row+1, limit):
                rows.append(format_row(line, cols))
        return rows

    def row_count(self):
        return int(self.meta['COUNT'])
