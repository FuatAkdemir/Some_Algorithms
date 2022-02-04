"""
EN
Verilen string ifadesinde ardışık sayılarda 2 sayı çift ise True döndüren program
Örnek: "35rt7gsgeth81egeg44rtrtb" -> 44, ardışık 2 çift sayıdır ve True değerini döndürür.
Örnek: "39tefq25kl4lw2139" -> Ardışık sayılarda 2 çift sayı olmadığından false döndürür.
Örnek: "to34lh741hcbp341ro874" -> 874 ardışık sayı 8 ve 4 çift sayı içerdiğinden True döndürür.
"""

"""
TR
Verilen string ifade içinde ardışık sayılar içinde 2 tane rakamın çift olması durumunda True dönen program
Örnek: "35rt7gsgeth81egeg44rtrtb" -> 44 ardışık 2 çift sayıdır ve True döndürür.
Örnek: "39tefq25kl4lw2139" -> Ardışık sayılar içinde 2 adet çift sayı olmadığı için false döndürür.
Örnek: "to34lh741hcbp341ro874" -> 874 ardışık sayılar içinde 8 ve 4 çift sayılar olduğundan True döndürür.
"""

def EvenPairs(strParam):

    even = False
    prev = False

    for i in strParam:
        if i.isnumeric():
            if int(i) % 2 == 0:
                if prev:
                    return True
                even = True
        else:
            even = False
        prev = even
    return False


print(EvenPairs("35rt7gsgeth81egeg44rtrtb"))    # True
print(EvenPairs("35rt7gsgeth81egeg2rtrtb"))     # False
print(EvenPairs("35rt7gsgeth81ege212trtb"))     # True
print(EvenPairs("44rt7gsgeth81ege21trtb"))      # True
print(EvenPairs("to34lh741hcbp341ro874"))       # True
print(EvenPairs("39tefq25kl4lw2139"))           # False
