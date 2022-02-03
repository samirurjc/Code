#!/usr/bin/python3

"""Solución del ejercicio "Descarga de documentos web" """

import urllib.request

class Robot:

    def __init__(self, url):
        self.url = url
        self.retrieved = False
        print(self.url)

    def retrieve(self):
        if not self.retrieved:
            print("Descargando...")
            f = urllib.request.urlopen(self.url)
            self.content = f.read().decode('utf-8')
            self.retrieved = True

    def content(self):
        self.retrieve()
        return self.content

    def show(self):
        print(self.content())

class Cache:

    def __init__(self):
        self.cache = {}

    def retrieve(self, url):
        if url not in self.cache:
            robot = Robot(url = url)
            self.cache[url] = robot

    def content(self, url):
        self.retrieve(url)
        return self.cache[url].content()

    def show(self, url):
        print(self.content(url))

    def show_all(self):
        for url in self.cache:
            print(url)

if __name__ == '__main__':
    print("Test Robot class")
    r = Robot('http://gsyc.urjc.es/')
    print(r.url)
    r.show()
    r.retrieve()
    r.retrieve()
    print("Test Cache class")
    c = Cache()
    c.retrieve('http://gsyc.urjc.es/')
    c.show('https://urjc.es/')
    c.show_all()