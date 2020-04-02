#!/usr/bin/python3

#
# Simple XML parser for JokesXML
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# SARO and SAT subjects (Universidad Rey Juan Carlos)
# 2009-2020
#
# Just prints the jokes in a JokesXML file

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string

class CounterHandler(ContentHandler):

    def __init__ (self):
        self.inContent = False
        self.theContent = ""

    def startElement (self, name, attrs):
        if name == 'joke':
            self.title = attrs.get('title')
            print(" Title: " + self.title + ".")
        elif name == 'start':
            self.inContent = True
        elif name == 'end':
            self.inContent = True
            
    def endElement (self, name):
        if name == 'joke':
            print()
        elif name == 'start':
            print("  Start: " + self.theContent + ".")
        elif name == 'end':
            print ("  End: " + self.theContent + ".")
        if self.inContent:
            self.inContent = False
            self.theContent = ""
        
    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars
            
# --- Main prog
if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Usage: python xml-parser-jokes.py <document>")
        print()
        print(" <document>: file name of the document to parse")
        sys.exit(1)
    
    # Load parser and driver
    JokeParser = make_parser()
    JokeHandler = CounterHandler()
    JokeParser.setContentHandler(JokeHandler)

    # Ready, set, go!
    xmlFile = open(sys.argv[1],"r")
    JokeParser.parse(xmlFile)

    print("Parse complete")
