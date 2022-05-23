#!/bin/sh

# Vorbereiten
rm /home/pi/data/*

# Resol Messdaten abfragen
cd /home/pi/resol
python /home/pi/resol/resol.py > /home/pi/data/resol.json

# Stecagrid Messdaten abfragen
cd /home/pi/data/
wget http://192.168.1.251/measurements.xml
mv measurements.xml stecagrid.xml

# -------------------------------------------------

# Content für WebScreen erstellen
python /home/pi/webscreen_top.py > /home/pi/data/content_top.html
python /home/pi/webscreen_bottom.py > /home/pi/data/content_bottom.html
cp content*.html /var/www/volkszaehler.org/htdocs/screen/