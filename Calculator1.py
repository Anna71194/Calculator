print('Welcome to the calculator')
first_num=float(input("Enter a number: "))
history = [first_num,]
store = first_num
final = str('')
while True:
    operator=input("Select * + - / or = : ")
    history.append(operator)
    if operator == '=':
        for i in history:
            num=str(i)
            final += ' '
            final += num
        print(final,store) 
        break
    elif operator == '+':
        second_num=float(input("Enter a number: "))
        calculation=store + second_num
        history.append(second_num)
        store =+ calculation
    elif operator == '*':
        second_num=float(input("Enter a number: "))
        history.append(second_num)
        calculation=store * second_num
        store=+ calculation
    elif operator == '-':
        second_num=float(input("Enter a number: "))
        history.append(second_num)
        calculation=store - second_num
        store=+calculation
    elif operator == '/':
        second_num=float(input("Enter a number: "))
        history.append(second_num)
        calculation= store / second_num
        store=+calculation
    else:
        print('Sorry we do not accept that operator, try again')
        continue





