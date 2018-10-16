import datetime
import datarum
import re


class BaseType(object):
    @staticmethod
    def cast_to_hord(value):
        return str(value)


class String(BaseType):
    @staticmethod
    def cast_from_hord(value):
        return String.escape_characters(value, reverse=True)

    @staticmethod
    def cast_to_hord(value):
        return String.escape_characters(value)

    @staticmethod
    def escape_characters(value, reverse=False):
        escapes = [("|", "\|"), ("\n", "\\n")]
        for escape in escapes:
            escape = escape[::-1] if reverse else escape
            value = value.replace(*escape)
        return value


class Boolean(BaseType):
    @staticmethod
    def cast_from_hord(value):
        return value == "True"

    @staticmethod
    def cast_to_hord(value):
        return "True" if value else "False"


class Integer(BaseType):
    @staticmethod
    def cast_from_hord(value):
        return int(value)


class Float(BaseType):
    @staticmethod
    def cast_from_hord(value):
        return float(value)


class DateTime(BaseType):
    @staticmethod
    def cast_from_hord(value):
        return datetime.datetime.strptime(value, "%d.%m.%Y // %H.%M.%S")

    @staticmethod
    def cast_to_hord(value):
        return datetime.datetime.strftime(value, "%d.%m.%Y // %H.%M.%S")


class Wending(BaseType):
    @staticmethod
    def cast_from_hord(value):
        return datarum.wending.strptime(
            value, "{daeg} {month} {gere} // {tid_zero}.{minute_zero}.{second_zero}"
        )

    @staticmethod
    def cast_to_hord(value):
        return value.strftime(
            "{daeg} {month} {gere} // {tid_zero}.{minute_zero}.{second_zero}"
        )


class Coordinate(BaseType):
    @staticmethod
    def _validate(lon, lat):
        if not (-180 <= lon <= 180):
            raise ValueError(
                f"{lon} is invalid longitude coordinate. Must be between -180 and 180"
            )
        if not (-90 <= lat <= 90):
            raise ValueError(
                f"{lat} is invalid latitude coordinate. Must be between -90 and 90"
            )

    @staticmethod
    def cast_from_hord(value):
        elements = re.findall(r"^(\-?\d+(?:\.\d+)?), \s*(\-?\d+(?:\.\d+)?)$", value)
        lon = float(elements[0][0])
        lat = float(elements[0][1])
        Coordinate._validate(lon, lat)
        return (lon, lat)

    @staticmethod
    def cast_to_hord(value):
        lon, lat = value
        Coordinate._validate(lon, lat)
        return f"{lon}, {lat}"
