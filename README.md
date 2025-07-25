# 風月

尺貫法を扱うためのライブラリ

| Parameters    | type  | description               |
| ---           | ---   | ---                       |
| name          | str   | 単位名                    |
| ratio         | float | SI単位系に対する比率      |
| type          | str   | 単位の種類を区別する一意の値 |
| content       | float | SI単位系で表した時の値 |

## 使用可能メソッド  

| Method        | type  | args      | description                   |
| ---           | ---   | ---       | ---                           |
| value         | float | content   | 値を返す <br> 引数で値を書き換え可能 |
| si            | float | content   | SI単位系に直した時の値を返す<br> 引数にSI単位系で表した時の値を入れることで、値を書き換え可能 |