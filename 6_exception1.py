"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    while True:
      try:
        user_text = input ('Как дела?: ')
        if user_text == 'Хорошо':
          print ('ок. ясно. понятно.')
          break
      except(KeyboardInterrupt):
        print ('\nПока!')
        break

    
if __name__ == "__main__":
    ask_user()
