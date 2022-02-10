#!/usr/bin/python3

"""Solución del ejercicio "Descarga de documentos web"
Solución con módulos
"""

from cache import Cache

if __name__ == '__main__':
    print("Test Cache class")
    c = Cache()
    c.retrieve('http://gsyc.urjc.es/')