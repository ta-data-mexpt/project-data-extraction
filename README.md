
![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)  |    ![](https://i.ibb.co/3186ns9/fbe8b5cf8780a6a5f6ff3678e60ed349.png)
-------------------------------------------|----------------------------------
 
# Project: API and Web Data Scraping

## Overview

This project consists of a jupyter notebook file that calls the CoinMarketCap's API to obtain a certain number of top crypto coins based on a specific currency (both of them given by the user as inputs). The ***_main-api.ipynb_*** file also does a little bit of web scraping through the CoinMarketCap's API and Selenium's webdriver documentation to retrieve data of interest for the user to decide what supported parameters are able to pass through the code's functions. 

When all of the inputs are given correctly by the user, the result displays a pandas DataFrame that then gets saved as a csv file to a path also defined by the user.

--
## Requirements

For the ***_main-api.ipynb_*** file to run correctly, the user needs to have:

* Selenium webdriver
* A valid CoinMarketCap API key that can be obtained [here](https://pro.coinmarketcap.com/signup)

## Files

* **Jupyter Notebook (.ipynb) file** contains the code used to work with the API and scrape the web pages.
* **Output folder** contains the output of the API and scraping results.
* **This ``README.md`` file** contains an explanation of the approach, code and useful information. 


## Useful Resources

* [Selenium webdriver download](https://pypi.org/project/selenium/)
* [Selenium with Python](https://selenium-python.readthedocs.io/index.html)
* [CoinMarketCap API documentation](https://coinmarketcap.com/api/documentation/v1/#)

