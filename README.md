Proyecto API

Mi proyecto de API consistio en estar monitoreando los vuelos tanto comerciales como privados sobre un area especifica que determina el usuario del programa. 
En el caso del programa realizado estuve trabajando en las latitudes y longitudes que corresponden tanto a USA como a Mexico y monitoree tanto en la madrugada
como en el dia y se logro apreciar un aumento significativo de trafico de aviones tanto en Mexico como en USA en el dia.
Es importante mencionar que tuve que leer bastante con relacion a como se leen las coordenadas tanto de latitudes y longitudes de acuerdo al standard WGS84, 
ademas de leer acerca del ADS-B (vigilancia dependiente automatica - difusion) que es la tecnologia que permite determinar la posicion de los aviones a traves
de la navegacion por satelite.

La API fue establecida directamente con el sitio de opensky-network. Despues de leer las relacionado con las autenticaciones y altas, este indicaba que si eres
un usuario registrado, el tiempo de muestreo puede ser como minimo cada 5 segundos mientras que con usuarios no registrados la frecuencia minima de monitoreo es
de 10 segundos. Aunque intente varias veces en registrarme para poder tener mejores tiempos de monitoreo. El sitio de opensky presento problemas para terminar el
registro, por lo que termine trabajando con usuario no registrado.

una vez que logre realizar la consulta al sitio de opensky desde mi endpoint, procedi a trabajar en cargar la DataFrame de panda, definiendo los nombres de las 
columnas y pude apreciar datos desde la clave de las aerolineas, como paises donde salen los vuelos, la hora de despegue, hora del ultimo contacto (timestamp)
entre otros. Posteriormente, salve las tablas a archivos CSV, mismos que se pueden consultar en esta misma carpeta. Estos archivos comprenden monitoreos para
USA y Mexico.

Posteriormente, me parecio interesante que existen algunas APIs que ayudan a visualizar las posiciones de los aviones mediante dibujos de graficos de vectores que
representan los datos. Es mendianto el modulo Bokeh.plotting que se loga incluir los elementos como lineas, cuadros y demas figuras que representan los desplaza-
mientos y las posiciones actuales.



PROYECTO WEB-SCRAPER

En mi trabajo de WebScraper, hay 2 accesorios que siempre estoy buscando su mejor precio y los monitoreo muy seguido para comprarlos. Aprovechando mi aprendizaje
de webscraper, los conocimientos adquiridos de Dev tools y lo estudiado de HTML y CSS, quise hace un programa que me ayude a monitorear los items que tengo 
identificados en Amazon.

Los modulos con los que inicialmente tenia previsto trabajar son requests, BeautifulSoup y time. Fue despues de que identifique que iba a extraer el nombre del 
producto mediante su ID y el precio de este mediante una clase 'span',{'class':'a-price-whole'}. Despues de un par de intentos me di cuenta que no era posible
extraer la informacion con los modulos antes mencionados, por lo que decidi utilizar los modulos de selenium (keys, ActionChains). Posteriormente procedi a 
establecer comunicacion y esta vez si logre una comunicacion exitosa y logre ver los datos de los productos que deseaba.Todo lo puse en una funcion para poder
misma que me permite extraer los datos deseados, ademas de limpiarlos y darlos forma.

Una vez solucionado el reto de recolectar los datos del producto de la pagina, me puse a trabajar en lo referente a como enviarme las notificaciones de que 
el producto a monitorear cumpliera alguna de las condiciones establecidas. Decidi, por tanto, que lo haria mendiante el email.
Una vez decidido que enviaria las notificaciones via email, entonces instale el modulo de 'smtplib'. Despues me fui a generar una contraseña para apps en mi 
cuenta de google, para que me permitiera enviar correos desde el enlace del programa una vez que una condicion de un producto se lograra.

Configure el tema del correo, asi como el cuerpo de este. A continuacion coloque dos cuentas de correo electronicos donde quiero recibir las alertas con las
condiciones buscadas y por ultimo coloque un timer para estar monitoreando el producto con una frecuencia definida. En el caso del programa estara monitoreando
cada 20 minutos.

Para este trabajo monitoree dos productos y al reducor el valor del time.sleep a 20 segundos, tras lograr la condicion del precio, el programa me envio los 
mensajes recurrentemente a mi correo establecido. En la carpeta de output agregue un par de correos que recibi.

Los retos principales consistieron en la configuracion del modulo del email, ademas de que Amazon me estuvo bloqueando mis consultas cuando baje la frecuencia 
de muestreo con mi time.sleep. 
En otra ocasion, mi contraseña para app se vencio y por tanto tambien dejo de enviarme las alertas y fue hasta que genere una nueva, que logre recibir mis
notificaciones.


******************************************************************************************************************************************************************************************************************************************


![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: API and Web Data Scraping

## Overview

The goal of this project is for you to practice what you have learned in the APIs and Web Scraping chapter of this program. For this project, you will choose both an API to obtain data from and a web page to scrape. For the API portion of the project will need to make calls to your chosen API, successfully obtain a response, request data, convert it into a Pandas data frame, and export it as a CSV file. For the web scraping portion of the project, you will need to scrape the HTML from your chosen page, parse the HTML to extract the necessary information, and either save the results to a text (txt) file if it is text or into a CSV file if it is tabular data.

**You will be working individually for this project**, but we'll be guiding you along the process and helping you as you go. Show us what you've got!

---

## Technical Requirements

The technical requirements for this project are as follows:

* You must obtain data from an API using Python.
* You must scrape and clean HTML from a web page using Python.
* The results should be two files - one containing the tabular results of your API request and the other containing the results of your web page scrape.
* Your code should be saved in a Jupyter Notebook and your results should be saved in a folder named output.
* You should include a README.md file that describes the steps you took and your thought process for obtaining data from the API and web page.

## Necessary Deliverables

The following deliverables should be pushed to your Github repo for this chapter.

* **A Jupyter Notebook (.ipynb) file** that contains the code used to work with your API and scrape your web page.
* **An output folder** containing the outputs of your API and scraping efforts.
* **A ``README.md`` file** containing a detailed explanation of your approach and code for retrieving data from the API and scraping the web page as well as your results, obstacles encountered, and lessons learned.

## Suggested Ways to Get Started

* **Find an API to work with** - a great place to start looking would be [API List](https://apilist.fun/) and [Public APIs](https://github.com/toddmotto/public-apis). If you need authorization for your chosen API, make sure to give yourself enough time for the service to review and accept your application. Have a couple back-up APIs chosen just in case!
* **Find a web page to scrape** and determine the content you would like to scrape from it - blogs and news sites are typically good candidates for scraping text content, and [Wikipedia](https://www.wikipedia.org/) is usually a good source for HTML tables (search for "list of...").
* **Break the project down into different steps** - note the steps covered in the API and web scraping lessons, try to follow them, and make adjustments as you encounter the obstacles that are inevitable due to all APIs and web pages being different.
* **Use the tools in your tool kit** - your knowledge of intermediate Python as well as some of the things you've learned in previous chapters. This is a great way to start tying everything you've learned together!
* **Work through the lessons in class** & ask questions when you need to! Think about adding relevant code to your project each night, instead of, you know... _procrastinating_.
* **Commit early, commit often**, don’t be afraid of doing something incorrectly because you can always roll back to a previous version.
* **Consult documentation and resources provided** to better understand the tools you are using and how to accomplish what you want.

## Useful Resources

* [Requests Library Documentation: Quickstart](http://docs.python-requests.org/en/master/user/quickstart/)
* [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Stack Overflow Python Requests Questions](https://stackoverflow.com/questions/tagged/python-requests)
* [StackOverflow BeautifulSoup Questions](https://stackoverflow.com/questions/tagged/beautifulsoup)
