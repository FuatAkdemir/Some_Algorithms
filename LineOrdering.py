"""
EN
Have the function LineOrdering(strArr) read the strArr parameter being passed which will represent the relations among
people standing in a line. The structure of the input will be ["A>B","B>C","A<D",etc..]. The letters stand for different
people and the greater than and less than signs stand for a person being in front of someone or behind someone. A>B
meansA is in front of B and B<C means that B is behind C in line. For example if strArr is: ["J>B","B<S","D>J"], these
are the following ways you can arrange the people in line: DSJB, SDJB and DJSB. Your program will determine the number
of ways people can be arranged in line. So for this example your program should return the number 3. It also may be the
case that the relations produce an impossible line ordering, resulting in zero as the answer.

Only the symbols <, >, and the uppercase letters A...Z will be used. The maximum number of relations strArr will
contain is ten.

Examples:
Input: ["A>B","A<C","C<Z"]
Output: 1
Input: ["A>B","B<R","R<G"]
Output: 3
"""

"""
TR
LineOrdering(strArr) fonksiyonuyla, bir sırada duran insanlar arasındaki ilişkileri temsil edecek olan iletilen strArr 
parametresini okumasını sağlayın. Girişin yapısı ["A>B","B>C","A<D",vb..] olacaktır. Harfler farklı kişileri, büyüktür 
ve küçüktür işaretleri bir kişinin birinin önünde veya arkasında olduğunu gösterir. A>B, A'nın B'nin önünde olduğu 
anlamına gelir ve B<C, B'nin sırada C'nin arkasında olduğu anlamına gelir. Örneğin, strArr: ["J>B","B<S","D>J"] ise, 
kişileri sıraya koymanın aşağıdaki yolları şunlardır: DSJB, SDJB ve DJSB. Programınız, insanların sıraya dizilebileceği 
yolların sayısını belirleyecektir. Dolayısıyla bu örnek için programınız 3 sayısını döndürmelidir. İlişkilerin imkansız 
bir satır sıralaması üretmesi ve cevap olarak sıfırla sonuçlanması da söz konusu olabilir.

Yalnızca <, > simgeleri ve A...Z büyük harfleri kullanılacaktır. strArr'ın içereceği maksimum ilişki sayısı on'dur. 
Örnekler:
Girdi: ["A>B","A<C","C<Z"]
Çıktı: 1
Girdi: ["A>B","B<R","R<G"]
Çıktı: 3
"""


import re
from itertools import permutations


def LineOrdering(strArr):
    arr = strArr.copy()
    # Create a set which includes all people
    s = set()
    while len(strArr) > 0:
        temp = strArr.pop()
        temp = temp.replace("&#60;", "<")
        a, b = re.split("<|>", temp)
        s.update([a, b])
        # print("s= ", s)

    # Produce all possible lines
    all_lines = permutations(s, len(s))

    # This looks better on screen but a list would work too
    all_lines = ["".join(i) for i in all_lines]

    # Filter all sequences that do not meet the conditions for every given condition
    for temp in arr:
        temp = temp.replace("&#60;", "<")
        a, b = re.split("<|>", temp)

        # "a" must be in front of "b"
        if "<" in temp:
            a, b = b, a

        # Create a new list with the elements that comply with the condition
        all_lines = [seq for seq in all_lines if seq.index(a) < seq.index(b)]
    return len(all_lines)


l1 = ["A>B", "A<C", "C<Z"]    # ZCAB
l2 = ["A>B", "B<R", "R<G"]    # GRAB GARB AGRB

print(LineOrdering(l1))         # 1
print(LineOrdering(l2))         # 3

