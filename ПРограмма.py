def tabl1():
    p = int(input("Введите p (2<p<=10):"))
    x,y = int(1),int(1)

    for x in range (1,p):
       a=[]
       for y in range (1,p):
          z = (x*y//p)*10 + (x*y)% p
          a.append(z)
       print(a)
    






def perevod1():
    a=[]
    st=int(5)
    Itogo=int()
    ss=int(input("Введите показатель системы счисления >>> "))
    x=int(input("Введите число в восьмеричной системе счисления >>> "))
    a=list(str(x))
    print(a)
    for i in range(6):
        (a[i])*(ss**st)
        Itogo=Itogo+(int(a[i]))*(8**st)
        st=st-1
    print(f"Число {x} в восьмеричной системе счисления при переводе в десятичную будет равно {Itogo} ")




def perevod():
    p=int(input("p="))
    Np=int(input(f"N{p}="))
    k=int(1)
    N10=int(0)
    while Np !=0:
        N10+= (Np  %10)*k
        k=k*p
        Np= Np//10
    print(f"N10={N10}")




def morze():
    a = "abwgdevijklmnoprstufhcqx"
    abc = list(a)
    print(abc)
    b = ".- -... .-- --. -.. . ...- --.. .. .--- -.- .-.. -- -. --- .--. .-. ... - ..- ..-. .... -.-. --.- -..-"
    abcm=b.split()
    print(abcm)
    abcm=b.split()
    text=input("Введите текст на английском: ")
    indm=""
    for i in range (len(text)):
        ind = abc.index(text[i])
        indm=indm + abcm[ind] 
    print(f"{indm}строка  в азбуке морзе")


def hem():
    chisla='0123456789'
    chisla_spisok=list(chisla)
    print(chisla_spisok)
    haming='0000000 0001111 0011001 0100101 0101010 0110011 0111100 1000011 1001100'
    haming_spisok=haming.split()
    print(haming_spisok)
    def distance(x,y):
        k=7
        for i in range(0,7):
            if x % 10 == y % 10:
                k = k - 1
            x = x // 10
            y = y // 10
        return k
    cod=int(input("код= "))
    min=distance(cod,int(haming_spisok[0]))
    imin=0
    for i in range(0,9):
        D=distance(cod,int(haming_spisok[i]))
        if D < min:
            min = D
            imin=i
        print(min)
    if min==0:
        print(f"код верный: символ {chisla_spisok[imin]}")
    elif min==1:
        print(f"код исправлен: символ {chisla_spisok[imin]}")
    else:
        print("код неверный")






def func1():
    select = 0
    while select != 5:
        print('Код Хэмминга')
        print('Морзе')
        print('Перевод из n-ой системы счисления в десятичную')
        print('Перевод из десятичной в n-ую.py')
        print('Таблица по системам мчисления')
        select = int(input('Введите номер пункта -'))

        if select == 1:
            hem()
        elif select == 2:
            morze()
        elif select == 3:
            perevod()
        elif select == 4:
            perevod1()
        elif select == 5:
            tabl1()

func1()
