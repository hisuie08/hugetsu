from .common import Length

class Metre(Length):
    name = "m"
    ratio = 1.0


class Ri(Length):
    name="里"
    ratio = 0.0002546


class Cho(Length):
    name="町"
    ratio = 0.0091667


class Ken(Length):
    name="間"
    ratio = 0.55



class Jou(Length):
    name = "丈"
    ratio = 0.33


class Hiro(Length):
    name = "尋"
    ratio = 0.33


class Shaku(Length):
    name="尺"
    ratio = 3.3


class Sun(Length):
    name="寸"
    ratio = 33.0


class LengthBu(Length):
    name="分"
    ratio = 330.0


class Rin(Length):
    name="厘"
    ratio=3300.0


class Mou(Length):
    name="毛"
    ratio=33000.0
