def zvuk():
    select = 0
    while select !=4:
        print('1 Размер аудиофайла')
        print('2 Частота')
        print('3 Время звучания')
        print('4 Разрядность регистра')
        select = int(input('выберите, ту велечину, которую нужно найти - '))

        if select == 1:
            print('Введите частоту - ')
            a = int(input())
            print('Введите время звучания - ')
            b = int(input())
            print('Введите разрядность регистра - ')
            с = int(input())
            d = a * b * c / 8
            print('Размер аудиофайла - ')
        elif select == 2:
            print('Введите размер аудиофайла - ')
            a = int(input())
            print('Введите время звучания - ')
            b = int(input())
            print('Введите разрядность регистра - ')
            с = int(input())
            d = 8*a/b*c
            print('Частота - ')
        elif select == 3:
            print('Введите размер аудиофайла - ')
            a = int(input())
            print('Введите частота - ')
            b = int(input())
            print('Введите разрядность регистра - ')
            с = int(input())
            d = 8 * a / b * c
            print('Частота - ')
        elif select == 4:
            print('Введите размер аудиофайла - ')
            a = int(input())
            print('Введите частота - ')
            b = int(input())
            print('Введите время звучания - ')
            с = int(input())
            d = 8 * a /  b* c
            print('Разрядность регистра - ')


def vibor():
    select = 0
    while select != 4:
        print('1 Байты')
        print('2 Биты')
        print('3 Килобайты')
        print('4 Килобиты')
        select = int(input('выберите, ту велечину, в которой представлена информация - '))

        if select == 1:
            print('Введите число - ')
            a = int(input());
            print('Ответ', int(a), 'символов')
        elif select == 2:
            print('Введите число - ')
            a = int(input());
            b = a / 8
            print('Ответ', int(b), 'символов')
        elif select == 3:
            print('Введите число - ')
            a = int(input());
            b = a * 1024
            print('Ответ', int(b), 'символов')
        elif select == 4:
            print('Введите число - ')
            a = int(input());
            b = a * 1024
            c = b / 8
            print('Ответ', int(c), 'символов')


def menu1():
    select = 0
    while select != 3:
        print('0 Назад в главное')
        print('1 Обьем информации')
        print('2 Количество символов')
        select = int(input('выберите, что нужно найти -'))

        if select == 0:
            func()
        elif select == 1:
            print('Введите количество символов')
            a = int(input())
            b = a * 8
            print('Ответ', int(b), 'битов')
        elif select == 2:
            vibor()


def func():
    select = 0
    while select != 4:
        print('1 Кодирование информации')
        print('2 Кодирование звука')
        print('3 Кодирование изображения')
        select = int(input('Введите номер пункта -'))

        if select == 1:
            menu1()
        elif select == 2:
            zvuk()


func()

