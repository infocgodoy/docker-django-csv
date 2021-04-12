# Prueba Técnica DjangoLinets
## Descripción
Se ocupo Docker para montar el ambiente de desarrollo.
[![Try in PWD](https://github.com/play-with-docker/stacks/raw/cff22438cb4195ace27f9b15784bbb497047afa7/assets/images/button.png)](http://play-with-docker.com?stack=https://raw.githubusercontent.com/nextcloud/docker/8db861d67f257a3e9ac1790ea06d4e2a7a193a6c/stack.yml)

####Requerimientos
                
+ 1 Crear un comando personalizado de django que genere el fichero csv con el formato descrito anteriormente
+ 2 Crear un endpoint utilizando rest framework para:
    + a Consultar productos
    + b Cargar nuevos productos
+ 3 Crear una interfaz web para generar el csv (ejecute el comando generado en el paso 1). Utilice bootstrap para dar formato a la interfaz (basta con un botón)

##Manual de navegacion de APP

Desde el localhost se podra navegar por un menu de dos opciones:

+ INICIO
+ SERVICIOS

Donde **INICIO** nos llevara a un boton que EXPORTARA el csv formateado como el ejemplo del output esperado.

Esto lo hace gracias a un cursor que lo podemos encontrar en la funcion export hubicada en 
docker-django-csv\CsvApp\views.py

La opcion **SERVICIOS** desplegara un boton que nos llevara directo a un endpoint creado con **Django Rest Framework** y si, es la cumbia, el endpoint tiene el CRUD completo **PERO PERO PERO** para un modelo User por que tuve problemas con el que enviaron.

Ahora estoy buscando documentacion para Custom Django Management, si bien se como crear un comando personalizado, no puedo encontrar la forma de que cree un fichero csv, encontre algunas formas en las cuales abre un csv que se encuentra **commands** lo edita y luego lo cierra. Esperemos que esto cambie de hoy Domingo 11 hasta mañana lunes 12.

##Gracias por la oportunidad