# gdankh

Python library for high-level interaction with the Geometry Dash game editor

Are you building difficult levels? Do you want to automate a routine or generate objects using algorithms? With this library, you can easily work with the Geometry Dash editor.

## Usage

```python
from gdankh import Editor, Object

editor = Editor.load_ws()
obj = Object.from_string("1,1,2,15,3,15;")
editor.add_object(obj)
editor.save()
```

Working via WebSocket requires the [WSLiveEditor](https://github.com/iAndyHD3/WSLiveEditor) mod.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/maslina524/gdankh
```

2. Navigate to the project folder:
```bash
cd C:/.../gdankh/
```

3. Install the library
```bash
pip install .
```

## TODO list

- [x] Add object creation via kwargs
- [x] Automatic port detection for WebSocket
- [ ] Changing the level via CCLocalLevels (vanilla)
- [ ] Detailed level string editing
    - [x] Color channel editing
    - [ ] Level meta settings editing
- [ ] Function decorators
    - [ ] `group` decorator
    - [ ] `layer` decorator
    - [ ] `z_layer` decorator
    - [ ] `hsv` decorator
    - [ ] `loop` decorator