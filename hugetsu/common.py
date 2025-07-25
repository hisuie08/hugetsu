class Unit():
    """
単位型クラス  
| Parameters    | type  | description               |
| ---           | ---   | ---                       |
| name          | str   | 単位名                    |
| ratio         | float | SI単位系に対する比率      |
| type          | str   | 単位の種類を区別する一意の値 |
| content       | float | SI単位系で表した時の値 |

使用可能メソッド  
| Method        | type  | args      | description                   |
| ---           | ---   | ---       | ---                           |
| value         | float | content   | 値を返す <br> 引数で値を書き換え可能 |
| si            | float | content   | SI単位系に直した時の値を返す<br> 引数にSI単位系で表した時の値を入れることで、値を書き換え可能 |
    """

    name: str
    ratio: float
    type: str

    def __init__(self, content = 0):
        self.value(content)
    
    def __str__(self):
        return f"{self.value()} {self.name}"
    
    def si(self, content = None):
        if content is not None:
            self.content = content
        return self.content
    
    def value(self, content = None):
        if content is not None:
            self.content = content / self.ratio
        return self.content * self.ratio
    
    def type_check(self, other):
        return self.type == other.type

    def __add__(self, other):
        if self.type_check(other):
            return type(self)((self.si() + other.si()) * self.ratio)
        else:
            raise TypeError("異なる種類の単位の加算は出来ません")
        
    def __sub__(self, other):
        if self.type_check(other):
            return type(self)((self.si() - other.si()) * self.ratio)
        else:
            raise TypeError("異なる種類の単位の減算は出来ません")
        
    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return type(self)((self.si() * other) * self.ratio)
        elif self.type_check(other):
            return type(self)((self.si() * other.si()) * self.ratio)
        else:
            raise TypeError("異なる種類の単位の乗算は出来ません")
        
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return type(self)((other * self.si()) * self.ratio)
        else:
            raise TypeError("異なる種類の単位の乗算は出来ません")
        
    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            return type(self)((self.si() / other) * self.ratio)
        elif self.type_check(other):
            return type(self)((self.si() / other.si()) * self.ratio)
        else:
            raise TypeError("異なる種類の単位の除算は出来ません")
    
    def __floordiv__(self, other):
        if isinstance(other, (float, int)):
            return type(self)(int((self.si() / other) * self.ratio))
        elif self.type_check(other):
            return type(self)(int((self.si() / other.si()) * self.ratio))
        else:
            raise TypeError("異なる種類の単位の除算は出来ません")
    
    def __eq__(self, other):
        if self.type_check(other):
            return self.si() == other.si()
        else:
            raise TypeError("異なる種類の単位の比較は出来ません")
    
    def __lt__(self, other):
        if self.type_check(other):
            return self.si() < other.si()
        else:
            raise TypeError("異なる種類の単位の比較は出来ません")
    
    def __gt__(self, other):
        if self.type_check(other):
            return self.si() > other.si()
        else:
            raise TypeError("異なる種類の単位の比較は出来ません")


class Length(Unit):
    name    = "m"
    ratio   = 1.0
    type    = "length"

    def __init__(self, content = 0) -> "Length":
        super().__init__(content)

class Weight(Unit):
    name    = "kg"
    ratio   = 1.0
    type    = "weight"

    def __init__(self, content = 0) -> "Weight":
        super().__init__(content)
