#list called history to remember past numbers and operators add first number as first list number
history = []
#store variable to keep a running amount in case of multiple calculatons (ex. 1 + 1 + 2)
store = 0
#final var is for printing out the list contents and converting to string
final = str('')
#create first number var
cont = True
#first number function to collect first number
def f_number():
    #calling global variables
    global store,history
    while True:
        #try function to ensure a float/int is being entered and not a string
        try:  
            first_num=float(input("Enter a number: "))
            #store the number for recalling
            store = first_num
            #add the first number to the history list for recolection
            history.append(first_num)
        #except if the input entered by user is not a number reject and error and have them try again
        except ValueError:
            print('That doesnt seem to be a valid number, try again')
            continue
        #break cycle if no value error is triggered
        else:
            break
    return first_num
#operarion call function to gather operator user wants to use
def ops():
    #choose operator and then commit that operator to history list for remembering past operators, calling global history
    global history
    operator=input("Select * + - / or = : ")
    return operator
#second calculation for calling second number and then deciding what to do with the calculation based on operation user chose
def s_calc():  
        #calling global variables   
        global store,final,history,cont   
        operator=ops()
        if operator == '=':
            cont = False
            history.append(operator)
            #if operator equals + add the first number to the second number add the second number to the history list for remembering
            for i in history:
                num=str(i)
                final += ' '
                final += num
            #if operator equals = then iterate over the history list and add the history contents to a string called final and print the final 
            print(final,store) 
            #break because user indicated a completion to calculation
        elif operator == '+':
            history.append(operator)
            while True:
                #try function to ensure no string is being entered as a number
                try:
                    second_num=float(input("Enter a number: "))
                #if valuerror triggers, a value is entered that is not what is expeted it will error and ask to try again
                except ValueError:
                    print('That doesnt seem to be a valid number, try again')
                    continue
                #break cycle if no value error is triggered
                else:
                    break
            calculation= store + second_num
            history.append(second_num)
            store =+ calculation
            s_calc()
        #if operator equals * multiply the first number to the second number add the second number to the history list for remembering
        elif operator == '*':
            history.append(operator)
            while True:
                #try function to ensure no string is being entered as a number
                try:
                    second_num=float(input("Enter a number: "))
                #if valuerror triggers, a value is entered that is not what is expeted it will error and ask to try again
                except ValueError:
                    print('That doesnt seem to be a valid number, try again')
                    continue
                #break cycle if no value error is triggered
                else:
                    break
            history.append(second_num)
            calculation=store * second_num
            store=+ calculation
            s_calc()
        #if operator equals - subtract the first number to the second number add the second number to the history list for remembering
        elif operator == '-':
            history.append(operator)
            while True:
                #try function to ensure no string is being entered as a number
                try:
                    second_num=float(input("Enter a number: "))
                #if valuerror triggers, a value is entered that is not what is expeted it will error and ask to try again
                except ValueError:
                    print('That doesnt seem to be a valid number, try again')
                    continue
                #break cycle if no value error is triggered
                else:
                    break
            history.append(second_num)
            calculation=store - second_num
            store=+calculation
            s_calc()
        #if operator equals / divide the first number to the second number add the second number to the history list for remembering
        elif operator == '/':
            history.append(operator)
            while True:
                #try function to ensure no string is being entered as a number
                try:
                    second_num=float(input("Enter a number: "))
                #if valuerror triggers, a value is entered that is not what is expeted it will error and ask to try again
                except ValueError:
                    print('That doesnt seem to be a valid number, try again')
                    continue
                #break cycle if no value error is triggered
                else:
                    break
            history.append(second_num)
            calculation= store / second_num
            store=+calculation
            s_calc()
        # if the operator equals nothing in the above if elif statement then print this error and try again
        else:
            print('Sorry we do not accept that operator, try again')
            s_calc()
#main function for intro and calculator loop
def main():
    #calling global varaibles for use
    global cont,history,store,final
    #print welcome
    print('Welcome to the calculator')
    #call first function for collection of number
    f_number()
    #while loop for indication of if user is done with the first iteration of calulation
    while cont:
        s_calc()
    #once = is chosen by user cont = false and we ask if they want to do another iteration of calculations
    if cont == False:
        while True:
            another=input('Do you want to do another calculation? Y/N: ')
            #turning answer to upper just in case of lower case answer
            answer=another.upper()
            #ensuring we only collect Y or N, if not then error occurs and they can try again
            if answer == 'Y' or answer == 'N':
                break
            else:
                print(answer)
                print("Sorry please enter Y or N, try again")     
    #if user wants another calculation clear history list clear store and final string for use in new calculation storage
    if answer == 'Y':
        history.clear()
        store = 0
        final = str('')
        cont = True
        #start over with main
        main()
    #if no then end loop
    elif answer == 'N':
        print('Thank you!')
main()






