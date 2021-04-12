# Prueba Técnica DjangoLinets
## Descripción
Se ocupo Docker para montar el ambiente de desarrollo.
[![Try in PWD](https://github.com/play-with-docker/stacks/raw/cff22438cb4195ace27f9b15784bbb497047afa7/assets/images/button.png)](http://play-with-docker.com?stack=https://raw.githubusercontent.com/nextcloud/docker/8db861d67f257a3e9ac1790ea06d4e2a7a193a6c/stack.yml)

> El proyecto esta versionado utilizando git


####Requerimientos
                
+ 1 Crear un comando personalizado de django que genere el fichero csv con el formato descrito anteriormente
+ 2 Crear un endpoint utilizando rest framework para:
    + a Consultar productos
    + b Cargar nuevos productos
+ 3 Crear una interfaz web para generar el csv (ejecute el comando generado en el paso 1). Utilice bootstrap para dar formato a la interfaz (basta con un botón)

##Manual de navegacion de APP

Al escribir en consola **python manage.py export** se exportara el fichero csv a la carpeta raiz del proyecto. 

Desde el localhost se podra navegar por un menu de dos opciones:

+ INICIO
+ SERVICIOS

Donde **INICIO** nos llevara a un boton que EXPORTARA el csv formateado como el ejemplo del output esperado.

Esto lo hace gracias a un cursor que lo podemos encontrar en la funcion hubicada en: 

CsvApp\management\commands\export.py

### Al desplegarlo desde el boton "Exportar Csv" el programa se cae pero si logra exportar 😔

La opcion **SERVICIOS** desplegara un boton que nos llevara directo a un endpoint creado con **Django Rest Framework** y si, es la cumbia, lo deje programado para que diera todo **status** correctamente, el endpoint tiene el CRUD completo **PERO PERO PERO**  😔 para un modelo User por que tuve problemas con el que enviaron.

##Gracias por la oportunidad