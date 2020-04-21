# Django YouTube (versión 2)

Esta versión utiliza una tabla en la base de datos para almacenar la
lista de videos. La tabla incluye un campo que indica si un video está
seleccionado o no. La inicialización de los datos en la base de datos
(la recogida del canal XML de YouTube, y el uso de sus datos para
inicializar la base de datos) se hace mediante migraciones.
El fichero donde está implementada esta parte de inicialización es
`youtube/migrations/0002_video.py`.

Para hacer funcionar el programa:

```bash
% rm db.sqlite3
% python3 manage.py makemigrations
% python3 manage.py migrate
% python3 manage.py runserver
```

Si quieres crear una un fichero como `0002_video.py` en tu proyecto,
en el que aún no has creado "a mano" un fichero de migración,
puedes conseguir uno "vacío" (pero listo para "rellenar"), si
ejecutas, después de haber ejecutado 'makemigrations',
el siguiente comando:

```bash
% python3 manage.py makemigrations --empty youtube --name video
```

(pero esto no lo tienes que ejecutar si estás usando el contenido
de este repositorio, pues ya tienes el fichero `0002_video.py`).

**Documentación:**

* [Data migrations](https://docs.djangoproject.com/en/3.0/topics/migrations/#data-migrations)
  en la documentacion de Django.
