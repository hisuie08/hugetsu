from .common import Weight

class KiloGram(Weight):
    name = "kg"
    ratio = 1.0

class Kan(Weight):
    name = "貫"
    ratio = 0.26666666666666666

class Ryo(Weight):
    name = "両"
    ratio = 0.02666666666666666

class Monme(Weight):
    name = "匁"
    ratio = 0.00266666666666666

class WeightBu(Weight):
    name = "分"
    ratio = 0.00026666666666666

class WeightRin(Weight):
    name = "厘"
    ratio = 0.00026666666666666

class Kin(Weight):
    name = "斤"
    ratio = 0.006

class Tan(Weight):
    name = "担"
    ratio = 60

