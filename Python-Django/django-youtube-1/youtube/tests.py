
import sys

from django.test import TestCase

from .ytchannel import YTChannel

class TestParser(TestCase):

    def setUp(self):
        self.simpleFile = 'youtube/testdata/youtube.xml'
        self.zeroFile = 'youtube/testdata/youtube-0.xml'
        self.oneFile = 'youtube/testdata/youtube-1.xml'
        self.expected = [{'link': 'https://www.youtube.com/watch?v=WlqYH7clQ0c',
                     'title': 'Implementación de aplicaciones web: Counter WebApp',
                     'id': 'WlqYH7clQ0c'},
                    {'link': 'https://www.youtube.com/watch?v=FmtWarjh1SQ',
                     'title': 'Implementación de aplicaciones web: Counter Server',
                     'id': 'FmtWarjh1SQ'},
                    {'link': 'https://www.youtube.com/watch?v=6fLZUn5jWjk',
                     'title': 'Arquitectura Modelo-Vista-Controlador',
                     'id': '6fLZUn5jWjk'},
                    {'link': 'https://www.youtube.com/watch?v=nfq8R654D4s',
                     'title': 'Frikiminutos: Proyecto Gutenberg',
                     'id': 'nfq8R654D4s'},
                    {'link': 'https://www.youtube.com/watch?v=Ew37o0oMY80',
                     'title': 'Introducción a Django y "Django calc"',
                     'id': 'Ew37o0oMY80'},
                    {'link': 'https://www.youtube.com/watch?v=IY3dywwiM6g',
                     'title': 'Acceso a los laboratorios docentes de la ETSIT medainte VNCweb y ssh',
                     'id': 'IY3dywwiM6g'}]

    def test_simple(self):
        """Find videos in a simple XML file for a YT channel"""
        xmlFile = open(self.simpleFile, 'r')
        channel = YTChannel(xmlFile)
        videos = channel.videos()
        self.assertEqual(videos, self.expected)

    def test_zero(self):
        """Find videos in a file with no <entry> (only channel data)"""
        xmlFile = open(self.zeroFile, 'r')
        channel = YTChannel(xmlFile)
        videos = channel.videos()
        self.assertEqual(len(videos), 0)

    def test_one(self):
        """Find videos in a file with no <entry> (only channel data)"""
        xmlFile = open(self.oneFile, 'r')
        channel = YTChannel(xmlFile)
        videos = channel.videos()
        self.assertEqual(len(videos), 1)
        self.assertEqual(videos, self.expected[0:1])
