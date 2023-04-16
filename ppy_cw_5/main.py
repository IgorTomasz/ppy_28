import smtplib
from email.mime.text import MIMEText

def save_to_file(lista, file):
    with open(file, "w") as file_object:
        for x in lista:
            if x.get("status", "no status") == "no status":
                line = x.get("email")+","+x.get("name")+","+x.get("lastName")+","+x.get("points")+"\n"
            else:
                line = x.get("email") + "," + x.get("name") + "," + x.get("lastName") + "," + x.get("points")+","+x.get("status")+"\n"
            file_object.write(line)

def check_email(email):
    for x in users_list:
        if x.get("email") == email:
            return True

def grades():
    for x in users_list:
        if x.get("status", "no status") == "no status":
            points = int(x.get("points", "no points for student"))
            if points < 50:
                x["ocena"] = 2.0
            elif 51 <= points <= 60:
                x["ocena"] = 3.0
            elif 61 <= points <= 70:
                x["ocena"] = 3.5
            elif 71 <= points <= 80:
                x["ocena"] = 4.0
            elif 81 <= points <= 90:
                x["ocena"] = 4.5
            elif 91 <= points <= 100:
                x["ocena"] = 5.0
            x["status"] = "GRADED"
            save_to_file(users_list, filepath)

def menu():
    response = "yes"
    while response != "no":
        email = input("Podaj email nowego studenta: ")
        if check_email(email):
            print("Ten email juz istnieje!")
            menu()
        imie = input("Podaj imie nowego studenta: ")
        nazwisko = input("Podaj nazwisko nowego studenta: ")
        punkty = input("Podaj punkty nowego studenta: ")

        user = {"email": email, "name": imie, "lastName": nazwisko, "points": punkty}
        users_list.append(user)
        save_to_file(users_list, filepath)
        response = input("Czy chcesz oddac kolejnego studenta? (yes/no)")
        grade = input("Czy ocenic dodanych studentow? (yes/no)")
        if grade == "yes":
            grades()

def send_to_all():
    for x in users_list:
        if x.get("status") != "MAILED":
            msg = MIMEText("ocena koncowa: "+x.get("ocena"))
            msg['Subject'] = "oceny koncowe"
            msg['From'] = "prowadzacy@gmail.com"
            msg['To'] = x.get("email")
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.login("mojmail@gmail.com","123123123")
            smtp_server.sendmail("mojmail@gmail.com",x.get("email"),msg.as_string())
            smtp_server.quit()
            x["status"] = "MAILED"

filepath = "students.txt"
users_list = []
with open(filepath) as file_object:
    for line in file_object:
        splitted = line.split(",")
        if len(splitted) == 4:
            user = {"email": splitted[0], "name": splitted[1], "lastName": splitted[2], "points": splitted[3].strip()}
        elif len(splitted) == 5:
            user = {"email": splitted[0], "name": splitted[1], "lastName": splitted[2], "points": splitted[3],
                    "status": splitted[4]}
        users_list.append(user)

print("Students loaded")



print("Students have been graded")

menu()

send_to_all()

for x in users_list:
    for key, val in x.items():
        print(key+": "+str(val))


