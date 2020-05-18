"""

Домашнее задание №1

Цикл 

* Создать список из десяти целых чисел.
* Вывести на экран каждое число, увеличенное на 1.
"""
import random
number = []

def main():
    for i in range (10):                      # заполняем список
      number.append(random.randint(0, 200))   # цикл можно описывать как-то сокращенно, не указывая <i>? 
    print (number)                            # выдается warning, что переменная i не используется

    for i in range (10):                      # делаем всем +1
      number[i] += 1
    print (number)

if __name__ == "__main__":
    main()
