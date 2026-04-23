from typing import Any
from utils import chunks
from props import TYPES, NAME_TO_ID
from errors import UnknownPropID, UnknownPropName
from base64 import b64encode, b64decode

class GameObject:
    def __init__(self):
        self._props = [None] * 600
        self._level_string = ""

    def _value_type_by_id(self, id: int, value: str) -> Any:
        type_name = TYPES.get(str(id))
        if type_name is None:
            raise UnknownPropID(id)
        match type_name:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "bool":
                return value == "1"
            case "b64string":
                return b64decode(str(value).encode()).decode()
            case "grouplist":
                return [int(x) for x in value.split(".")] if value else []
            case _:
                return value

    def _type_to_string(self, id: int, value: Any) -> str:
        type_name = TYPES.get(str(id))
        if type_name is None:
            raise UnknownPropID(id)
        match type_name:
            case "b64string":
                return b64encode(str(value).encode()).decode()
            case "bool":
                return "1" if value else "0"
            case "grouplist":
                return ".".join(str(x) for x in value)
            case _:
                return str(value)

    @classmethod
    def from_string(cls, string: str):
        obj = cls()
        string = string.rstrip(";")
        pairs = chunks(string.split(","), 2)
        for p_id_str, p_value in pairs:
            p_id = int(p_id_str)
            converted = obj._value_type_by_id(p_id, p_value)
            obj.set_prop(p_id, converted)
        return obj

    @classmethod
    def from_kwargs(cls, **kwargs):
        obj = cls()
        for k, v in kwargs.items():
            if k.startswith("_"):
                p_id = int(k.lstrip("_"))
            else:
                p_id = NAME_TO_ID.get(k)
                if p_id is None:
                    raise UnknownPropName(k)
            obj.set_prop(p_id, v)
        return obj

    def get_prop(self, id: int):
        if id < 1 or id > 599:
            raise ValueError("The number is not within the acceptable limits (1-599)")
        return self._props[id]

    def set_prop(self, id: int, value: Any):
        if id < 1 or id > 599:
            raise ValueError("The number is not within the acceptable limits (1-599)")
        self._props[id] = value

    def get_level_string(self) -> str:
        parts = []
        for i in range(1, 600):
            v = self._props[i]
            if v is not None:
                parts.append(str(i))
                parts.append(self._type_to_string(i, v))
        return ",".join(parts) + ";"