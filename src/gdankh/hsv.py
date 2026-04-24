from dataclasses import dataclass

class Hsv:
    def __init__(self):
        self.h: float
        self.s: float
        self.v: float
        self.s_checked: bool
        self.v_checked: bool

    @classmethod
    def from_string(cls, string: str):
        instance = cls()
        parts = string.split("a")
        instance.h = int(parts[0])
        instance.s = float(parts[1])
        instance.v = float(parts[2])
        instance.s_checked = bool(int(parts[3]))
        instance.v_checked = bool(int(parts[4]))
        return instance

    @classmethod
    def from_rgb(cls, r: float, g: float, b: float):
        instance = cls()
        r_norm = r / 255.0
        g_norm = g / 255.0
        b_norm = b / 255.0
        
        max_val = max(r_norm, g_norm, b_norm)
        min_val = min(r_norm, g_norm, b_norm)
        delta = max_val - min_val
        
        if delta == 0:
            h = 0
        elif max_val == r_norm:
            h = 60 * (((g_norm - b_norm) / delta) % 6)
        elif max_val == g_norm:
            h = 60 * (((b_norm - r_norm) / delta) + 2)
        else:
            h = 60 * (((r_norm - g_norm) / delta) + 4)
        
        if max_val == 0:
            s = 0
        else:
            s = (delta / max_val) * 100
        
        v = max_val * 100
        
        instance.h = h
        instance.s = s / 360
        instance.v = v / 255
        instance.s_checked = False
        instance.v_checked = False

        return instance
    
    def __str__(self):
        return f"{self.h:.0f}a{self.s:.2f}a{self.v:.2f}a{int(self.s_checked)}a{int(self.v_checked)}"