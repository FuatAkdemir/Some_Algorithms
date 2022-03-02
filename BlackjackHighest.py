"""
EN
Have the function BlackjackHighest(strArr) take the strArr parameter being passed which will be an array of numbers and
letters representing blackjack cards. Numbers in the array will be written out. So for example strArr may be
["two","three","ace","king"]. The full list of possibilities for strArr is: two, three, four, five, six, seven, eight,
nine, ten, jack, queen, king, ace. Your program should output below, above, or blackjack signifying if you have
blackjack (numbers add up to 21) or not and the highest card in your hand in relation to whether or not you have
blackjack. If the array contains an ace but your hand will go above 21, you must count the ace as a 1. You must always
try and stay below the 21 mark. So using the array mentioned above, the output should be below king. The ace is counted
as a 1 in this example because if it wasn't you would be above the 21 mark.

Another example would be if strArr was ["four","ten","king"], the output here should be above king. If you have a tie
between a ten and a face card in your hand, return the face card as the "highest card". If you have multiple face cards,
the order of importance is jack, queen, king.

Examples:
Input: ["four", "ace", "ten"]
Output: below ten
Input: ["ace", "queen"]
Output: blackjack ace
"""

"""
TR
BlackjackHighest(strArr) işlevinin, blackjack kartlarını temsil eden bir sayı ve harf dizisi olacak olan strArr 
parametresini almasını sağlayın. Dizideki sayılar yazılacaktır. Örneğin, strArr ["iki", "üç", "as", "kral"] olabilir. 
strArr için olasılıkların tam listesi: iki, üç, dört, beş, altı, yedi, sekiz, dokuz, on, vale, kraliçe, kral, as. 
Programınızın çıktısı aşağıda, yukarıda veya blackjack olup olmadığını (sayıların toplamı 21'e kadar) ve blackjack olup 
olmadığına göre elinizdeki en yüksek kartı belirten bir çıktı vermelidir. Dizi bir as içeriyorsa ancak eliniz 21'in 
üzerine çıkacaksa, ası 1 olarak saymalısınız. Daima 21 işaretinin altında kalmaya çalışmalısınız. Yani yukarıda 
bahsedilen diziyi kullanarak çıktı kralın altında olmalıdır. As, bu örnekte 1 olarak sayılmıştır çünkü olmasaydı, 21 
işaretinin üzerinde olurdunuz.

Başka bir örnek, strArr ["dört", "ten", "kral"] olsaydı, buradaki çıktı kralın üzerinde olmalıdır. Elinizde on ile bir 
yüz kartı arasında bir bağ varsa, yüz kartını "en yüksek kart" olarak iade edin. Birden fazla yüz kartınız varsa, önem 
sırası vale, kraliçe, kraldır.

Örnekler:
Girdi: ["four", "ace", "ten"]
Çıktı: below ten
Girdi: ["ace", "queen"]
Çıktı: blackjack ace
"""


def BlackjackHighest(strArr):
    cardsValues = {1: "ace", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
                   8: "eight", 9: "nine", 10: "ten", 10.01: "jack", 10.02: "queen", 10.03: "king"}

    def get_key(val):
        for k, v in cardsValues.items():
            if val == v:
                return k

    t = 0
    biggest = []
    for i in strArr:
        t += int(get_key(i))
        biggest.append(float(get_key(i)))

    biggest = cardsValues.get(max(biggest))

    if "ace" in strArr and t+10 <= 21:
        t += 10
        biggest = "ace"

    if t == 21:
        return "blackjack " + biggest
    elif t > 21:
        return "above " + biggest
    else:
        return "below " + biggest


l1 = ["four", "ace", "ten"]
l2 = ["ace", "queen"]
l3 = ["ace", "queen", "king"]
l4 = ["queen", "king", "jack"]
l5 = ["queen", "queen", "jack", "five", "five"]
l6 = ["ace", "ace", "ace"]
l7 = ["ace", "nine", "ace"]

print(BlackjackHighest(l1))         # below ten
print(BlackjackHighest(l2))         # blackjack ace
print(BlackjackHighest(l3))         # blackjack king
print(BlackjackHighest(l4))         # above king
print(BlackjackHighest(l5))         # above queen
print(BlackjackHighest(l6))         # below ace
print(BlackjackHighest(l7))         # blackjack ace
