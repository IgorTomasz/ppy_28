que = ["Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:",
       "W jakich okolicznościach czytasz książki najczęściej?",
       "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?",
       "Po książki w jakiej formie sięgasz najczęściej?", "Ile książek czytasz średnio w ciągu roku?",
       "Jak często średnio czytasz książki?", "Po jakie gatunki książek sięgasz najczęściej?"]

answ = [
    ["oglądanie telewizji/filmów/seriali", "czytanie książek/czasopism", "słuchanie muzyki",
     "spotkania z rodziną/przyjaciółmi",
     "podróżowanie", "uprawianie sportu"],
    ["podczas podróży", "w czasie wolnym (po pracy, na urlopie)", "podczas pracy/nauki (to ich element)",
     "w ogóle nie czytam"],
    ["chęć poszerzenia wiedzy", "czytanie mnie relaksuje/odpręża", "fakt, że czytanie jest modne",
     "czytanie to moje hobby",
     "konieczność nauki w związku z wykonywaną pracą/studiami", "odczuwam presję rodziny/środowiska, żeby czytać"],
    ["papierowej (tradycyjnej)", "e-booki (książki elektroniczne) na komputerze", "e-booki na tablecie/telefonie",
     "e-booki na specjalnym czytniku (np. Kindle)"],
    ["0", "żadnej w całości - jedynie fragmenty", "1", "2 lub 3", "4-10", "powyżej 10"],
    ["codziennie", "raz w tygodniu", "raz w miesiącu", "raz na kilka miesięcy", "raz na pół roku", "raz na rok",
     "wcale"],
    ["kryminały/thrillery", "romanse", "psychologiczne", "horrory", "naukowe", "dla dzieci i młodzieży", "fantastykę",
     "biograficzne", "historyczne", "science fiction", "podróżnicze", "hobbystyczne (gotowanie, wędkarstwo itp.)",
     "przygodowe", "poezję"]
]

chosed = []

x = 0

name = input("Jak masz na imię i nazwisko? ")

for q in que:
    print(q)
    length = len(answ[x])
    for obj in range(length):
        print(str(obj+1) + " " + answ[x][obj])
    x += 1
    odpowiedz = int(input("wybierz opcje: "))
    chosed.append(odpowiedz-1)
    print()

y = 0
a = 0

print("pytanie: Jak masz na imię i nazwisko?")
print("odpowiedź: "+name)

for q in que:
    print("Pytanie: "+q)
    print("Odpowiedz: "+answ[y][chosed[a]])
    a += 1
    y += 1


