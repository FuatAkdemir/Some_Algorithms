"""
EN
Program that returns "yes" if the given number is in the Fibonacci sequence, and "no" if it is not.
Input: 34
Output: yes
Input: 54
Output: no
"""

"""
TR
Verilen sayı Fibonacci serisinde yer almaktaysa "evet", yer almıyorsa "hayır" döndüren program.
Girdi: 34
Çıktı: yes
Girdi: 54
Çıktı: no
"""


def fibonacciChecker(num):
    if num == 0 or num == 1:
        return "yes"
    a, b = 0, 1
    while a+b <= num:
        if a+b == num:
            return "yes"
        a, b = b, a+b
    return "no"


print(fibonacciChecker(34))         # yes
print(fibonacciChecker(2))          # yes
print(fibonacciChecker(5))          # yes
print(fibonacciChecker(75))         # no
print(fibonacciChecker(7))          # no

