"""

Домашнее задание №1

Цикл while: ищем Валеру

* Пройдите по списку пока не встретится имя "Валера".
* Когда найдёте, напишите "Валера нашёлся". Использовать метод list.pop()
    
"""

def search_valera():
  names = ['Вася', 'Петя', 'Вова', 'Валера', 'Саша', 'Нина', 'Наташа']
  while names.pop(0) != 'Валера':
    pass
  print ('Валера нашелся')
    
if __name__ == "__main__":
    search_valera()
