"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    while True:
      user_text = input ('Как дела?: ')
      if user_text == 'Хорошо':
        print ('ок. ясно. понятно.')
        break

    
if __name__ == "__main__":
    ask_user()
