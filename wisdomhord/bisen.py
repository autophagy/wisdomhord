class Sweor(object):

    def __new__(self, column_name, cast_from_func, cast_to_func):
        self = object.__new__(self)
        self.column_name = column_name.upper()
        self.cast_from_func = cast_from_func
        return self

    def cast_from(self, value):
        if value == '':
            return None
        else:
            return self.cast_from_func(value)

    def cast_to(self, value):
        return self.cast_to_func(value)


class Bisen(object):

    __invoker__ = 'Wísdómhord'
    __description__ = 'Wísdómhord file'

    def __init__(self):
        self.sweoras = {}
        for attr in dir(self):
            attr_obj = getattr(self, attr)
            if isinstance(attr_obj, Sweor):
                self.sweoras[attr_obj.column_name] = attr_obj

        if len(self.sweoras.keys()) == 0:
            raise ValueError("Bisen columns definition has no valid columns")

    def cast_row(self, row_dict):
        casted_dict = {}

        for k, v in row_dict.items():
            if k in self.sweoras:
                casted_dict[k] = self.sweoras[k].cast_from(v)
            else:
                casted_dict[k] = v

        return casted_dict

    def sweoras(self):
        return list(self.sweoras.keys())
