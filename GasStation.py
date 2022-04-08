"""
EN
Take the strArr parameter given to the GasStation function. The structure of strArr is as follows:
"["N", "g:c", "g:c", "g:c", ...]". The first element N is the number of gas stations, g is the amount of gas taken from
the gas station, and c is the amount of gas consumed until it goes to the next gas station. The stations are on a round
route and the vehicle has to stop by all stations. The function should return "impossible" if the vehicle's gas is not
enough to complete the entire route. Otherwise, it should return the smallest starting index it can complete the route.
While calculating the route, it should proceed in order from left to right of strArr.
Examples
Input: ["4", "1:1", "2:2", "1:2", "0:1"]
Output: impossible
Input: ["4", "3:1", "2:2", "1:2", "0:1"]
Output: 1
"""

"""
TR
GasStation fonksiyonuna verilen strArr parametresini alın. strArr'ın yapısı şu şekildedir: "["N", "g:c", "g:c", ...]". 
İlk eleman N gaz istasyonu sayısı, g gaz istasyonundan alınan gaz miktarı, c ise bir sonraki gaz istasyonuna gidene 
kadar harcanan gaz miktarıdır. İstasyonlar yuvarlak bir rotadadır ve araç tüm istasyonlara uğramak zorundadır. Eğer 
aracın gazı tüm rotayı tamamlamaya yetmiyorsa fonksiyon "imkansız" döndürmeli. Aksi taktirde rotayı tamamlayabildiği en 
küçük başlangıç index'ini döndürmeli. Rota hesaplanırken strArr'in solundan sağına doğru sırayla ilerlemelidir. 
Giriş: ["4", "1:1", "2:2", "1:2", "0:1"]
Çıkış: impossible
Giriş: ["4", "3:1", "2:2", "1:2", "0:1"]
Çıkış: 1
"""


def GasStation(strArr):
    n = int(strArr.pop(0))
    for index in range(1, n+1):
        g, c = 0, 0
        for i, gc in enumerate(strArr):
            g2, c2 = map(int, gc.split(":"))
            g += g2
            c += c2
            if g < c:
                break
            if i+1 == n:
                return index

        strArr.append(strArr.pop(0))

    return "impossible"


l1 = ["4", "1:1", "2:2", "1:2", "0:1"]
l2 = ["4", "0:1", "2:2", "1:2", "3:1"]
l3 = ["4", "1:2", "4:3", "3:2", "5:6"]
l4 = ["4", "3:1", "2:2", "1:2", "0:1"]
l5 = ["5", "1:1", "2:2", "1:2", "0:1", "6:3"]
l6 = ["5", "4:1", "2:2", "1:2", "0:1", "6:3"]

print(GasStation(l1))       # impossible
print(GasStation(l2))       # 4
print(GasStation(l3))       # 2
print(GasStation(l4))       # 1
print(GasStation(l5))       # 5
print(GasStation(l6))       # 1
