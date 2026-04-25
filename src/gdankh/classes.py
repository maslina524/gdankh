from enumerations import PlayerColor
from utils import chunks

class ColorChannel:
    def __init__(self):
        from_r: int
        from_g: int
        from_b: int
        p_color: PlayerColor
        blending: bool
        color_i: int
        from_opacity: float
        toggle_opacity: bool
        inherited_color_i: int
        hsv: Hsv
        to_r: int
        to_g: int
        to_b: int
        delta_time: float
        to_opacity: float
        duration: float
        copy_opacity: bool

    @classmethod
    def from_string(cls, string: str):
        instance = cls()

        color_chunks = chunks(string.split("_"), 2)
        if len(color_chunks) < 3:
            return instance
            
        for chunk in color_chunks:
            # https://boomlings.dev/resources/client/level-components/color-string#client-color-string-resource
            v = chunk[1]
            match int(chunk[0]): # key
                case 1:
                    instance.from_r = int(v)
                case 2:
                    instance.from_g = int(v)
                case 3:
                    instance.from_b = int(v)
                case 4:
                    instance.p_color = PlayerColor(int(v))
                case 5:
                    instance.blending = (v == '1')
                case 6:
                    instance.color_i = int(v)
                case 7:
                    instance.from_opacity = float(v)
                case 8:
                    instance.toggle_opacity = bool(int(v))
                case 9:
                    instance.inherited_color_i = int(v)
                case 10:
                    instance.hsv = Hsv.from_string(v)
                case 11:
                    instance.to_r = int(v)
                case 12:
                    instance.to_g = int(v)
                case 13:
                    instance.to_b = int(v)
                case 14:
                    instance.delta_time = float(v)
                case 15:
                    instance.to_opacity = float(v)
                case 16:
                    instance.duration = float(v)
                case 17:
                    instance.copy_opacity = bool(int(v))

        return instance
    
    def __str__(self):
        ret = []
        
        if hasattr(self, 'from_r'):
            ret.append(f"1_{self.from_r}")
        if hasattr(self, 'from_g'):
            ret.append(f"2_{self.from_g}")
        if hasattr(self, 'from_b'):
            ret.append(f"3_{self.from_b}")
        
        if hasattr(self, 'p_color'):
            ret.append(f"4_{self.p_color.value}")
        
        if hasattr(self, 'blending'):
            ret.append(f"5_{1 if self.blending else 0}")
        
        if hasattr(self, 'color_i'):
            ret.append(f"6_{self.color_i}")
        
        if hasattr(self, 'from_opacity'):
            ret.append(f"7_{self.from_opacity}")
        
        if hasattr(self, 'toggle_opacity'):
            ret.append(f"8_{int(self.toggle_opacity)}")
        
        if hasattr(self, 'inherited_color_i'):
            ret.append(f"9_{self.inherited_color_i}")
        
        if hasattr(self, 'hsv'):
            ret.append(f"10_{self.hsv}")
        
        if hasattr(self, 'to_r'):
            ret.append(f"11_{self.to_r}")
        if hasattr(self, 'to_g'):
            ret.append(f"12_{self.to_g}")
        if hasattr(self, 'to_b'):
            ret.append(f"13_{self.to_b}")
        
        if hasattr(self, 'delta_time'):
            ret.append(f"14_{self.delta_time}")
        
        if hasattr(self, 'to_opacity'):
            ret.append(f"15_{self.to_opacity}")
        
        if hasattr(self, 'duration'):
            ret.append(f"16_{self.duration}")
        
        if hasattr(self, 'copy_opacity'):
            ret.append(f"17_{int(self.copy_opacity)}")
        
        return "_".join(ret)
    
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