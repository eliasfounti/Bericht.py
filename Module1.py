import datetime
import random

def bericht():
    infile = open("berichten.csv", "a")
    stations = open("stations.txt", "r")
    lines = stations.readlines()
    stationlijst = [lines[8].replace('\n', ''), lines[29].replace("\n", ""), lines[14].replace("\n", "")]

    station = random.choice(stationlijst)


    naam = input("Wat is uw naam?: ")
    vandaag = datetime.datetime.now()
    datum_tijd = vandaag.strftime("%Y-%d-%m, %H:%M")

    if naam == "":
        naam = "anoniem"
    if naam.isnumeric():
        print("Niet alleen nummers gebruiken voor uw naam!")
    else:
        if len(naam) > 50:
            print("Te lange naam!")
        else:
            print("Welkom bij het station in", station + ",", naam)
            bericht = input("{}, {}".format("Wat is het bericht dat u wilt achterlaten", naam + "?\n"))
            if len(bericht) > 140:
                print("U kan niet meer dan 140 letters gebruiken!")
            else:
                if bericht == "":
                    print("U moet een bericht achterlaten!")
                else:
                    infile.write("{}, {}, {}, {} \n".format(bericht, datum_tijd, naam, station))
                    print("Uw bericht is aangemaakt, fijne dag verder")





bericht()


