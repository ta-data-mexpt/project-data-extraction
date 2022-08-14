![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: API and Web Data Scraping

## Overview

In this project I obtained data from two sources: an API and a website which I scrapped.

API data extraction:

The API used was the Rick and Morty API. The documentation can be found here: https://rickandmortyapi.com/documentation/ and the actual API can be found here: https://rickandmortyapi.com/

The API presented no special difficulties since all calls had to be made using the GET method and there were no authorization requirements like API Keys or similar.

The endpoint used whas the /character endpoint, which allows users to retrieve information for all characters who have appeared in a Rick and Morty episode. The main challenge encountered was that the results returned by the endpoint were paginated, with 20 results in each page. The results returned for each call indicated if there were more results in the next page, so it was just a matter of checking this information.

Another challenge tackled was how to make the script usable for all endpoints of the API, and not just for the /character endpoint. This was solved creating a dictionary with all endpoint paths, so that we can just call the name of the path and the endpoint url will be built to be able to call that endpoint. Extracting the information from each endpoint works the same way for all endpoints. 

The only problem is when we want to create a dataframe with the information obtained from each endpoint, because in this case each endpoint has different information columns, so what we've done for the information obtained from the /character endpoint will not work for the /location or /episode endpoints. This is perhaps something which can be improved upon in the future.

After that, we just had to obtain the data we wanted for each character, which was: id, name, status, species, type, gender, origin and location. Some results were discarded, such as the episodes the character appeared in or an image of the character.

Web Scrapping:

The website scrapped was properstar.es, which provides information about house listings for rental and purchase. More specifically, I scrapped the url for rental listings in Mexico City for apartments and houses: https://www.properstar.es/mexico/ciudad-de-mexico-loc/alquiler/piso-casa

However, the script should work if we change the location: https://www.properstar.es/{countryname}/{cityname}-loc/alquiler/piso-casa

The main challenges encountered were two:
1) Getting the prices for each listing in Mexican pesos, since by default I was getting them in euros. To achieve this result, I had to use Selenium to navigate the page's menu and click on the option to change the currency the website uses to show prices in.
2) Getting all result pages, since the website only provides 20 results per page. To solve this, I obtained the total number of listings from the first results page, and knowing that number, I was able to calculate the total number of page results and build the url for each of those results pages.

Having solved those two challenges, it was just a matter of obtaining the info I wanted from each listing, which was: title, type of building (house or apartment), price, listing url, number of bedrooms, number of rooms, number of bathrooms, address and surface.


