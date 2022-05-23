# Daten von Stecagrid (PV) abfragen und Content html erstellen 
# (das ist die Zeit der Messung, nicht die Systemzeit verwenden)

#from datetime import datetime
#now = datetime.now()
#datumzeit = now.strftime("%d.%m.%Y %H:%M")

from xml.dom import minidom
xmldoc = minidom.parse('/home/pi/data/stecagrid.xml')
itemlist = xmldoc.getElementsByTagName('Device')

datumzeit = itemlist[0].attributes['DateTime'].value

# Zeitformat von Stecagrid ist "2021-06-16T21:50:59"
#                               YYYY MM DD HH NN
#                               0123 56 89 11 11
#					   12 45
if (len(datumzeit) != 19):
	exit();
if (datumzeit[10] != "T"):
	exit();

Y=datumzeit[2:4]
M=datumzeit[5:7]
D=datumzeit[8:10]
H=datumzeit[11:13]
N=datumzeit[14:16]

# Datum und Zeit im Anzeigeformat
datumzeit= D+"."+M+"."+Y+" "+H+":"+N

print("<html><body><font size=20>")
print(datumzeit)
print("</font></body></html>")

