"""

Домашнее задание №1

Цикл while: ищем имя

* Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке
    
"""

def find_person(name):
  names = ['Вася', 'Петя', 'Вова', 'Валера', 'Саша', 'Нина', 'Наташа']
  while names.pop(0) != str(name):
    pass
  print (f'{name} нашелся')
    
if __name__ == "__main__":
    find_person('Саша')
