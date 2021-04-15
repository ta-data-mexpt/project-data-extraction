![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

https://img.shields.io/github/languages/top/rikrdinii1/project-data-extraction?color=green&logo=python&style=plastic

# Project: API and Web Data Scraping

## Descripcion del Proyecto

Navegacion y extraccion de informacion de listas de reproduccion de Spotify. 


## Proceso:

1. Primero se ingresa con las credenciales de la API de Spotify
2. Se crea un objeto con el cual se maneja toda la parte de accesar a la info de la API, 
   la generacion de los "Headers", el token de acceso, los permisos pertinentes y refrescar el token si este ah caducado. 
3. Se inicia ingresando a las listas de reproduccion del usuario con su "id_usuario"
4. Para el proyecto solo se busca analizar y extraer la info de dos listas de reproduccion, por lo cual se deja el codigo general
   y el especifico.
   En este, se le pide al usuario que ingrese que lista de reproduccion se desea analizar, y el codigo itera por cada uno de 
   los items (canciones) que se encuentran en dicha lista de reproduccion, se extrae la info de cada cancion y por ultimo se
   unen ambas tablas de informacion (canciones, caracteristicas de canciones)
5. Por ultimo se extrae la informacion en un CSV, que se guarda directamente en la carpeta en la cual se tiene el codigo. 


## Entregables:

1. Codigo
2. CSV correspondiente a la lista de reproduccion de Ricardo, Brenda y Listas Extras encontradas


## Documentacion:

Documentacion para las Playlist: 
 https://developer.spotify.com/documentation/web-api/reference/playlists/get-a-list-of-current-users-playlists/

Documentacion Obtencion de info de las listas de reproduccion:
 https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-audio-features/

Documentacion para la info de las canciones:
 https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/

Referencia para el login en la API de Spotify:
 https://www.youtube.com/watch?v=xdq6Gz33khQ&t=4594s&ab_channel=CodingEntrepreneurs


