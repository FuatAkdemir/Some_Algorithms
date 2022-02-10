"""
EN
Write a function that flattens a list. Its elements can consist of multi-layered lists (such as [[3], 2]) or non-scalar
data. For example:
input: [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
"""

"""
TR
Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3], 2] gibi) 
oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:
input: [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
"""


def flatten_it(flat_it):
    for lngt, i in enumerate(flat_it):
        if type(i) == int or type(i) == str:
            flatten_list.append(i)
        else:
            flatten_it(i)
    return flatten_list


flatten_list = []
l1 = [1, 5, 75, [30, 2]]
l2 = [1, [2, 3, [4, 5, [6, 7, [8]]]]]
l3 = [26, [34, 98, "python", ["hello", "world"]], "test", "abc"]
l4 = [20, 7, 75, ["xyz", 2], "a", "bcd"]

print(flatten_it(l1))       # [1, 5, 75, 30, 2]
flatten_list.clear()
print(flatten_it(l2))       # [1, 2, 3, 4, 5, 6, 7, 8]
flatten_list.clear()
print(flatten_it(l3))       # [26, 34, 98, 'python', 'hello', 'world', 'test', 'abc']
flatten_list.clear()
print(flatten_it(l4))       # [20, 7, 75, 'xyz', 2, 'a', 'bcd']
flatten_list.clear()

