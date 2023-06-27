# Daten von Resol (Solarthermie) abfragen und webscreen erstellen

import json
import re

# Start
print("<html><body>")
print("<table style='font-family:Arial; font-size:40'>")

# Daten vom vzlogger
with open("/home/pi/data/vzlogger.json") as json_format_file: 
  resoljson = json.load(json_format_file)
  
resoljsonroot = resoljson["data"][0]
value = resoljsonroot["tuples"][0][1]
value = int(value);
if (value > 0):
	print("<tr><td width=250>Bezug &Oslash;:</td><td>");
else:
	print("<tr><td width=250>Liefer.&Oslash;:</td><td>");
print(str(value)+"W");
print("</td/tr>");

# Daten von Stecagrid (Solar PV) - die wird zyklisch geladen
from xml.dom import minidom
xmldoc = minidom.parse('/home/pi/data/stecagrid.xml')
itemlist = xmldoc.getElementsByTagName('Measurement')

value = itemlist[2].attributes['Value'].value
values = value.split('.');
print("<tr><td width=250>Strom S&uuml;d:</td><td>");
print(values[0].replace('-nan','0')+"W");
print("</td/tr>");

f = open("/home/pi/data/esppowermeter.data", "r")
value = f.read()
values = value.split('.');
print("<tr><td width=250>Strom Ost:</td><td>");
print(values[0]+"W");
print("</td/tr>");

print("<tr><td width=250></td><td>");
print("&nbsp;");
print("</td/tr>");

# Daten von Resol (Solarthermie) - die wird zyklisch geladen
with open("/home/pi/data/resol.json") as json_format_file: 
  resoljson = json.load(json_format_file)
  
resoljsonroot = resoljson["DeltaSol BS 2009"]

# Fuehler oben (entities 14 0d1da960-a014-11ea-985e-e9d8eac2fe2e)
value = resoljsonroot["Temperatur Sensor 3"]
value = value.encode('utf8').replace('\xc2', '').replace('\xb0','&deg;');
print("<tr><td width=250>Wasser:</td><td>");
print(value);
print("</td/tr>");

# Fuehler unten (entities 13 1c26b290-97c9-11ea-9c01-11ed7286b899)
value = resoljsonroot["Temperatur Sensor 2"]
value = value.encode('utf8').replace('\xc2', '').replace('\xb0','&deg;');
print("<tr><td></td><td>");
print(value);
print("</td/tr>");

# Kesseltemperatur (entities 15 74e335c0-c94e-11eb-a752-512e21a0807b)
value = resoljsonroot["Temperatur Sensor 4"]
value = value.encode('utf8').replace('\xc2', '').replace('\xb0','&deg;');
print("<tr><td>Kessel:</td><td>");
print(value);
print("</td/tr>");

# Kollektortemperatur (entities 16 2ed03d20-c950-11eb-a986-fd2195d4a96e)
value = resoljsonroot["Temperatur Sensor 1"]
value = value.encode('utf8').replace('\xc2', '').replace('\xb0','&deg;');
print("<tr><td>Kollektor:</td><td>");
print(value);
print("</td/tr>");

# Abschluss
print("</table>")
print("</body></html>")

