print("Введи свои оценки за неделю через пробел:")

ocenki = input()
ocenki_list = ocenki.split()

chisla =[]
for o in ocenki_list:
    chisla.append(int(o))

sum = sum(chisla)
kol = len(chisla)
avr = sum / kol

pyaterki = 0
for x in chisla:
    if x == 5:
        pyaterki += 1

print ("твои оценки: ", chisla)
print ("средний бал ", avr)
print ("Пятерки: ", pyaterki)


if avr == 5:
    print("отличник")
if avr >= 4 and avr < 5:
    print("хорошист")
if avr <= 3.9:
    print("Нужно подтянусься")