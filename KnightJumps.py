"""
EN
A function that returns the number of points the knight can go if there are no other pieces on a standard chessboard.
The current position of the horse will be given as ("x y").
Input: "(1 1)"
Output: 2 -> Because the horse can go from 1, 1 to 2 different points.
Input: "(4 5)"
Output: 8 -> Because the horse can go from 4, 5 to 8 different points.
"""

"""
TR
Standart bir satranç tahtasında başka hiçbir taş olmamak kaydıyla atın gidebileceği noktaların sayısını veren bir 
fonksiyon. Atın o anki konumu ("x y") şeklinde verilecek. 
Giriş: "(1 1)"
Çıkış: 2 -> Çünkü at 1, 1 noktasından 2 farklı noktaya gidebilir.
Giriş: "(4 5)"
Çıkış: 8 -> Çünkü at 4, 5 noktasından 8 farklı noktaya gidebilir.
"""


def KnightJumps(strParam):
    """ x: left to rigth and y: top to bottom """
    x, y = strParam.replace("(", "").replace(")", "").split(" ")
    return moves[int(x)-1][int(y)-1]


moves = [
    [2, 3, 4, 4, 4, 4, 3, 2],
    [3, 4, 6, 6, 6, 6, 4, 3],
    [4, 6, 8, 8, 8, 8, 6, 4],
    [4, 6, 8, 8, 8, 8, 6, 4],
    [4, 6, 8, 8, 8, 8, 6, 4],
    [4, 6, 8, 8, 8, 8, 6, 4],
    [3, 4, 6, 6, 6, 6, 4, 3],
    [2, 3, 4, 4, 4, 4, 3, 2]
]

m1 = "(1 1)"
m2 = "(1 7)"
m3 = "(3 1)"
m4 = "(3 2)"
m5 = "(3 3)"
m6 = "(6 3)"
m7 = "(7 6)"
m8 = "(8 8)"

print(KnightJumps(m1))      # 2
print(KnightJumps(m2))      # 3
print(KnightJumps(m3))      # 4
print(KnightJumps(m4))      # 6
print(KnightJumps(m5))      # 8
print(KnightJumps(m6))      # 8
print(KnightJumps(m7))      # 6
print(KnightJumps(m8))      # 2
