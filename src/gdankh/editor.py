import websocket, json

DEFAULT_URI = "ws://localhost:1313"

class Editor:
    def __init__(self):
        self._ws
        self.level_string

    @classmethod
    def load_ws(cls):
        cls._ws = websocket.WebSocket()
        cls._ws.connect(DEFAULT_URI, timeout=3)

        cls._ws.send(json.dumps({"action": "GET_LEVEL_STRING", "close": False}))
        ret = json.loads(cls._ws.recv())
        if ret.get("status", "") == "successful":
            cls.level_string = ret.get("response", "")
    
        return cls
    
if __name__ == "__main__":
    editor = Editor.load_ws()
    print(editor.level_string[:300])