firstNum = input("Podaj pierwsza liczbe: ")
secondNum = input("Podaj druga liczbe: ")
operation = input("Podaj operator operacji ktora chcesz wykonac: ")

first = float(firstNum)
sec = float(secondNum)

if operation == '+':
    print(first + sec)
elif operation == '-':
    print(first - sec)
elif operation == '*':
    print(first * sec)
elif operation == '/':
    print(first / sec)
