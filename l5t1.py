# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('l5t1-1.txt', 'r', encoding='utf-8') as data:
    first_text = data.readlines()[0]

with open('l5t1-2.txt', 'w', encoding='utf-8') as data:
    data.write(first_text.replace('абв', ''))