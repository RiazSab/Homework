print('Введите предложение:')
text = str(input())

words = text.split()
count_word = len(words)

print("Слов в предложении: " + str(count_word))

# Задание 2: посчитать буквы
count_letter = 0
for i in text:
    if i != ' ' and i != ',' and i != '.' and i != '!' and i != '?':
        # Если это не пробел и не знак препинания, то это буква
        count_letter = count_letter + 1

print("Букв в предложении: " + str(count_letter))

# Задание 3: найти самое длинное слово
if count_word == 0:
    print("Самое длинное слово: слов нет")
else:
    # Сначала беру первое слово как самое длинное
    max = words[0]
    
    # Потом проверяю все остальные слова
    for this in words:
        if len(this) > len(max):
            max = this
    
    print("Самое длинное слово: " + max)

