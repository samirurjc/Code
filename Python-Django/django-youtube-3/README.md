# Django YouTube (versión 3)

En esta versión hemos sustuido las plantillas que teniamos en
`views.py`, y que se utlizaban con el `format` de Python3,
por plantillas Django, declaradas a partir de strings
(puedes verlo en el mismo fichero `views.py`, las plantillas
se llaman `PAGE` y `VIDEO`, igual que antes).

Lo hemos hecho de esta forma, en lugar de usar ficheros de
plantilla (que es lo más habitual), para ayudar a entender
que las plantillas no son más que texto que cuando se resuelve
(con `render`), proporcionándole un determinado contexto,
se sustituyen las variables según ese contexto, y se
ejecutan las estructuras de control (bucles, etc.).

También puede verse cómo una plantilla (`PAGE`) incluye a otra
(`VIDEO`), especificando qué contexto se usará para resolverla.

Hay también un test nuevo (en `test.py`) para hacer algunas
comprobaciones sobre las plantillas, incluyendo que se han usado
cuando se hace un `GET /`, y que el contexto que se les ha pasado
tiene la pinta adecuada.

Para hacer funcionar el programa:

```bash
% rm db.sqlite3
% python3 manage.py makemigrations
% python3 manage.py migrate
% python3 manage.py runserver
```

**Documentación:**

* [Loading a template](https://docs.djangoproject.com/en/3.0/ref/templates/api/#loading-a-template)
  y secciones siguientes en [Templates API](https://docs.djangoproject.com/en/3.0/ref/templates)
  en la documentacion de Django. Explica con detalle cómo se instancia
  un objeto de la clase Template, proporcionando un string (que dará
  lugar a la plantilla) para incializarlo, y como se resuelve (render)
  un contexto que se le pase.
