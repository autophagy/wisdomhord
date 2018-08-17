class Sweor(object):
    def __new__(self, column_name, column_class):
        self = object.__new__(self)
        self.column_name = column_name.upper()
        self.column_class = column_class
        return self

    def cast_from(self, value):
        if value == "":
            return None
        else:
            return self.column_class.cast_from_hord(value)

    def cast_to(self, value):
        if value == None:
            return ""
        else:
            return self.column_class.cast_to_hord(value)


class Entry(object):
    def __init__(self):
        self.keys = {}

    def get(self, key, default=None):
        if key in self.keys:
            return getattr(self, self.keys[key])
        return default

    def set(self, attr, sweor, key):
        setattr(self, attr, sweor)
        self.keys[key] = attr


class Bisen(object):

    __invoker__ = "Wísdómhord"
    __description__ = "Wísdómhord file"

    def __init__(self, **kwargs):
        self.sweoras = {}
        self.sweoras_attr = {}
        self.values = {}
        for attr in dir(self):
            attr_obj = getattr(self, attr)
            if isinstance(attr_obj, Sweor):
                self.sweoras[attr_obj.column_name] = attr
                self.sweoras_attr[attr] = attr_obj

        if len(self.sweoras.keys()) == 0:
            raise ValueError("Bisen columns definition has no valid columns")

        for k, v in kwargs.items():
            if k in self.sweoras_attr:
                self.values[k] = v

    def cast_from(self, row_dict):
        entry = Entry()
        for k, v in row_dict.items():
            if k in self.sweoras:
                a = self.sweoras[k]
                entry.set(a, self.sweoras_attr[a].cast_from(v), k)

        return entry

    def cast_to(self, insert_bisen):
        casted_dict = {}

        for k, v in insert_bisen.values.items():
            if k in self.sweoras_attr:
                sweor = self.sweoras_attr[k]
                casted_dict[sweor.column_name] = sweor.cast_to(v)

        return casted_dict

    def sweoras(self):
        return list(self.sweoras.keys())
