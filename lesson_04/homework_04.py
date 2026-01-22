import re

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
modified_str = adwentures_of_tom_sawer.replace("\n", " ")
# print(modified_str)

# task 02 ==
""" Замініть .... на пробіл
"""
modified_str = modified_str.replace("....", " ")
# print(modified_str)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
text_with_spaces = modified_str
modified_str = " ".join(text_with_spaces.split())
print(modified_str)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = modified_str.count("h")
print(count_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count_capital = 0
for word in modified_str.split():
    if word[0].isupper():
        count_capital += 1

print(count_capital)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
words = modified_str.split()
count_tom = 0
#можливо є простіший спосіб але я не зрозумів як
for index, word in enumerate(words, start=1):
    if word == "Tom":
        count_tom += 1
        if count_tom == 2:
            print(index)
            break

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
#Бляха, 5 разів переписував через те що split(".") створює порожній елемент після останньої крапки
adwentures_of_tom_sawer_sentences = [
    sentence.strip()
    for sentence in modified_str.split(".")
    if sentence.strip()
]

print(len(adwentures_of_tom_sawer_sentences))
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
sentence_four = adwentures_of_tom_sawer_sentences[3]
print(sentence_four.lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
index = modified_str.find("By the time")
if index != -1:
    print(f"Знайдено на позиції {index}.")
else:
    print("Підстрічка не знайдена.")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
sentence_five = adwentures_of_tom_sawer_sentences[4]
sentence_without_signs = re.findall(r'\w+', sentence_five)
print(sentence_without_signs)
print(len(sentence_without_signs))