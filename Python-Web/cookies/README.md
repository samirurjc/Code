# Ejercicios sobre cookies

En este directorio hay varios programas relacionados con algunos ejercicios
sobre cookies de la asignatura.
Son servidores web, construidos utilizando el módulo
[http.server](https://docs.python.org/3/library/http.server.html)
de Python.

Para ejecutar cualquiera de ellos,
por ejemplo [cookies-server-6.py](cookies-server-6.py),
descárgalo (bien clonando este repositorio, o bien
descargándolo desde su interfaz web):

```bash
$ chmod 755 cookies-server-6.py
```

Y a continuación, ejecutalo:

```bash
$ ./cookies-server-6.py
Serving at port 1234
```

Si quieres ejecutarlo en un puerto diferente del que tiene
programado por defecto, puedes usar la opción `-p`:

```bash
$ ./cookies-server-6.py -p 2345
Serving at port 2345
```

Una vez lo hayas ejecutado, puedes acceder al servidor
cargando en un navegador, desde la misma máquina,
la url donde está escuchando. Por ejemplo
[http://localhost:1234](http://localhost:1234)
