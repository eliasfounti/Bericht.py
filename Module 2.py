import psycopg2
import datetime

connection_string = "host='localhost' dbname='Project NS' user='postgres' password='256244zaki'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()
                             # Make the (‘pending’) changes persistent
def modlogin():
    naam_mod = input("Naam van mod: ")
    email_mod = input("Email van mod: ")

    vandaag = datetime.datetime.now()
    datum = vandaag.strftime("%Y/%m/%d")
    tijd = vandaag.strftime("%H:%M:%S")

    lijst_mod = [naam_mod, email_mod, datum, tijd]
    return lijst_mod


lijst_mod = modlogin()

def inlezen(lijst_mod):
    infile = open("berichten.csv", "r")

    berichten = infile.readlines()

    for bericht in berichten:
        #Laat het bericht zien
        print(bericht)
        berichtlijst = bericht.split(",")

        beoordeling = input("Keur je dit bericht goed of fout? U kan ook 'stop' zeggen om te stoppen \n")

        #Stopt de programma
        if beoordeling == "stop":
            break

        if beoordeling == "goed" or beoordeling == "fout":

            if beoordeling == "goed":
                goedgekeurd = True
            if beoordeling == "fout":
                goedgekeurd = False

            query = """INSERT INTO Bericht (Naam, Datum, Tijd, Bericht, Station, Beoordeling)
            VALUES (%s, %s, %s, %s, %s, %s)"""
            query2 = """INSERT INTO Beoordeling (Mod_naam, Mod_email, bd_datum, bd_tijd)
            VALUES (%s, %s, %s, %s)"""
            data = (berichtlijst[3], berichtlijst[1], berichtlijst[2], berichtlijst[0], berichtlijst[4].strip(), goedgekeurd)
            data2 = (lijst_mod[0], lijst_mod[1], lijst_mod[2], lijst_mod[3])
            cursor.execute(query, data) # This transaction is now ‘pending’
            cursor.execute(query2, data2)
            conn.commit()


        #https://stackoverflow.com/questions/4710067/how-to-delete-a-specific-line-in-a-file
        with open("berichten.csv", "r") as f:
            lines = f.readlines()
            line1 = lines[0]
        with open("berichten.csv", "w") as f:
            for line in lines:
                if line != line1:
                    f.write(line)
mod_ww = input("Wat is het wachtwoord? ")
if mod_ww == "elias123":
    print("U bent ingelogd u gaat nu door naar de moderatie")
    inlezen(lijst_mod)
else:
    print("Verkeerd wachtwoord ingevoerd")

conn.close()








