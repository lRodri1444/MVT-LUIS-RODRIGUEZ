--------------------------README--------------------------

LIBRERIAS EXTERNAS REQUERIDAS:
------------------------------

1) Django https://www.djangoproject.com/download/
2) django_countries https://pypi.org/project/django-countries/

ACERCA DEL PROYECTO:
--------------------

Web para ensayar modelos, formas y filtros.

LINKS:
------

Pagina de inicio : <runserver_port>
Pagina de filtros : <runserver_port>/filter

No es necesario tipear el enlace, los hipervínculos agregados en la navbar de bootstrap estan configurados.

Aviso de error : El nav-link "Pricing" no redirige a ningúna pestaña. Es parte de la dummy data del snippet.

PAGINA DE INICIO:
-----------------

Página que carga 3 formularios para almacenar data correspondiente a los modelos "Persona", "Job", "Migration", 
la data será enviada al servidor tras presionar el botón "Create New".

El campo Document ID requiere de 8 enteros positivos, mientras que los campos Health Insurance ID, 
Passport ID y Phone Number requieren de 9 enteros positivos.

Los campos : Document ID, Health Insurance ID y Passport ID están configurados con unique=True, 
por lo que cargar dummy data ya existente en esos campos ejecutará un error_message.

Aviso de error : Los campos Document ID, Phone Number, Health Insurance ID y Passport ID 
no aceptan valores que inicien en 0 incluso si se respeta el mínimo de dígitos.
La web no se colgará, pero el error_messages configurado en el validator no dejará que se suba la data.

PAGINA DE FILTROS:
------------------

Página que toma 3 argumentos : Document ID, Health Insurance ID y Passport ID.

Al ingresarse estos 3 argumentos la pagina redireccionará sobre si misma mostrando un nuevo template
con la data del usuario al que correspondan los argumentos.

Es posible ingresar un nuevo filtro desde la misma página donde se muestran los datos.

De no llenarse los 3 argumentos, no se ejecutará el filtro. Los mensajes de error de filtros aun no fueron configurados.

DUMMY DATA:
-----------

Data ya registrada que se puede ingresar en la pagina de filtro para comprobar la funcionalidad:

1) Autor

Document ID         : 72682396
Health Insurance ID : 123456789
Passport ID         : 120249298


2) Diego Maradona

Document ID         : 41231592
Health Insurance ID : 452326075
Passport ID         : 376539892

3) Ben Affleck

Document ID         : 54391370
Health Insurance ID : 360254196
Passport ID         : 300124698

4) Steve Harvey

Document ID         : 20136985
Health Insurance ID : 629622042
Passport ID         : 142333611