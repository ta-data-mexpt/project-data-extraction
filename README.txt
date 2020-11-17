Emilio Flores Cortes DAPT 09/20 Ironhack Mexico

SCRAPPING https://www.leagueofgraphs.com/

I wanted to retrieve all matches from soloqueue of a given player(s) to later saved it as a csv document.

At first I thought it could be easy to scrap because I just needed some basic info (name, rank, worldwide rank position, regional position, LP and match history. Well... LP points for a challenger is different (somewhow) to LP for an Iron, also if the summoner is unranked well... what info can you get from him? That was also a challenge.

Something a learned is that before beginning scrapping a page is to try and make all posible cases in case a result can't be found and if there's and easier way to get the info you need try and do it. (pd.read_html if you need info from a table or maybe just requests instead of selenium)



