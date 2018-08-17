import os.path
import re
import itertools
import datarum

from .bisen import Bisen


def hladan(file_path, bisen=Bisen):
    return Wisdomhord(file_path, bisen)


def cennan(file_path, bisen=Bisen):
    now = datarum.wending.now()

    b = bisen()

    with open(file_path, "xt") as hord:
        hord.write("// INVOKER :: {}\n".format(b.__invoker__))
        hord.write("// DESCRIPTION :: {}\n".format(b.__description__))
        hord.write(
            "// INCEPT :: {}\n".format(
                now.strftime("{daeg} {month} {gere} // {tid_zero}.{minute_zero}")
            )
        )
        hord.write(
            "// UPDATED :: {}\n".format(
                now.strftime("{daeg} {month} {gere} // {tid_zero}.{minute_zero}")
            )
        )
        hord.write("// COUNT :: 0\n\n")
        hord.write("[ {} ]".format(" | ".join(b.sweoras)))

    return hladan(file_path, bisen)


class Wisdomhord(object):

    meta = {}
    keys = []
    _key_row = 0
    _column_lengths = {}

    row_regex = "\[ (.*?)\ ]"

    def __new__(self, file_path, bisen=Bisen):
        self = object.__new__(self)

        if os.path.isfile(file_path):
            self.file_path = file_path
            self.open_hord()
            self.bisen = bisen()
            return self
        else:
            raise ValueError("{} does not exist".format(file_path))

    def open_hord(self):
        with open(self.file_path, "r") as hord:
            self.meta = {}
            self.keys = []
            for line_index, line in enumerate(hord):
                if line[:2] == "//":
                    self._add_to_meta(line[2:])
                if line[0] == "[":
                    self._add_to_keys(line)
                    self._key_row = line_index
                    break

    def _add_to_meta(self, line):
        values = line.split("::", 1)
        self.meta[values[0].strip()] = values[1].strip()

    def _add_to_keys(self, line):
        keys_definition = re.search(self.row_regex, line).group(1)
        for key in keys_definition.split(" | "):
            stripped_key = key.strip().upper()
            self._column_lengths[stripped_key] = len(key)
            self.keys.append(stripped_key)

    def get_rows(
        self,
        limit=None,
        cols=None,
        filter_func=lambda x: True,
        sort_by=None,
        reverse_sort=False,
    ):
        if limit is not None:
            limit = self._key_row + 1 + limit

        rows = []
        with open(self.file_path) as hord:
            for line in itertools.islice(hord, self._key_row + 1, limit):
                row = self.bisen.cast_from(self.format_row(line, cols))
                if filter_func(row):
                    rows.append(row)

        if sort_by:
            return sorted(
                rows, key=lambda x: x.get(sort_by.column_name), reverse=reverse_sort
            )
        else:
            return rows

    def format_row(self, line, cols=None):
        row = {}
        row_definition = re.search(self.row_regex, line).group(1)
        for idx, col in enumerate(row_definition.split(" | ")):
            if cols is None:
                row[self.keys[idx]] = col.strip()
            elif self.keys[idx] in cols:
                row[self.keys[idx]] = col.strip()
        return row

    def row_count(self):
        return int(self.meta["COUNT"])

    def insert(self, bisen):
        def format_cell(cell, col_length):
            c = str(cell).strip()
            return "{0}{1}".format(c, " " * (col_length - len(c)))

        def update_column_lengths(row_dict, column_lengths):
            a = dict(
                map(
                    lambda kv: (kv[0], max(len(str(kv[1])), column_lengths[kv[0]])),
                    row_dict.items(),
                )
            )
            if a != column_lengths:
                return True, a
            else:
                return False, column_lengths

        assert type(bisen) is self.bisen.__class__

        casted_row_dict = self.bisen.cast_to(bisen)
        update_lengths, self._column_lengths = update_column_lengths(
            casted_row_dict, self._column_lengths
        )

        row_framework = "[ {} ]\n"
        ordered_row = []
        for key in self.keys:
            ordered_row.append(
                format_cell(casted_row_dict[key], self._column_lengths[key])
            )

        row = row_framework.format(" | ".join(ordered_row))

        with open(self.file_path, "r") as hord:
            hord_buffer = hord.readlines()[self._key_row + 1 :]

        with open(self.file_path, "w") as hord:
            # Update metadata
            self.meta["COUNT"] = self.row_count() + 1
            self.meta["UPDATED"] = datarum.wending.now().strftime(
                "{daeg} {month} {gere} // {tid_zero}.{minute_zero}"
            )

            for k, v in self.meta.items():
                hord.write("// {0} :: {1}\n".format(k, v))

            hord.write("\n")

            # Pad out keys
            padded_keys = list(
                map(
                    lambda x: "{0}{1}".format(
                        x, " " * (self._column_lengths[x] - len(x))
                    ),
                    self.keys,
                )
            )
            hord.write(row_framework.format(" | ".join(padded_keys)))

            # Insert new row
            hord.write(row)

            for line in hord_buffer:
                if update_lengths:
                    padded_cells = list(
                        map(
                            lambda kv: format_cell(kv[1], self._column_lengths[kv[0]]),
                            self.format_row(line).items(),
                        )
                    )
                    line = row_framework.format(" | ".join(padded_cells))
                hord.write(line)
