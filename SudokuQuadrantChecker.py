"""
EN
A function that finds whether the given statements on a 9x9 sudoku board are true or false. The input is
["(N,N,N,N,N,x,x,x,x)","(...)"," (...)",...)] where N is An integer from 1 to 9 and x represents an empty cell. It is a
rule of thumb that numbers in each row, column, or 3x3 quadrant do not repeat. If there is a repeating number, you
should print this incorrect cell on the screen. Cell numbers are 1-9, going from left to right and top to bottom. If
there is no error, you should print "legal" on the screen.

Examples:
Sample inputs and outputs below.
"""

"""
TR
9x9'luk bir sudoku bordundaki verilen ifadelerin doğru ya da hatalı olduğunu bulan bir fonksiyon. Girdi 
["(N,N,N,N,N,x,x,x,x)","(...)"," (...)",...)] şeklindedir ve burada N, 1 ile 9 arasında bir tamsayı ve x boş bir hücreyi 
temsil eder. Her bir satırda, sütunda veya 3x3'lük çeyreklerde bulunan rakamların tekrar etmemesi bir sudoku kuralıdır. 
Eğer tekrar eden bir rakam varsa, hatalı olan bu hücreyi ekrana yazdırmalısınız. Hücre numaraları soldan sağa ve 
yukarıdan aşağı gidecek şekilde 1-9 şeklindedir. Eğer bir hata yoksa ekrana "legal" yazdırmalısınız.

Örnekler:
Örnek girdi ve çıktılar aşağıda.
"""

def SudokuQuadrantChecker(strArr):

    # To find the wrong cell
    def findQuad(row, col):
        if row < 3:
            if col < 3: q.add(1)
            elif col < 6: q.add(2)
            elif col < 9: q.add(3)
        elif row < 6:
            if col < 3: q.add(4)
            elif col < 6: q.add(5)
            elif col < 9: q.add(6)
        elif row < 9:
            if col < 3: q.add(7)
            elif col < 6: q.add(8)
            elif col < 9: q.add(9)

    # Searching for errors in rows
    def rowSearch(ar):
        for i, r in enumerate(ar):
            for j, c in enumerate(r):
                if c != "x" and r.count(c) > 1:
                    findQuad(i, j)

    # Searching for errors in columns
    def colSearch(ar):
        for i, c in enumerate(ar):
            for j, r in enumerate(c):
                if r != "x" and c.count(r) > 1:
                    findQuad(j, i)

    # Searching for errors in quadrants
    def quadSearch(ar):
        a = b = 0
        for i in range(9):
            quad = []
            for j in range(b*3, (b+1)*3):
                for k in range(a*3, (a+1)*3):
                    if ar[j][k] != "x":
                        quad.append(ar[j][k])
                        if quad.count(ar[j][k]) > 1:
                            q.add(i+1)
            a += 1
            if a == 3:
                a = 0
                b += 1

    q = set()
    arr = []

    # To clean the entry and make it list
    for s in strArr:
        arr.append(s.lstrip("(").rstrip(")").split(","))

    rowSearch(arr)
    colSearch([*zip(*arr)])
    quadSearch(arr)

    ans = sorted(list(q))
    ans = "".join(str(ans)).replace("[", "").replace("]", "").replace(" ", "")

    return ans if len(ans) != 0 else "legal"


l1 = [
    "(1,2,3,4,5,6,7,8,1)",
    "(x,x,x,x,x,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,x)",
    "(1,x,x,x,x,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,x)"
]
l2 = [
    "(9,2,3,4,5,6,7,8,1)",
    "(x,x,x,x,x,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,x)",
    "(1,x,x,x,x,x,x,x,x)",
    "(x,x,x,x,5,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,x)",
    "(9,x,x,x,x,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,1)"
]
l3 = [
    "(1,2,3,4,5,6,7,8,9)",
    "(x,x,x,x,x,x,x,x,x)",
    "(6,x,5,x,3,x,x,4,x)",
    "(2,x,1,1,x,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,9)"
]
l4 = [
    "(1,2,3,4,5,6,7,8,9)",
    "(x,x,x,x,x,x,x,x,x)",
    "(x,x,9,x,x,x,x,x,x)",
    "(5,x,x,x,x,7,x,x,x)",
    "(x,x,x,x,x,x,x,x,x)",
    "(x,x,x,x,1,x,x,x,x)",
    "(x,x,x,3,x,x,x,x,x)",
    "(x,x,x,x,x,x,x,x,1)",
    "(x,x,4,x,x,x,x,2,x)"
]

print(SudokuQuadrantChecker(l1))        # 1,3,4
print(SudokuQuadrantChecker(l2))        # 1,2,3,5,7,9
print(SudokuQuadrantChecker(l3))        # 3,4,5,9
print(SudokuQuadrantChecker(l4))        # legal

