#!/usr/bin/python3

#
# Simple JSON importer for municipios.json
#   municipios.json obtained from
#   https://opendata.aemet.es/opendata/api/maestro/municipios/?api_key=XXX
# This version retrieves the JSON file from
#   https://raw.githubusercontent.com/CursosWeb/Code/master/Python-JSON/municipios.json
#
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# April 2019
#
# Just prints some of the data in the file

import json
import urllib.request

url = 'https://raw.githubusercontent.com/CursosWeb/Code/master/Python-JSON/municipios.json'

with urllib.request.urlopen(url) as json_doc:
    json_str = json_doc.read().decode(encoding="ISO-8859-1")
    munis = json.loads(json_str)

for muni in munis:
    print("Name: " + muni['nombre'], ", Id: ", muni['url'])
