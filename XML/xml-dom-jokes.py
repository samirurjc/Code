#!/usr/bin/python3

# Simple DOM XML parser for JokesXML
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# SARO and SAT subjects (Universidad Rey Juan Carlos)
# 2022
#
# Just prints the jokes in a JokesXML file

from xml.dom.minidom import parse

with open("jokes.xml") as file:
    document = parse('jokes.xml')
    jokes = document.getElementsByTagName('joke')
    for joke in jokes:
        title = joke.getAttribute('title')
        starts = joke.getElementsByTagName('start')
        ends = joke.getElementsByTagName('end')
        print(f"Title: {title}.")
        print(f" Start: {starts[0].firstChild.nodeValue}.")
        for end in ends:
            print(f" End: {end.firstChild.nodeValue}")
