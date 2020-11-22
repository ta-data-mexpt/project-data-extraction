Emilio Flores Cortes DAPT 09/20 Ironhack Mexico
SCRAPPING https://www.leagueofgraphs.com/
I wanted to retrieve all matches from soloqueue of a given player(s) and it as a csv document.


At first I thought it could be easy to scrapp because I just needed some basic info (summoner name, if the player won or lose the game, when that matched was played, duration, kills, deaths, assists, overall kda and cs.

First, getting the right page to scrap needed some research as most of them just keeps recent matches (no more than 2 months) and some of the players I wanted to get their match history hadn't played ranked SoloQ for that long. 

Second, getting to know the page was quick but trying to scrap it took more than what I wanted to. "Selenium" was the best instrument to use as the see all the matches a button needed to be clicked (the "Show more" button) many  times.

Third, once the page was scrapped, using pandas.read_html() make all of the work easier but that Dataframe panda got me wasn't the way I like it, so the next step was to organize that information in a nicer format. To separate KDA (into K, D, A) and calculating the overall KDA I used regex to make it easier.

And finally, I used a for loop to save each match history and concatenate it to a Dataframe and save ALL match histories into one Dataframe.

Before beginning to scrap a page make sure to define the type that each data need to be (you can't make math operations with numbers being strings...), and also think to future and scrap at once all the info you think you will be needing later on.
