#!/usr/bin/python3

"""Solución del ejercicio "Descarga de documentos web"
Solución con módulos: módulo para la clase Cache
"""

from robot import Robot

class Cache:

    def __init__(self):
        self.cache = {}

    def retrieve(self, url):
        if url not in self.cache:
            bot = Robot(url = url)
            self.cache[url] = bot

    def content(self, url):
        self.retrieve(url)
        return self.cache[url].content()

    def show(self, url):
        print(self.content(url))

    def show_all(self):
        for url in self.cache:
            print(url)

if __name__ == '__main__':
    print("Test Cache class")
    c = Cache()
    c.retrieve('http://gsyc.urjc.es/')
    c.show('https://www.aulavirtual.urjc.es')
    c.show_all()
