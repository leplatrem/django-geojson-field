Example project of GeoJSON fields, with Leaflet widgets:
Geographic data edition without GIS stack.

=======
INSTALL
=======

Install project dependencies :

::

    virtualenv env
    source env/bin/activate

    python setup.py develop

======
PLAY !
======

::

    python manage.py syncdb
    python manage.py runserver
