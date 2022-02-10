"""
EN
Write a function that reverses the elements inside the given list. If the elements inside the list also contain the
list, reverse their elements as well. For example:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[7, 6, 5], [4, 3], [2, 1]]
"""

"""
TR
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste 
içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[7, 6, 5], [4, 3], [2, 1]]
"""


def reverse_list(rev):
    rev.reverse()
    for i in rev:
        if type(i) == list:
            reverse_list(i)
    return rev


l1 = [[1, 2], [3, 4], [5, 6, 7]]
l2 = [["a", "b"], ["cde", "fgh"], [75, 34, "python"]]
l3 = [["a", ["b", "c"]], ["123", 123, [456, 789]]]
l4 = ["a", "x", ["b", "c"], ["123", 123, [456, 789, [10, 11, 12, [13, 14]]]]]

print(reverse_list(l1))         # [[7, 6, 5], [4, 3], [2, 1]]
print(reverse_list(l2))         # [['python', 34, 75], ['fgh', 'cde'], ['b', 'a']]
print(reverse_list(l3))         # [[[789, 456], 123, '123'], [['c', 'b'], 'a']]
print(reverse_list(l4))         # [[[[[14, 13], 12, 11, 10], 789, 456], 123, '123'], ['c', 'b'], 'x', 'a']

