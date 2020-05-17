![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: API and Web Data Scraping _(Learn how to use the API of Riot Games)_

## Overview
The main goal of this project is to practice with 2 different information sources, obtain the desire info and presented
as a guide for both new and regular players. This project will be continued to develop in the future.

## Workflow
During the development of this project was necessary to investigate how to get info from _Riot Games_(game owners).
After that was necessary to get info from another website to complement the info before obtained. The follow steps was 
performed

1. Create or use an account in site of your region _(in my case LATAM)_ in _www.riotgames.com_ 
2. Access to the _https://developer.riotgames.com/_ to request an API key _(keys have a duration of 24 hrs )_ , this 
will allow us to get info from their servers.
    * We can also register your project or product to avoid the refresh of the API key access.
3. In the API documentation you  will find all the _GET_ consults _(the only ones)_ for your program. Also we could
find the documentation for other games.
4. Select a website to scrap, I try in different sites.
5. Clean data and saved as a CSV.

## Results 
Using the API was more useful than the website. I could obtain a table with the basic information of all playable characters
also the icon url for each character, to display the icon was necessary to use specific library from Python.


## Obstacles and Lessons Learned
I found some obstacles, for example in the scraping I had difficulties to obtain the information of main characters used
in this season patch. Also I can't display the icon image in the full DataFrame but in a small table I could display it
so I still working in this issue.
My main lesson learned was rely more on the API than the website.
Also another important point I discover was that there is a lot of information about this game, which actually is the
mainly from Riot Games, but their last game _*Legend of Runeterra*_ exist much lees information. So I could change the
focus of this project.
 
## Links

* [Create an account in Riot Games](https://lan.leagueoflegends.com/es-mx/news/riot-games/)
* [Request API key in developer site](https://developer.riotgames.com/)
* [First site to scrap information about characters](https://lan.op.gg/statistics/champion/)
* [Second site to scrap information about characters](https://u.gg/lol/tier-list?rank=overall&region=la1) 
