x = True
while x:
    print('===============================================================')
    print('||                                                           ||')
    print('||                       400 of water                        ||')
    print('||                       540 of milk                         ||')
    print('||                       120 of coffee beans                 ||')
    print('||                       9 of disposable                     ||')
    print('||                       550 of money                        ||')
    print('||                                                           ||')
    print('||                       ============                        ||')
    print('||                        press    1                         ||')
    print('||                       =============                       ||')
    print('===============================================================')
    f1 = str(input('function :'))
    while not(f1 in ['1']):
        f1 = str(input('function :'))
    w = 400
    m = 540
    c = 120
    d = 9
    mon = 550
    if f1 == '1':
        print('===============================================================')
        print('||                                                           ||')
        print('||                        1.bay                              ||')
        print('||                        2.fill                             ||')
        print('||                        3.take                             ||')
        print('||                                                           ||')
        print('||                                                           ||')
        print('||                                                           ||')
        print('||                                                           ||')
        print('||                                                           ||')
        print('===============================================================')
    f2 = str(input('select function :'))
    while not(f2 in ['1', '2', '3']):
        f2 = str(input('select function :'))
    if f2 == '1':
        print('===============================================================')
        print('||                                                           ||')
        print('||                        1.espresso                         ||')
        print('||                        2.latte                            ||')
        print('||                        3.cappuccino                       ||')
        print('||                                                           ||')
        print('||                                                           ||')
        print('||                                                           ||')
        print('||                                                           ||')
        print('||                                                           ||')
        print('===============================================================')
    # bay คำนวนหาค่า
        f3 = str(input('select function :'))
        while not(f3 in ['1', '2', '3']):
            f3 = str(input('select function :'))
        if f2 == '1' and f3 == '1':
            t = int(w - 250)
            t1 = (m - 540)
            t2 = int(c - 16)
            t3 = int(d-1)
            t4 = int(mon + 4)
            t5 = ('The ingredient')
        elif f2 == '1' and f3 == '2':
            t = int(w - 350)
            t1 = int(m - 75)
            t2 = int(c - 20)
            t3 = int(d-1)
            t4 = int(mon + 7)
            t5 = ('The ingredient')
        elif f2 == '1' and f3 == '3':
            t = int(w - 200)
            t1 = int(m - 100)
            t2 = int(c - 12)
            t3 = int(d-1)
            t4 = int(mon + 6)
            t5 = ('The ingredient')
    if f2 == '2':
        n = int(input('volume water :'))
        n1 = int(input('volume milk  :'))
        n2 = int(input('volume coffee beans :'))
        n3 = int(input('volume disposable :'))

    if f2 == '2':
        t = (n + 400)
        t1 = (n1 + 540)
        t2 = (n2 + 120)
        t3 = (n3 + 9)
        t4 = (mon)
        t5 = ('The ingredient')
    if f2 == '3':
        t5 = ('I gave you $ 550')
        t = (400)
        t1 = (540)
        t2 = (120)
        t3 = (9)
        t4 = (mon - 550)
    print('===============================================================')
    print(f'||                       {t5}                            ||')
    print(f'||                       {t} of water                        ||')
    print(f'||                       {t1} of milk                         ||')
    print(f'||                       {t2} of coffee beans                  ||')
    print(
        f'||                       {t3} of disposable                      ||')
    print(f'||                       {t4} of money                         ||')
    print('||                                                           ||')
    print('||           ===============================                 ||')
    print('||           press 1 continue || press 0 out                 ||')
    print('||           ===============================                 ||')
    print('===============================================================')
    x = str(input('press  :'))
    while not(x in ['1', '0']):
        x = int(input('press  :'))
    if x == '1':
        x = True
    elif x == '0':
        x = False
