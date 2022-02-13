"""
EN
Function that finds the total minutes in a given time interval in hours.
Example: If "9:00am-10:00am" the output should be 60
Example: If "1:00pm-11:00am" the output should be 1320
"""

"""
TR
Saat cinsinden verilen zaman aralığındaki toplam dakikayı bulan fonksiyon.
Örnek: "9:00am-10:00am" ise çıktı 60 olmalı
Örnek: "1:00pm-11:00am" ise çıktı 1320 olmalı 
"""


def CountingMinutes(time_interval):
    t1, t2 = time_interval.split("-")
    result = ConvertToMinutes(t2) - ConvertToMinutes(t1)
    return result if result > 0 else result + 1440


def ConvertToMinutes(clock):
    """ Code to convert given time into minutes"""
    hours, minutes = map(int, clock[:-2].split(":"))
    if clock.endswith("pm"): hours += 12
    total = hours * 60 + minutes
    return total


# keep this function call here
print(CountingMinutes("10:30am-11:30am"))   # 60
print(CountingMinutes("10:30am-12:30am"))   # 120
print(CountingMinutes("10:30am-12:30pm"))   # 840
print(CountingMinutes("1:00pm-11:00am"))    # 1320
