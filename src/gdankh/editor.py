import websocket, json
from errors import WsConnectFailed, EditorActionOnly, ServerError
from object import GameObject
from saveload import get_gd_appdata_path

DEFAULT_URI = "ws://localhost:1313"
DEFAULT_PORT = 1313

class Editor:
    def __init__(self):
        self._ws = None
        self.level_string = None
        self.objects = []

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

        # instance._parse_level_string()
        return instance
    
    def add_object(self, obj: GameObject):
        if isinstance(obj, GameObject):
            self.objects.append(obj)
        else:
            raise TypeError(f"Expected `GameObject`, got `{type(obj).__name__}`")
        
    def save(self):
        if len(self.objects) > 0:
            ret = ""
            for obj in self.objects:
                ret += obj.get_level_string()
            self._ws_send({"action": "ADD_OBJECTS", "objects": ret, "close": True})

if __name__ == "__main__":
    # editor = Editor.load_ws()
    obj = GameObject.from_kwargs(id = 1, x = 15, y = 45, _57 = [42, 55, 88])
    print(obj.get_level_string())
    # editor.add_object(obj)
    # editor.save()