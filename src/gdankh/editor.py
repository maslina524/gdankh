import websocket, json
from errors import WsConnectFailed, EditorActionOnly, ServerError
from object import GameObject
from saveload import get_gd_appdata_path
from utils import chunks
from classes import ColorChannel, Hsv

DEFAULT_URI = "ws://localhost:1313"
DEFAULT_PORT = 1313

class Editor:
    def __init__(self):
        self._ws = None
        self.level_string = ""
        self.object_string = ""
        self.color_channels = {}
        self.temp_meta_settings = {}

        self._ret_object_string = ""
        self._ret_color_channels = {}
        self._ret_temp_meta_settings = {}

    def _ws_send(self, json_data) -> str | None:
        self._ws.send(json.dumps(json_data))
        try:
            raw_ret = self._ws.recv()
            if raw_ret == "":
                raise EditorActionOnly
        except:
            raise EditorActionOnly
        
        ret = json.loads(raw_ret)
        if ret.get("status", "error") == "successful":
            return ret.get("response", None)
        else:
            err_msg = ret.get("error", "")
            raise ServerError(err_msg)

    def _get_port(self) -> int:
        path = get_gd_appdata_path() / 'geode' / 'mods' / 'iandyhd3.wsliveeditor' / 'settings.json'
        try:
            with open(path) as f:
                return json.load(f).get('ws-port') or DEFAULT_PORT
        except (FileNotFoundError, json.JSONDecodeError):
            return DEFAULT_PORT

    def _parse_color_string(self, string: str):
        self.color_channels = {}
        colors = string.split('|')
        for color in colors:
            if color == "":
                continue
            color_channel = ColorChannel.from_string(color)
            self.color_channels[color_channel.color_i] = color_channel
                        
    def _parse_level_string(self):
        sep_index = self.level_string.index(';')
        self.object_string = self.level_string[sep_index + 1:]
        start_chunks = chunks(self.level_string[:sep_index].split(","), 2)
        for chunk in start_chunks:
            k = chunk[0]
            v = chunk[1]
            match k:
                case "kS38":
                    self._parse_color_string(v)
                case _:
                    self.temp_meta_settings[k] = v

    @classmethod
    def load_ws(cls):
        instance = cls()
        instance._ws = websocket.WebSocket()
        try:
            instance._ws.connect(f"ws://localhost:{instance._get_port()}", timeout=3)
        except:
            raise WsConnectFailed()

        ret = instance._ws_send({"action": "GET_LEVEL_STRING", "close": False})
        instance.level_string = ret
        instance._parse_level_string()

        instance._ret_object_string = instance.object_string
        instance._ret_color_channels = instance.color_channels
        instance._ret_temp_meta_settings = instance.temp_meta_settings

        return instance
    
    def add_object(self, obj: GameObject):
        if isinstance(obj, GameObject):
            self._object_string += obj.get_string()
        else:
            raise TypeError(f"Expected `GameObject`, got `{type(obj).__name__}`")
        
    def save(self):
        start_parts = []

        # color string
        color_strings = []
        for k, c in list(self._ret_color_channels.items()):
            c.color_i = k
            color_strings.append(f"{c}")
        color_ret = '|'.join(color_strings)
        start_parts.append(f"kS38,{color_ret}|")

        # settings (TEMP)
        for k, v in list(self._ret_temp_meta_settings.items()):
            start_parts.append(f"{k},{v}")
        
        ret = f"{','.join(start_parts)};{self._ret_object_string}"

        print(ret)
        self._ws_send({"action": "REPLACE_LEVEL_STRING", "levelString": ret, "close": True})

if __name__ == "__main__":
    editor = Editor.load_ws()
    editor.color_channels[10] = ColorChannel.from_string("1_10_2_10_3_10_4_-1_6_15_7_1.0_8_1_10_-86a-0.78a0.28a1a1_11_2_12_2_13_2_15_1.0")
    editor.save()