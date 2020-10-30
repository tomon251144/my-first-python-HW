x = True
while x   :
        print("===============================================================================")
        print("===============================================================================")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                 select                                    ||")
        print("||                    1.Gasoline 95  price  29.16  BAHT                      ||")
        print("||                    2.Gasoline 95  price  25.30  BAHT                      ||")
        print("||                    3.Gasoline 95  price  21.68  BAHT                      ||")
        print("||                    4.Gasoline 95  price  20.2  BAHT                       ||")
        print("||                    5.Gasoline 95  price  21.2  BAHT                       ||")
        print("||                    6.DIESEL       price   21.1                            ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("===============================================================================")
        print("===============================================================================")
        print("_______________________________________________________________________________")  

        
        mo = input('type: ')
        while not(mo in ['1','2','3','4','5','6']) or mo == '' :
            mo = str(input('type: '))
        print("============")
        print("============")
        
        
        print("===============================================================================")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                 select                                    ||")
        print("||                                                                           ||")
        print("||                           1.แปลงเงินเป็นลิตร                                 ||")
        print("||                           2.แปลงลิตรเป็นเงิน                                 ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("===============================================================================")
        print("===============================================================================")
        print("_______________________________________________________________________________")

        no = input('function :')
        while not(no in ['1','2','']) :
            no = input('Function: ')

        if no == '1' :
            money = float(input("จำนวนเงิน  :"))
        elif no == '2' :
            money1 = float(input("จำนวนลิตร  :"))
        else :
            print('error')


        if no == '1' and mo == '1' :
            #print('จำนวนลิตร',round(money/29.16,2))
            t ='จำนวนลิตร'+(str(round(money/29.16,2)))
        elif no == '1' and mo == '2' :
            #print('จำนวนลิตร',round(money/25.30,2))
            t = 'จำนวนลิตร'+(str(round(money/25.30,2)))
        elif no == '1' and mo == '3' :
            #print('จำนวนลิตร',round(money/21.68,2))
            t = 'จำนวนลิตร'+(str(round(money/21.68,2)))
        elif no == '1' and mo == '4' :
            #print('จำนวนลิตร',round(money/20.2,2))
            t = 'จำนวนลิตร'+(str(round(money/20.2,2)))
        elif no == '1' and mo == '5' :
            #print('จำนวนลิตร',round(money/21.2))
            t = 'จำนวนลิตร'+str(round(money/21.2,2))
        elif no == '1' and mo == '6' :
            t = 'จำนวนลิตร'+str(round(money/21.1,2))
            #print('จำนวนลิตร',round(money/21.1))
        

        elif no == '2' and mo == '1' :
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
        print("===============================================================================")
        print("===============================================================================")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print(f"||                                {t}                              ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                                                                           ||")
        print("||                               ===========                                 ||")
        print("||                               กด 1 เพื่อทำต่อ                                ||")
        print("||                               ===========                                 ||")
        print("||                               ===========                                 ||")
        print("||                               กด 2 เพื่อออก                                 ||")
        print("||                               ===========                                 ||")
        print("||                                                                           ||")
        print("===============================================================================")
        print("===============================================================================")
        x = str(input())
        while not(x in ['1','2']) :
            x = str(input())
        if x != '1' :
            x = False



        
        
       
