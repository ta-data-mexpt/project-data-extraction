![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: Web Data Scraping 

In this project I obtained information from the best-selling books in the month of November 2021 for two of the most popular bookselleries in Mexico; Gandhi booksellery and El Sotano bookseller. The information are from the best-selling books in the categories of physical book, electronic book and audio book. 

The data obtained is stored in a csv file called **los_libros + vendidos.csv** which is located in the *output* folder with the following information collected from each book: book, type( physical book, electronic, audiobook), #Topxtipo ( the number occupied by the book in the best sellers by type) , title, author, publisher, edition, format, language, pages, year and price. About 4000 records were obtained in the csv file.


## Steps:

* I got the url of the page of the best-selling books by category of the booksellers. In the case of the Gandhi booksellery there were several pages that kept the best-selling books.

* Through requests and scrapping I got the links of each book using a for loop.

* Through other for loops and scrapping I obtained lists that saved the information of what each column would be in a data frame. I had to adapt the lists and data frames to the information that each page threw on the books and find the patterns that those pages followed.

* I created the data frames by bookseller and type of book.

* I put all the data frames together in one data frame and save it to the output folder as a csv file.