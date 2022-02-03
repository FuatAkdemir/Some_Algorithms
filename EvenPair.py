"""
Verilen string ifade içinde ardışık sayılar içinde 2 tane rakamın çift olması durumunda True dönen program
Örnek: "35rt7gsgeth81egeg22rtrtb" -> 22 ardışık 2 çift sayıdır ve True döndürür.
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


print(EvenPairs("35rt7gsgeth81egeg22rtrtb"))    # T
print(EvenPairs("35rt7gsgeth81egeg2rtrtb"))     # F
print(EvenPairs("35rt7gsgeth81ege212trtb"))     # T
print(EvenPairs("44rt7gsgeth81ege21trtb"))      # T
print(EvenPairs("to34lh741hcbp341ro874"))       # T
print(EvenPairs("39tefq25kl4lw2139"))           # F
