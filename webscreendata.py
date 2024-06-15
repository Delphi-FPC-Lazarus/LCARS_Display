# Daten aus den vom collectdata.sh zusammengesammelten Daten (verschiedene Formate)
# in einer Tag/Value Liste zur weiteren Verabeitung zusammenstellen

import json
import re

# Systemzeit anzeigen (zum Zeitpunkt der Datenerfassung fest ins html geschrieben)
from datetime import datetime
now = datetime.now()
screentitle = now.strftime("%d.%m.%Y %H:%M")

# Zeitstempel (PV) anzeigen (waere richtiger weil Zeitpunkt der Messung aber Zeitzonen Problematik, irrefuehrend)
#from xml.dom import minidom
#xmldoc = minidom.parse('/home/pi/data/stecagrid.xml')
#itemlist = xmldoc.getElementsByTagName('Device')
#datumzeit = itemlist[0].attributes['DateTime'].value
# Zeitformat von Stecagrid ist "2021-06-16T21:50:59"
#                               YYYY MM DD HH NN
#                               0123 56 89 11 11
#					   12 45
#if (len(datumzeit) != 19):
#	exit();
#if (datumzeit[10] != "T"):
#	exit();
#Y=datumzeit[2:4]
#M=datumzeit[5:7]
#D=datumzeit[8:10]
#H=datumzeit[11:13]
#N=datumzeit[14:16]
# Datum und Zeit im Anzeigeformat
#screentitle = D+"."+M+"."+Y+" "+H+":"+N

print("Title:"+screentitle)

# Daten vom vzlogger (Stromzähler)
try:
	with open("/home/pi/data/vzlogger.json") as json_format_file: 
		vzjson = json.load(json_format_file)  
	vzjsonroot = vzjson["data"][0]
	value = vzjsonroot["tuples"][0][1]
	value = int(value);
	if (value > 0):
		print("Bezug &Oslash;:"+str(value)+"W");
	else:
		print("Liefer.&Oslash;:"+str(value)+"W");
except Exception as e:
	print(f"{e}\n")

# Daten von Stecagrid (Solar PV) - die wird zyklisch geladen
try:
	from xml.dom import minidom
	xmldoc = minidom.parse('/home/pi/data/stecagrid.xml')
	itemlist = xmldoc.getElementsByTagName('Measurement')

	value = itemlist[2].attributes['Value'].value
	values = value.split('.');
	print("Strom S&uuml;d:"+values[0].replace('-nan','0')+"W");
except Exception as e:
	print(f"{e}\n")

# Daten von PV Ost
try:
	with open("/home/pi/data/esppvost.json") as json_format_file: 
		vzjson = json.load(json_format_file)  
	value = str(vzjson["ch"][0][2])
	print("Strom Ost:"+value+"W");
except Exception as e:
	print(f"{e}\n")

# Daten von PV Garage
try:
	f = open("/home/pi/data/esppvgarage.data", "r")
	value = f.read()
	values = value.split('.');
	print("Strom Garage:"+values[0]+"W");
except Exception as e:
	print(f"{e}\n")
	
# Daten vom Akku
try:
	f = open("/home/pi/data/espakku.data", "r")
	value = f.read()
	values = value.split('.');
	f = open("/home/pi/data/espakkustate.data", "r")
	state = f.read()
	if (state == "F"):
		state = "Fehler"
	if (state == "S"):
		state = "Bereit"
	if (state == "C"):
		state = "L&auml;d" 
	if (state == "D"):
		state = "Einsp."
	if (state == "?"):
		state = "??"

	print("Akku: "+state+":"+values[0]+"W");
except Exception as e:
	print(f"{e}\n")

# Daten von Resol (Solarthermie) - die wird zyklisch geladen
try:
	with open("/home/pi/data/resol.json") as json_format_file: 
		resoljson = json.load(json_format_file)
  
	resoljsonroot = resoljson["DeltaSol BS 2009"]

	# Fuehler oben (entities 14 0d1da960-a014-11ea-985e-e9d8eac2fe2e)
	value = resoljsonroot["Temperatur Sensor 3"].replace('\xc2', '').replace('\xb0','&deg;');
	print("Wasser:"+value);

	# Fuehler unten (entities 13 1c26b290-97c9-11ea-9c01-11ed7286b899)
	value = resoljsonroot["Temperatur Sensor 2"].replace('\xc2', '').replace('\xb0','&deg;');
	print("&nbsp;:"+value);

	# Kesseltemperatur (entities 15 74e335c0-c94e-11eb-a752-512e21a0807b)
	value = resoljsonroot["Temperatur Sensor 4"].replace('\xb0','&deg;');
	print("Kessel:"+value);

	# Kollektortemperatur (entities 16 2ed03d20-c950-11eb-a986-fd2195d4a96e)
	value = resoljsonroot["Temperatur Sensor 1"].replace('\xb0','&deg;');
	print("Kollektor:"+value);

except Exception as e:
	print(f"{e}\n")

