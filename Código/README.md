# Código para extraer información de casos COVID19


Los siguientes códigos fueron elaborados de dos maneras, el primero para sacar la cantidad de casos confirmados, decesos y recuperaciones como un "summary" hasta la fecha actual, es decir datos acumulados.

El segundo código fue elaborado para poder extraer por día, por país la información de casos confirmados, decesos y recuperaciones a manera de histórico.

## Primer caso:

https://api.covid19api.com/summary

Se utulizó esta API para poder extraer los datos hasta la fecha actual de forma acumulada con los siguientes pasos.

    1. Se importaron las librerías necesarias
    2. Se solicita la información de la API  por medio de un .get
    3. Se convierte en un json
    4. Se limpia la información, identificando la etiqueta que necesitabamos extraer
    5. Se guarda en una variable y se transforma en un dataframe
    6. Se transofrma en un archivo csv, el cual se le determinó la ruta donde debe de guardar el archivo\          en mi computadora, donde además se cofniguró para que el título del archivo lleve el nombre del\          día que se descarga
    
Siguientes pasos?


    1. Poder programar que el código se ejecute por sí solo diariamente a la misma hora
    2. Poder insertar la información en un Google Sheet, ya que desde ahi es utilizado para un dashboard
    

## Segundo caso:

https://api.covid19api.com/country/afghanistan?from=2019-11-01T00:00:00Z&to=2019-11-01T23:59:59Z

Para poder consultar la información de manera histórica, la API nos indicaba que debíamos de especificar en la URL el país y la fecha de inicio y fin de la información consultada

    1. Se utilizó el json del summary extraido anteriormente para que por medio de un for pudieramos            obtener el nombre de los 191 países
    2. Se utilizó un segundo for para poder concatenar la liga 'https://api.covid19api.com/country/' a          cada país
    3. Se realizaron dos for, para poder crear las fechas de inicio y fin que necesitaba cada URL, se            debe mencionar que se tuvo que hacer una fecha por día, para poder obtener los historícos
    4. Por medio de otro for a cada país se le agregaron las fechas desde el 1 de noviembre de 2019              hasta 14 de nov de 2020 
    5. En total se obtuvieron 75,636 ligas
    6. Para poder hacer el pipeline, se guardaron esas 75,636 ligas en un csv
    7. Se crearon funciones que primero manden llamar en forma de lista al archivo de las ligas
    8. Por medio de un for se hace el request de un rang de ligas, donde posteriormente se transofrma en        un json y al ultimo lo trasnforma en un dataframe para poder ser exportado en un csv
    9. Se trasformo en un .py para que solo modifique 3 cosas: el rango de ligas (hasta que llegue a las        75,636, y el cambio de nombre de archivo csv en el que se guarda
    
Posterior a eso, con los 8 archivos que tenía, solicité todos los archivos y los uni para armar un solo archivo
    
Siguientes pasos?

    1. Se deberan correr las 75,636 ligas para poder obtener los historicos
    2. Teniendo almacenados todos los csv en una carpeta, por medio de pandas manipular todos los                archivos para concatenarlos u hacerlos uno solo
    3. Calcular 3 columnas que hacen falta para que quede de la misma manera que el summary
    
    
## ¿Qué se entrega?:

2 archivos de notebook donde se hicieron los códigos de manera simple
3 archivos .py que como pipeline:
    el summary diario
    request para historico a través de rangos
    el que lee varios csv y los acumula en un solo csv
4 archivos:
    ejemplo de descarga summary
    ejemplo de descarga histórico
    archivo con las 75,636 ligas
    ejemplo de compilado de 8 archivos csv a un solo csv