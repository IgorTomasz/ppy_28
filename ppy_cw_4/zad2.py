def prime(*liczba):
    for val in liczba:
        ifPrime = True
        if val == 1 or val == 0:
            print(str(val) + " is not prime")
        else:
            half = val // 2
            for i in range(2, half + 1):
                if val % i == 0:
                    ifPrime = False
            if ifPrime:
                print(str(val) + " is prime number")
            else:
                print(str(val) + " is not prime")


prime(0, 1, 2, 3, 4, 5)
