#!/usr/bin/python3

"""Solución del ejercicio "Descarga de documentos web"
Solución con módulos: módulo para la clase Robot
"""

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

if __name__ == '__main__':
    print("Test Robot class")
    r = Robot('http://gsyc.urjc.es/')
    print(r.url)
    r.show()
    r.retrieve()
    r.retrieve()
