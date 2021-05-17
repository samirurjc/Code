#!/usr/bin/python3

#
# Simple title extractor a HTML document, given its url
# Simple example of use of BeautifulSoup4
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# SARO and SAT subjects (Universidad Rey Juan Carlos)
# 2021
#
# Before running this program, install BeautifulSoup4,
# likely in a virtual environment. For example:
# pip install beautifulsoup4
#
# Example:
# python3 html-title.py https://python.org

import sys
import urllib.request
from bs4 import BeautifulSoup

# --- Main prog
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python html-title.py <url>")
        print()
        print(" <url>: url of HTML document")
        sys.exit(1)

    url = sys.argv[1]
    htmlStream = urllib.request.urlopen(url)
    soup = BeautifulSoup(htmlStream, 'html.parser')
    # Get Title from title element
    print("Title:", soup.title.string)
    # Get meta property='og:title'
    ogTitle = soup.find('meta', property='og:title')
    if ogTitle:
        print("Title (og:title):", ogTitle['content'])
    # Get meta property='og:image'
    ogImage = soup.find('meta', property='og:image')
    if ogImage:
        print("Image (og:image):", ogImage['content'])