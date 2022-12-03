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


EXTRACCIÓN DE DATOS PERSONALES DE FITBIT API

1. Leer documentación de API (https://dev.fitbit.com/build/reference/web-api/)
2. Iniciar sesión con mi cuenta personal de FitBit y crear una cuenta de "developer" (dev.fitbit.com). En ésta cuenta de developer se debe crear una aplicación y en base a los datos de la aplicación se genera un token y un client ID.
3. Con el token y el client_ID, se genera un link que se debe pegar en el navegador para autorizar a la API la extracción de datos personales de la cuenta en gestión. Se debe especificar por cuánto tiempo se permitirá la extracción de datos personales. En mi caso, yo permití el acceso por 30 días. Mi link para la autorzación de extracción de datos, quedó de la siguiente manera: 
https://www.fitbit.com/oauth2/authorize?response_type=token&client_id=2393C4&redirect_uri=http://127.0.0.1:8080/&scope=activity%20nutrition%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=2592000
4. Para la extracción de cada tipo de información, la API proporciona un formato del link para el "get". En este caso tuve que iterar algunas fechas, pues el formato de la API sólo permitía la extracción de un intervalo de tiempo menor al deseado.
5. Obtuve diferentes categorías de información personal (calorías, pasos y distancia) para un período de 2 años (2021 y 2022), así como la cantidad de horas dormidas en el año 2019 (sólo se registran los días en los que usé el tracker para dormir).
6. La información obtenida no ha sido "limpiada", pues en eso consistirá la segunda parte del proyecto.

Challenges:
-La parte más complica fue obtener la autorización para accesar a mi información, pues había que crear una cuenta de developer y crear una aplicación ficticia.
-El proceso de iteración de fechas y concatencación de tablas.