"""
EN
Program that returns True if 2 consecutive numbers are even in the given string expression.
Example: "35rt7gsgeth81egeg44rtrtb" -> 44 is 2 consecutive even numbers and returns True.
Example: "39tefq25kl4lw2139" -> Returns false as there are no 2 even numbers in consecutive numbers.
Example: "to34lh741hcbp341ro874" -> Returns True because 874 consecutive numbers contain 8 and 4 even numbers.
"""

"""
TR
Verilen string ifade içinde ardışık sayılar içinde 2 tane rakamın çift olması durumunda True dönen program.
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
