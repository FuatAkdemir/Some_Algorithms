"""
EN
This program splits the elements in a given array into pairs of 2. If the inverse of the corresponding pair is found,
it deletes both from the array. Returns "yes" if there are no elements left in the array when all iterations are
complete. Otherwise, it prints the remaining array elements in integer format and with commas between them.
Example: Input: [2,1,1,2,30,30]   ->  Output: 30,30
Example: Input: [5,4,6,7,7,6,4,5] ->  Output: "yes"
Example: Input: [2, 1, 35, 53]    ->  Output: 2, 1, 35, 53
"""

"""
TR
Bu program verilen bir dizideki elemanları 2'li çiftlere böler. Eğer ilgili çifte karşılık gelen çiftin tersi bulunursa 
ikisini de diziden siler. Bütün iterasyon bittiğinde dizide eleman kalmazsa "evet" döndürür. Aksi taktirde kalan dizi 
elemanlarını integer formatında ve aralarında virgül olarak yazdırır. 
Örnek: Giriş: [2,1,1,2,30,30]   ->  Sonuç: 30,30
Örnek: Giriş: [5,4,6,7,7,6,4,5] ->  Sonuç: "yes"
Örnek: Giriş: [2, 1, 35, 53]    ->  Sonuç: 2, 1, 35, 53
"""

from itertools import chain


def arraycouples(arr):
    result = []
    while len(arr) > 0:
        temp = arr[:2]
        arr = arr[2:]
        if temp[::-1] in result:
            result.remove(temp[::-1])
        else:
            result.append(temp)

    result = ",".join(map(str, chain.from_iterable(result)))
    return "yes" if len(result) == 0 else result


# keep this function call here

l0 = [2, 1, 1, 2, 3, 5, 5, 3]       # yes
l1 = [2, 1, 1, 2, 30, 50]           # 30, 50
l2 = [2, 1, 1, 2, 35, 53]           # 35, 53
l3 = [5, 4, 6, 7, 7, 6, 4, 5]       # yes
l4 = [7, 5, 6, 75, 75, 3, 0, 6]     # 7, 5, 6, 75, 75, 3, 0, 6

print(arraycouples(l0))
print(arraycouples(l1))
print(arraycouples(l2))
print(arraycouples(l3))
print(arraycouples(l4))
