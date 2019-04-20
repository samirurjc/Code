#!/usr/bin/python3

#
# Simple JSON importer for municipios.json
#   municipios.json obtained from
#   https://opendata.aemet.es/opendata/api/maestro/municipios/?api_key=XXX
#
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# April 2019
#
# Just prints some of the data in the file

import json
import sys


if len(sys.argv)<2:
    print("Usage: python json-municipios.py <document>")
    print()
    print(" <document>: file name of the document to read")
    sys.exit(1)

with open(sys.argv[1], 'r', encoding = "ISO-8859-1") as json_file:
    munis = json.load(json_file)

for muni in munis:
    print("Name: " + muni['nombre'], ", Id: ", muni['url'])
