print('Welcome to United Bank for Africa ATM')
restart = ('Y')
chances = 3
balance = 67.14
while chances >= 0:
    pin = int(input('Please Enter Your 4 Digit Pin:'))
    if pin == (1234):
        print('You entered your pin correctly\n')
        while restart not in ('n','NO','no','N'):
            print('Please Press 1 For Your Balance\n')
            print('Please press 2 To Make a Withdrawal\n')
            print('Please press 3 To Pay in\n')
            print('Please Press 4 To Return Card\n')
            option = int(input('What would you like to choose?'))
            if option == 1:
                print('Your Balance is N', balance,'\n')
                restart =  input('Would You like to go back? ')
                if restart  in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawal = float(input('How Much would you like to withdraw?\n N10/N20/N40/N60/N80/N100'))
                if withdrawal in [10,20,40,60,80,100]:
                    balance = balance - withdrawal
                    print('\nYour Balance is now N', balance)
                    restart = input('Would You like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawal != [10,20,40,60,80,100]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawal == 1:
                    withdrawal = float(input('Please Enter Desired amount'))

            elif option  == 3:
                pay_in = float(input('How Much Would You Like to pay In? '))
                balance = balance + pay_in
                print('\nYour Balance is now N' ,balance)
                restart = input('Would You like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please wait whilst your card is Returned...\n')
                print('Thank you for your service')
                break
            else:
                print('Please Enter a correct number.\n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            

