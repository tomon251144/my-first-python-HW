def com000() :
        t0 = ("===============================================================================")
        print(t0)
        t00 = ("||                                                                           ||")
        print(t00)
        print("||                                 select                                    ||")
        print(t00)
        print("||                           1.แปลงเงินเป็นลิตร                                 ||")
        print("||                           2.แปลงลิตรเป็นเงิน                                 ||")
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t0)
        print(t0)
        z1 = ("_______________________________________________________________________________")
        print(z1)

def com1(mo,no) :
    money = float(input("จำนวนเงิน  :"))
    if no == '1' and mo == '1' :
        t ='จำนวนลิตร'+(str(round(money/29.16,2)))
    elif no == '1' and mo == '2' :
        t = 'จำนวนลิตร'+(str(round(money/25.30,2)))
    elif no == '1' and mo == '3' :
        t = 'จำนวนลิตร'+(str(round(money/21.68,2)))
    elif no == '1' and mo == '4' :
        t = 'จำนวนลิตร'+(str(round(money/20.2,2)))
    elif no == '1' and mo == '5' :
        t = 'จำนวนลิตร'+str(round(money/21.2,2))
    elif no == '1' and mo == '6' :
        t = 'จำนวนลิตร'+str(round(money/21.1,2))
    
    return t
def com2(mo,no) :
    money1 = float(input("จำนวนลิตร  :"))
    if no == '2' and mo == '1' :
            #print('จำนวนลิตร',round(money/29.16,2))
            t ='จำนวนลิตร'+(str(round(money1*29.16,2)))
    elif no == '2' and mo == '2' :
            #print('จำนวนลิตร',round(money/25.30,2))
            t = 'จำนวนลิตร'+(str(round(money1*25.30,2)))
    elif no == '2' and mo == '3' :
            #print('จำนวนลิตร',round(money/21.68,2))
            t = 'จำนวนลิตร'+(str(round(money1*21.68,2)))
    elif no == '2' and mo == '4' :
            #print('จำนวนลิตร',round(money/20.2,2))
            t = 'จำนวนลิตร'+(str(round(money1*20.2,2)))
    elif no == '2' and mo == '5' :
            #print('จำนวนลิตร',round(money/21.2))
            t = 'จำนวนลิตร'+str(round(money1*21.2,2))
    elif no == '2' and mo == '6' :
            t = 'จำนวนลิตร'+str(round(money1*21.1,2))
            #print('จำนวนลิตร',round(money/21.1))
    return t
def com3(x) :
    if x != 1 :
        x = False
x = True
while x   :
        
        print(t0)
        print(t0)
        print(t00)
        print(t00)
        print("||                                 select                                    ||")
        print("||                    1.Gasoline 95  price  29.16  BAHT                      ||")
        print("||                    2.Gasoline 95  price  25.30  BAHT                      ||")
        print("||                    3.Gasoline 95  price  21.68  BAHT                      ||")
        print("||                    4.Gasoline 95  price  20.2  BAHT                       ||")
        print("||                    5.Gasoline 95  price  21.2  BAHT                       ||")
        print("||                    6.DIESEL       price   21.1                            ||")
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t0)
        print(t0)
        print(z1)
        mo = input('type: ')
        while not(mo in '123456') or mo == '' :
            mo = str(input('type: '))
        com000()
        no = input('function :')
        while not(no in ['1','2']) :
            no = input('Function: ')
       
        if no == '1' :
           t = com1(mo,no)
        elif no == '2' :
           t = com2(mo,no)
        print(t0)
        print(t0)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(f"||                                {t}                              ||")
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print(t00)
        print("||                               กด 1 เพื่อทำต่อ                                 ||")
        print("||                               ===========                                 ||")
        print("||                               ===========                                 ||")
        print("||                               กด 2 เพื่อออก                                 ||")
        print(t00)
        print(t00)
        print(t0)
        print(t0)
        x = input()
        com3(x)
	
	
