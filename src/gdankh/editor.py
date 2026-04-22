import websocket, json
from errors import WsConnectFailed, EditorActionOnly, ServerError

DEFAULT_URI = "ws://localhost:1313"

class Editor:
    def __init__(self):
        self._ws
        self.level_string
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

    @classmethod
    def load_ws(cls):
        cls._ws = websocket.WebSocket()
        try:
            cls._ws.connect(DEFAULT_URI, timeout=3)
        except:
            raise WsConnectFailed()

        ret = cls._ws_send(cls, {"action": "GET_LEVEL_STRING", "close": False})
        cls.level_string = ret

        cls._parse_level_string()

        return cls
    
    def add_object(self, obj: GameObject):
        if isinstance(obj, GameObject):
            self.objects.append(obj)
        else:
            raise TypeError(f"Expected `GameObject`, got `{type(obj).__name__}`")
    
if __name__ == "__main__":
    editor = Editor.load_ws()
    print(editor.level_string[:2000])