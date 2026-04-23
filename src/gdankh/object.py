from typing import Any
from utils import chunks
from props import TYPES
from errors import UnknownPropID

class GameObject:
    def __init__(self):
        self._props = [None] * 600
        self._level_string = ""

    def _value_type_by_id(self, v: str, i: int) -> Any:
        if i in TYPES:
            match TYPES.get(i):
                case "int":
                    return int(v)
                case "float":
                    return float(v)
                case "bool":
                    return v.lower() in ("true", "1", "yes")
                case _:
                    return v
        else:
            raise UnknownPropID(i)

    @classmethod
    def from_string(cls, string: str):
        obj = cls()
        string = string.rstrip(";")

        obj_chunks = chunks(string.split(","), 2)
        for p_id_str, p_value in obj_chunks:
            p_id = int(p_id_str)
            obj._props[p_id] = obj._value_type_by_id(p_value, p_id_str)
        return obj
    
    def get_level_string(self) -> str:
        parts = []
        for i, v in enumerate(self._props):
            if v != None:
                parts.append(f"{i},{v}")
        
        ret = ",".join(parts) + ";"
        return ret