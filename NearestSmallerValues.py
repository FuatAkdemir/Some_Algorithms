"""
EN
NearestSmallerValue(arr) take the array of integers stored in arr, and for each element in the list,
search all the previous values for the nearest element that is smaller than (or equal to) the current element and
create new list from this number. If there is no element before a certain position that is smaller,
input a -1.
Examples:
Input: [5, 2, 8, 3, 9, 12]
Output: -1, -1, 2, 2, 3, 9
Input: [5, 3, 1, 9, 7, 3, 4, 1]
Output: -1, -1, -1, 1, 1, 1, 3, 1
Input: [2, 4, 5, 1, 7]
Output: -1, 2, 4, -1, 1
"""

"""
TR
NearestSmallerValue(arr), arr'da depolanan tamsayı dizisini alır ve listedeki her öğe için, mevcut öğeden daha küçük 
olan en yakın öğe için önceki tüm değerleri arar ve bu sayıdan yeni bir liste oluşturur. Belirli bir konumdan önce 
daha küçük bir öğe yoksa, -1 girin.
Örnek:
Girdi: [5, 2, 8, 3, 9, 12]
Çıktı: -1, -1, 2, 2, 3, 9
Girdi: [5, 3, 1, 9, 7, 3, 4, 1]
Çıktı: -1, -1, -1, 1, 1, 1, 3, 1
Girdi: [2, 4, 5, 1, 7]
Çıktı: -1, 2, 4, -1, 1
"""


def NearestSmallerValues(arr):
    # code goes here
    lst = [-1]
    for i in range(len(arr) - 1):
        n1 = arr[i]
        n2 = arr[i + 1]
        if n1 >= n2:
            n3 = [s for s in lst[::-1] if s <= n2]
            lst.append(max(n3))
        else:
            lst.append(n1)

    return " ".join(str(elem) for elem in lst)


l1 = [5, 3, 1, 9, 7, 3, 4, 1]
l2 = [2, 4, 5, 1, 7]
l3 = [5, 2, 8, 3, 9, 12]

print(NearestSmallerValues(l1))         # -1 -1 -1 1 1 1 3 1
print(NearestSmallerValues(l2))         # -1 2 4 -1 1
print(NearestSmallerValues(l3))         # -1 -1 2 2 3 9

