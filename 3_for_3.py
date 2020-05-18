"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
import random


def main():

  book = []

  for grade in range (1,12):                   #заполняю журнал классами от 1 до 11
    if grade !=4:                              #в моём детстве 4 класса не было
      for letter in 'abcd':                    #буква класса, допустим их 4
        class_name = str(grade)+letter         #определяю название класса
        scores = []                            #создаю пустой список для оценок, иначе ругается
        scholar_number = random.randint(6, 15) #случайное количество учеников в классе
        for n in range (1,scholar_number):     #Придумываю рандомную оценку каждому ученику     
          scores.append(random.randint(1, 5))
        book.append({'school_class': class_name, 'scores': scores})
  
  print(f'{book}\n')
  sum_all = 0                                      #Считаю средний балл по школе
  counter_all = 0

  for b in range (len(book)):
    counter_class = 0
    sum_class = 0
    for s in range (len(book[b]['scores'])):
      sum_all += book[b]['scores'][s]
      sum_class += book[b]['scores'][s]
      counter_all += 1
      counter_class += 1
    avg_class = round(sum_class/counter_class,1)
    book[b]['avg_score'] = avg_class

  print(f'{book}\n')
  avg_all = round(sum_all/counter_all,1)
  print (f'Средний балл по школе: {avg_all}')   

  
if __name__ == "__main__":
    main()
