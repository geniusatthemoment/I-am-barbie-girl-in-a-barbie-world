a = ['Как на русский переводится слово colazione?',
           'Как на итальянского сказать пожалуйста?',
           'Незнакомец сказал вам grazie. Что он имел в виду?',
           'Говорят ли на итальянском в Швейцарии?',
           'В скольки странах итальянский является официальным языком?']
b = ['Завтрак',
              'Per favore',
              'Cпасибо',
              'Да',
              '6'
    ]
print('Вводите ответ c большой буквы')

def victorina():
    z=0
    for i in range(len(a)):
        print(a[i])
        answer1 = str(input())
        if answer1 == b[i]:
                print('Правильный ответ')
                z = z + 1
        else:
                print('Неправильный ответ')
        
    print(f'Твой результат - {z} правильных ответов')
    print('Хотите пройти викторину ещё раз?')
    answer2 = str(input())
    if answer2 == 'Да':
        victorina()
    else:
        stop



victorina()
            

     


