"""
EN
Program that checks if the given number is prime. It prints "true" if the number is prime, "false" otherwise.
Examples:
Input: 19
Output: true
Input: 110
Output: false
"""

"""
TR
Verilen sayının asal olup olmadığını kontrol eden program. Sayı asalsa "true", değilse "false" yazdırılır. 
Örnekler:
Girdi: 19
Çıktı: true
Girdi: 110
Çıktı: false
"""


def PrimeTime(num):
    if num < 2:
        return "false"
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return "false"
    return "true"


print(PrimeTime(1))         # false
print(PrimeTime(2))         # true
print(PrimeTime(7))         # true
print(PrimeTime(75))        # false
print(PrimeTime(110))       # false
print(PrimeTime(0))         # false
print(PrimeTime(-5))        # false

