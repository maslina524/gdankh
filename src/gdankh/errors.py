class WsConnectFailed(Exception):
    def __init__(self):
        super().__init__("Make sure you are in the editor and the mod is installed.")

class EditorActionOnly(Exception):
    def __init__(self):
        super().__init__("This action is only available in the editor. Please make sure it is open.")

class ServerError(Exception):
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__(f"Server error: {self.msg}")

class UnknownPropID(Exception):
    def __init__(self, id: int):
        self.id = id
        super().__init__(f"Unknown prop id: {self.id}")

class UnknownPropName(Exception):
    def __init__(self, name: str):
        self.name = name
        super().__init__(f"Unknown prop name: {self.name}")