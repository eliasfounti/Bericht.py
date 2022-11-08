from tkinter import *
from PIL import Image, ImageTk
import psycopg2
import requests


connection_string = "host='localhost' dbname='Project NS' user='postgres' password='256244zaki'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()
cursor2 = conn.cursor()
cursor3 = conn.cursor()
# Hier selecteer ik Bericht van het tabel bericht en in volgorde van berichtid maar van het hoogste berichtid naar laagste.
# Gaat zo door tot het 5 heeft
bericht = """SELECT Bericht FROM bericht order by berichtid desc limit 5"""
naam = """SELECT naam FROM bericht order by berichtid desc limit 5"""
station = """SELECT station FROM bericht order by berichtid desc limit 5"""

#Haalt alle informatie van de 5 tabellen van bericht
bericht = cursor.execute(bericht)
bericht = cursor.fetchall()
#Hetzelfde maar dan bij naam
naam = cursor2.execute(naam)
naam = cursor2.fetchall()
#Hetzelfde maar dan bij station
station = cursor3.execute(station)
station = cursor3.fetchall()


def faciliteiten():
    conn.cursor()
    stationlijst = []
    #Selecteert station_city en doet het in een lijst.
    for i in station:
        query = """SELECT * FROM station_service WHERE station_city = %s"""
        data = (i)
        cursor.execute(query, data)
        stationfaciliteiten = cursor.fetchall()
        stationlijst.append(stationfaciliteiten)
    return stationlijst

#Voert de frame uit.
def GUI():
    NaamBerichtFrame.pack()


root = Tk()

#Was vergeten variabel naam te veranderen nadat ik het af had dus heb het zo gelaten.
NaamBerichtFrame = Frame(master=root, background="Gold")
NaamBerichtFrame.pack(fill="both", expand=True)

#Kopjes labels voor later
NAMEN = Label(master=NaamBerichtFrame, text="Naam", font=("Arial", 30), background="Gold")
Bericht = Label(master=NaamBerichtFrame, text="Bericht", font=("Arial", 30), background="Gold")
Station = Label(master=NaamBerichtFrame, text="Station", font=("Arial", 30), background="Gold")
Faciliteitenlabel = Label(master=NaamBerichtFrame, text="Faciliteit", font=("Arial", 30), background="Gold")
Weer = Label(master=NaamBerichtFrame, text="Temperatuur", font=("Arial", 30), background="Gold")
#Bericht labels voor later
bericht1 = Label(master=NaamBerichtFrame, text=bericht[0], font=("Arial", 20), background="Gold")
bericht2 = Label(master=NaamBerichtFrame, text=bericht[1], font=("Arial", 20), background="Gold")
bericht3 = Label(master=NaamBerichtFrame, text=bericht[2], font=("Arial", 20), background="Gold")
bericht4 = Label(master=NaamBerichtFrame, text=bericht[3], font=("Arial", 20), background="Gold")
bericht5 = Label(master=NaamBerichtFrame, text=bericht[4], font=("Arial", 20), background="Gold")
#Naam labels voor later
naam1 = Label(master=NaamBerichtFrame, text=naam[0], font=("Arial", 20), background="Gold")
naam2 = Label(master=NaamBerichtFrame, text=naam[1], font=("Arial", 20), background="Gold")
naam3 = Label(master=NaamBerichtFrame, text=naam[2], font=("Arial", 20), background="Gold")
naam4 = Label(master=NaamBerichtFrame, text=naam[3], font=("Arial", 20), background="Gold")
naam5 = Label(master=NaamBerichtFrame, text=naam[4], font=("Arial", 20), background="Gold")
#Station labels voor later
station1 = Label(master=NaamBerichtFrame, text=station[0], font=("Arial", 20), background="Gold")
station2 = Label(master=NaamBerichtFrame, text=station[1], font=("Arial", 20), background="Gold")
station3 = Label(master=NaamBerichtFrame, text=station[2], font=("Arial", 20), background="Gold")
station4 = Label(master=NaamBerichtFrame, text=station[3], font=("Arial", 20), background="Gold")
station5 = Label(master=NaamBerichtFrame, text=station[4], font=("Arial", 20), background="Gold")

faciliteit = faciliteiten()

#Hier voeg ik de faciliteiten op plaats.
Faciliteitenlabel.grid(row=0, column=53)
if faciliteit[0][0][2] == True:
    ovfiets = Label(master=NaamBerichtFrame, text='OvFiets✔', background="Gold", font=("Arial", 18))
    ovfiets.grid(row=3, column=53)
else:
    ovfietsnee = Label(master=NaamBerichtFrame, text='OvFiets❌', background="Gold", font=("Arial", 18))
    ovfietsnee.grid(row=3, column=53)
if faciliteit[0][0][3] == True:
    lift = Label(master=NaamBerichtFrame, text='Lift✔', background="Gold", font=("Arial", 18))
    lift.grid(row=3, column=54)
else:
    liftnee = Label(master=NaamBerichtFrame, text='Lift❌', background="Gold", font=("Arial", 18))
    liftnee.grid(row=3, column=54)
if faciliteit[0][0][4] == True:
    toilet = Label(master=NaamBerichtFrame, text='Toilet✔', background="Gold", font=("Arial", 18))
    toilet.grid(row=3, column=55)
else:
    toiletnee = Label(master=NaamBerichtFrame, text='Toilet❌', background="Gold", font=("Arial", 18))
    toiletnee.grid(row=3, column=55)
if faciliteit[0][0][5] == True:
    pr = Label(master=NaamBerichtFrame, text='P+R✔', background="Gold", font=("Arial", 18))
    pr.grid(row=3, column=56)
else:
    prnee = Label(master=NaamBerichtFrame, text='P+R❌', background="Gold", font=("Arial", 18))
    prnee.grid(row=3, column=56)


if faciliteit[1][0][2] == True:
    ovfiets = Label(master=NaamBerichtFrame, text='OvFiets✔', background="Gold", font=("Arial", 18))
    ovfiets.grid(row=6, column=53)
else:
    ovfietsnee = Label(master=NaamBerichtFrame, text='OvFiets❌', background="Gold", font=("Arial", 18))
    ovfietsnee.grid(row=6, column=53)
if faciliteit[1][0][3] == True:
    lift = Label(master=NaamBerichtFrame, text='Lift✔', background="Gold", font=("Arial", 18))
    lift.grid(row=6, column=54)
else:
    liftnee = Label(master=NaamBerichtFrame, text='Lift❌', background="Gold", font=("Arial", 18))
    liftnee.grid(row=6, column=54)
if faciliteit[1][0][4] == True:
    toilet = Label(master=NaamBerichtFrame, text='Toilet✔', background="Gold", font=("Arial", 18))
    toilet.grid(row=6, column=55)
else:
    toiletnee = Label(master=NaamBerichtFrame, text='Toilet❌', background="Gold", font=("Arial", 18))
    toiletnee.grid(row=6, column=55)
if faciliteit[1][0][5] == True:
    pr = Label(master=NaamBerichtFrame, text='P+R✔', background="Gold", font=("Arial", 18))
    pr.grid(row=6, column=56)
else:
    prnee = Label(master=NaamBerichtFrame, text='P+R❌', background="Gold", font=("Arial", 18))
    prnee.grid(row=6, column=56)

if faciliteit[2][0][2] == True:
    ovfiets = Label(master=NaamBerichtFrame, text='OvFiets✔', background="Gold", font=("Arial", 18))
    ovfiets.grid(row=9, column=53)
else:
    ovfietsnee = Label(master=NaamBerichtFrame, text='OvFiets❌', background="Gold", font=("Arial", 18))
    ovfietsnee.grid(row=9, column=53)
if faciliteit[2][0][3] == True:
    lift = Label(master=NaamBerichtFrame, text='Lift✔', background="Gold", font=("Arial", 18))
    lift.grid(row=9, column=54)
else:
    liftnee = Label(master=NaamBerichtFrame, text='Lift❌', background="Gold", font=("Arial", 18))
    liftnee.grid(row=9, column=54)
if faciliteit[2][0][4] == True:
    toilet = Label(master=NaamBerichtFrame, text='Toilet✔', background="Gold", font=("Arial", 18))
    toilet.grid(row=9, column=55)
else:
    toiletnee = Label(master=NaamBerichtFrame, text='Toilet❌', background="Gold", font=("Arial", 18))
    toiletnee.grid(row=9, column=55)
if faciliteit[2][0][5] == True:
    pr = Label(master=NaamBerichtFrame, text='P+R✔', background="Gold", font=("Arial", 18))
    pr.grid(row=9, column=56)
else:
    prnee = Label(master=NaamBerichtFrame, text='P+R❌', background="Gold", font=("Arial", 18))
    prnee.grid(row=9, column=56)

if faciliteit[3][0][2] == True:
    ovfiets = Label(master=NaamBerichtFrame, text='OvFiets✔', background="Gold", font=("Arial", 18))
    ovfiets.grid(row=12, column=53)
else:
    ovfietsnee = Label(master=NaamBerichtFrame, text='OvFiets❌', background="Gold", font=("Arial", 18))
    ovfietsnee.grid(row=12, column=53)
if faciliteit[3][0][3] == True:
    lift = Label(master=NaamBerichtFrame, text='Lift✔', background="Gold", font=("Arial", 18))
    lift.grid(row=12, column=54)
else:
    liftnee = Label(master=NaamBerichtFrame, text='Lift❌', background="Gold", font=("Arial", 18))
    liftnee.grid(row=12, column=54)
if faciliteit[3][0][4] == True:
    toilet = Label(master=NaamBerichtFrame, text='Toilet✔', background="Gold", font=("Arial", 18))
    toilet.grid(row=12, column=55)
else:
    toiletnee = Label(master=NaamBerichtFrame, text='Toilet❌', background="Gold", font=("Arial", 18))
    toiletnee.grid(row=12, column=55)
if faciliteit[3][0][5] == True:
    pr = Label(master=NaamBerichtFrame, text='P+R✔', background="Gold", font=("Arial", 18))
    pr.grid(row=12, column=56)
else:
    prnee = Label(master=NaamBerichtFrame, text='P+R❌', background="Gold", font=("Arial", 18))
    prnee.grid(row=12, column=56)

if faciliteit[4][0][2] == True:
    ovfiets = Label(master=NaamBerichtFrame, text='OvFiets✔', background="Gold", font=("Arial", 18))
    ovfiets.grid(row=15, column=53)
else:
    ovfietsnee = Label(master=NaamBerichtFrame, text='OvFiets❌', background="Gold", font=("Arial", 18))
    ovfietsnee.grid(row=15, column=53)
if faciliteit[4][0][3] == True:
    lift = Label(master=NaamBerichtFrame, text='Lift✔', background="Gold", font=("Arial", 18))
    lift.grid(row=15, column=54)
else:
    liftnee = Label(master=NaamBerichtFrame, text='Lift❌', background="Gold", font=("Arial", 18))
    liftnee.grid(row=15, column=54)
if faciliteit[4][0][4] == True:
    toilet = Label(master=NaamBerichtFrame, text='Toilet✔', background="Gold", font=("Arial", 18))
    toilet.grid(row=15, column=55)
else:
    toiletnee = Label(master=NaamBerichtFrame, text='Toilet❌', background="Gold", font=("Arial", 18))
    toiletnee.grid(row=15, column=55)
if faciliteit[4][0][5] == True:
    pr = Label(master=NaamBerichtFrame, text='P+R✔', background="Gold", font=("Arial", 18))
    pr.grid(row=15, column=56)
else:
    prnee = Label(master=NaamBerichtFrame, text='P+R❌', background="Gold", font=("Arial", 18))
    prnee.grid(row=15, column=56)

#Hidde heeft hiermee geholpen
resource_uri = "https://api.openweathermap.org/data/2.5/weather"

#1e station api
station1api = {'APPID': '51796bd546343ee5647b321e20e74e58', 'q': station[0], 'units':'imperial'}
station1response = requests.get(resource_uri, station1api)
station1response_data = station1response.json()
lijst = []
for key in station1response_data.keys():
    #voegt het in de lijst
    lijst.append(f"{key}:{station1response_data[key]}")
#Split ik zodat ik het kan kiezen.
weerinfosplit = lijst[1].split(': ')
#Kiest temp in lijst en split het
temperatuurstring = lijst[3].split(': ')
temperatuurlijst = []
#Voegt het in de tabellen lijst
temperatuurlijst.append(temperatuurstring[2].split(', '))
#Kiest de graden
Fgraden = float(temperatuurlijst[0][0])
#Maakt het graden celsius
temperatuur = (Fgraden - 32) / 1.8
#Rond het af.
tempstation1 = round(temperatuur, 1)

#2e station api
station2api = {'APPID': '51796bd546343ee5647b321e20e74e58', 'q': station[1], 'units':'imperial'}
station2response = requests.get(resource_uri, station2api)
station2response_data = station2response.json()
lijst = []
for key in station2response_data.keys():
    lijst.append(f"{key}:{station2response_data[key]}")
weerinfosplit = lijst[1].split(': ')
temperatuurstring = lijst[3].split(': ')
temperatuurlijst = []
temperatuurlijst.append(temperatuurstring[2].split(', '))
Fgraden = float(temperatuurlijst[0][0])
temperatuur = (Fgraden - 32) / 1.8
tempstation2 = round(temperatuur, 1)

#3e station api
station3api = {'APPID': '51796bd546343ee5647b321e20e74e58', 'q': station[2], 'units':'imperial'}
station3response = requests.get(resource_uri, station3api)
station3response_data = station3response.json()
lijst = []
for key in station3response_data.keys():
    lijst.append(f"{key}:{station3response_data[key]}")
weerinfosplit = lijst[1].split(': ')
temperatuurstring = lijst[3].split(': ')
temperatuurlijst = []
temperatuurlijst.append(temperatuurstring[2].split(', '))
Fgraden = float(temperatuurlijst[0][0])
temperatuur = (Fgraden - 32) / 1.8
tempstation3 = round(temperatuur, 1)

#4e station api
station4api = {'APPID': '51796bd546343ee5647b321e20e74e58', 'q': station[3], 'units':'imperial'}
station4response = requests.get(resource_uri, station4api)
station4response_data = station4response.json()
lijst = []
for key in station4response_data.keys():
    lijst.append(f"{key}:{station4response_data[key]}")
weerinfosplit = lijst[1].split(': ')
temperatuurstring = lijst[3].split(': ')
temperatuurlijst = []
temperatuurlijst.append(temperatuurstring[2].split(', '))
Fgraden = float(temperatuurlijst[0][0])
temperatuur = (Fgraden - 32) / 1.8
tempstation4 = round(temperatuur, 1)

#5e station api
station5api = {'APPID': '51796bd546343ee5647b321e20e74e58', 'q': station[4], 'units':'imperial'}
station5response = requests.get(resource_uri, station5api)
station5response_data = station5response.json()
lijst = []
for key in station5response_data.keys():
    lijst.append(f"{key}:{station4response_data[key]}")
weerinfosplit = lijst[1].split(': ')
temperatuurstring = lijst[3].split(': ')
temperatuurlijst = []
temperatuurlijst.append(temperatuurstring[2].split(', '))
Fgraden = float(temperatuurlijst[0][0])
temperatuur = (Fgraden - 32) / 1.8
tempstation5 = round(temperatuur, 1)

#Labels voor temperatuur
weer1 = Label(master=NaamBerichtFrame, text=tempstation1, font=("Arial", 20), background="Gold")
weer2 = Label(master=NaamBerichtFrame, text=tempstation2, font=("Arial", 20), background="Gold")
weer3 = Label(master=NaamBerichtFrame, text=tempstation3, font=("Arial", 20), background="Gold")
weer4 = Label(master=NaamBerichtFrame, text=tempstation4, font=("Arial", 20), background="Gold")
weer5 = Label(master=NaamBerichtFrame, text=tempstation5, font=("Arial", 20), background="Gold")

#Weer grid
Weer.grid(row=0, column=100)
weer1.grid(row=3, column=100)
weer2.grid(row=6, column=100)
weer3.grid(row=9, column=100)
weer4.grid(row=12, column=100)
weer5.grid(row=15, column=100)
#Namen grid
NAMEN.grid(row=0, column=1)
naam1.grid(row=3, column=1)
naam2.grid(row=6, column=1)
naam3.grid(row=9, column=1)
naam4.grid(row=12, column=1)
naam5.grid(row=15, column=1)
#Bericht grid
Bericht.grid(row=0, column=18)
bericht1.grid(row=3, column=18)
bericht2.grid(row=6, column=18)
bericht3.grid(row=9, column=18)
bericht4.grid(row=12, column=18)
bericht5.grid(row=15, column=18)
#Station grids
Station.grid(row=0, column=35)
station1.grid(row=3, column=35)
station2.grid(row=6, column=35)
station3.grid(row=9, column=35)
station4.grid(row=12, column=35)
station5.grid(row=15, column=35)

root.mainloop()