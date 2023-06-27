#!/bin/sh

# Vorbereiten
rm /home/pi/data/*

# vzlogger abfragen
cd /home/pi/data/
wget http://192.168.1.252:8080/
mv index.html vzlogger.json

# Stecagrid Messdaten abfragen
cd /home/pi/data/
wget http://192.168.1.251/measurements.xml
mv measurements.xml stecagrid.xml

# ESP Powermeter Messdaten abfragen
cd /home/pi/data/
wget http://192.168.1.240/avgDo
mv avgDo esppowermeter.result 
sleep 10
wget http://192.168.1.240/avgFetchPower
mv avgFetchPower esppowermeter.data

# Resol Messdaten abfragen
cd /home/pi/resol
python /home/pi/resol/resol.py > /home/pi/data/resol.json

# -------------------------------------------------

# ggf. daten anderweitig verarbeiten

# -------------------------------------------------

# Content für WebScreen erstellen
python /home/pi/webscreen_top.py > /home/pi/data/content_top.html
python /home/pi/webscreen_bottom.py > /home/pi/data/content_bottom.html
cp content*.html /var/www/volkszaehler.org/htdocs/screen/
