# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import time, random

count = 2021
count_player = 0
count_comp = 0
print('Определяем кто ходит первым...')
time.sleep(2)
player = random.randint(0,1)
if player == 0:
    print('Первй ход за тобой!')
else:
    print('Увы, первым ходит компьютер!')
print()
time.sleep(1)
while count > 0:
    print(f'На столе лежит {count} конфет.')
    if player == 0:
        x = int(input('Сколько конфет возьмешь (1-28)? Ответ: '))
        print()
        count_player += x
        count -= x
        player = 1
    else:
        x = random.randint(1, 28)
        print(f'Оппонент взял {x} конфет.')
        print()
        count_comp += x
        count -= x
        player = 0
    time.sleep(1)
if player == 1:
    print('Поздравляю, ты победил!')
else:
    print('Ты проиграл! Все конфеты достаются оппоненту!')
