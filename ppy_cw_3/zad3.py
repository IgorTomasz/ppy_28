import getpass
import random

assets = ["kamien", "papier", "nożyce"]
win_rounds = []
rounds = input("Podaj ilosc rund: ")
type = input("1. komputer\n2. 2 graczy\n:")

print("Gra się zaczyna!")
if int(type) == 1:
    i = 1
    for i in range(0, int(rounds)):
        player = int(input("1. kamien\n2. papier\n3. nozyce\n: ")) - 1
        rand = int(random.randint(0, 2))
        print("komputer: " + assets[rand])

        if player == rand:
            win_rounds.append(0)
        elif player == 0:
            if rand == 2:
                win_rounds.append(1)
            else:
                win_rounds.append(-1)
        elif player == 1:
            if rand == 0:
                win_rounds.append(1)
            else:
                win_rounds.append(-1)
        elif player == 2:
            if rand == 1:
                win_rounds.append(1)
            else:
                win_rounds.append(-1)

    print(win_rounds)

    points = 0
    for val in win_rounds:
        points += val

    if points > 0:
        print("Wygral gracz!")
    elif points < 0:
        print("Wygral komputer!")
    else:
        print("Remis!")

if int(type) == 2:
    name1 = input("Podaj nazwę pierwszego gracza: ")
    name2 = input("Podaj nazwę drugiego gracza: ")
    i = 1
    for i in range(0, int(rounds)):
        player1 = int(getpass.getpass(name1+" wybiera: \n1. kamien\n2. papier\n3. nozyce\n: ")) - 1
        player2 = int(getpass.getpass(name2+" wybiera: \n1. kamien\n2. papier\n3. nozyce\n: ")) - 1

        print(name1+" wybrał: "+assets[player1]+"\n"+name2+" wybrał: "+assets[player2])

        if player1 == player2:
            win_rounds.append(0)
        elif player1 == 0:
            if player2 == 2:
                win_rounds.append(1)
            else:
                win_rounds.append(-1)
        elif player1 == 1:
            if player2 == 0:
                win_rounds.append(1)
            else:
                win_rounds.append(-1)
        elif player1 == 2:
            if player2 == 1:
                win_rounds.append(1)
            else:
                win_rounds.append(-1)

    print(win_rounds)

    points = 0
    for val in win_rounds:
        points += val

    if points > 0:
        print("Wygral " + name1)
    elif points < 0:
        print("Wygral " + name2)
    else:
        print("Remis!")




