import random

moja_lista = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań",
              "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]

rand = int(random.randint(1, len(moja_lista)))

i = 0
for i in range(0, rand):
    city = int(random.randint(1, len(moja_lista)))
    print(moja_lista[city-1])
    moja_lista.remove(moja_lista[city-1])
