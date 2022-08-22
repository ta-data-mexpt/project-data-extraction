
# Ironhack Proyecto 2: API

Se utilizan los protocolos API para obtener información de la Energía Asignada de Importación y Exportación del Centro Nacional de Control de Energía (CENACE).

## Fuente de información

El Servicio Web para descarga de Energía Asignada de Importación y Exportación ([SW-EAIMPEX](https://www.cenace.gob.mx/DocsMEM/2022-06-24%20Manual%20Técnico%20SW-EAIMPEX.pdf)) es un servicio que brinda el CENACE para descargar información sobre los resultados de la ejecución del Mercado del Día en Adelanto (MDA). 

Este servicio permite obtener la información de los puntos de importación y exportación de energía eléctrica.

## Solicitud
Obtener información de las Cantidades Asignadas de Importación y Exportación del MDA del Sistema Interconectado Nacional (SIN), correspondiente al Día de Operación del 01 al 31 de julio de 2022.

* **Nota:** Se realizan varias peticiones de consulta para periodo establecido, ya que la página del CENACE solo permite descargar informació de 1 a 7 Días de Operación.

## Información adicional
El Sistema Interconectado Nacional cuenta 13 interconexiones internacionales ubicadas en los estados fronterizos. Existen 11 interconexiones con Estados Unidos y 2 interconexiones con Centroamérica (uno con Guatemala y uno con Bélice).

La información de las interconexiones obtenidas del CENACE son:

    1. Ciudad Industrial - Laero Amer (interconexión con ERCOT, Texas)
    2. Cumbres Frontera - Railroad (interconexión con ERCOT, Texas)
    3. Piedas Negras - Eagle Pass (interconexión con ERCOT, Texas)
    4. Tapachula - Los Brillantes (interconexión con ETCEE, Guatemala)
    5. Xul Ha-WEST (interconexión con BEL, Bélice)

<p align="center">
<img width="600" alt="image_interconexiones" src="https://user-images.githubusercontent.com/108844724/185035023-569f126b-99b9-4982-a81f-e25ea12a6cd3.png">
</p>


-----------------
-----------------

# Ironhack Proyecto 2: Web scraping

Se utiliza Web Scraping para conocer la Clasificación de la Asociación Femenina de Tenis (WTA, *Women's Tennis Association*). Esta Clasificación pertenece al ranking mundial de tenistas femeninas que publica la WTA desde 1975.

<p align="center">
<img width="300" alt="Women's_Tennis_Association_logo_(2020) svg" src="https://user-images.githubusercontent.com/108844724/186027090-5e0fb27c-fb15-4d64-a233-e20df1dcc9b0.png">
</p>


## Fuente de información

La información es obtenida de la página [WTA rankings](https://en.wikipedia.org/wiki/WTA_rankings) de Wikipedia. Esta Clasificación es actualizada cada semana, como resultado de los puntos obtenidos por cada tenista de los torneos realizados en las últimas 52 semanas.


## Solicitud
Obtener de la Clasificación WTA con mayor puntaje en las modalidades *single* y *doubles individual*.

**Nota**: la información presentada es hasta la semana del 15 al 21 de agosto de 2022.

