# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

x = input('Введите строку: ')
rez = ''
count = 1
for i in range(1, len(x)):
    if x[i] == x[i-1]:
        count += 1
    else:
        rez += str(count) + x[i-1]
        count = 1
rez += str(count) + x[len(x)-1]
print(rez)
