#!/usr/bin/python3

#
# Simple XML parser for YouTube XML channels given a channel id
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# SARO and SAT subjects (Universidad Rey Juan Carlos)
# 2020
#
# Produces a HTML document in standard output, with
# the list of videos on the channel
#
# Example:
# yt-channel.py UC300utwSVAYOoRLEqmsprfg

import sys
import urllib

import ytparser

# --- Main prog
if __name__ == "__main__":

    PAGE = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <h1>Channel contents:</h1>
    <ul>
{videos}
    </ul>
  </body>
</html>
"""

    if len(sys.argv) < 2:
        print("Usage: python xml-parser-youtube.py <channel_id>")
        print()
        print(" <document>: id of the YouTube channel to parse")
        sys.exit(1)

    # Ready, set, go!
    url = 'https://www.youtube.com/feeds/videos.xml?channel_id=' \
        + sys.argv[1]
    xmlStream = urllib.request.urlopen(url)

    ytparser.Parser.parse(xmlStream)
    page = PAGE.format(videos=ytparser.videos)
    print(page)

