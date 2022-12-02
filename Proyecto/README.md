El proyecto se basa en una necesidad del trabajo.

La empresa para la que trabajo se basa en la compra y venta de artículos varios, teniendo varias áreas de mercado en donde se trabaja.
Por lo que se requiere bajar la información de paginas web, tanto para bajar las bases de datos de las páginas web de proveedores, así como también el poder realizar una copia de una pagina similar, con los productos base iniciales.
En ambos casos se requiere de bajar los datos, así como las imágenes de los productos.
En este caso la pagina que solicito uno de los jefes, fue la siguiente:
url = 'https://henki.com.mx/producto/results/categoria/1'
y lo que solicito de información fue:

•	nombre producto
•	marca
•	modelo
•	precio
•	descripción del producto
•	URL IMAGEN (SI ERA POSIBLE LA IMAGEN DEL PRODUCTO)

Al revisar la pagina me encontré con una pagina principal donde carga todos los productos, sin embargo, el primer obstáculo fue que hasta que bajas en el scroll, es que va cargando producto a producto.
Por lo que primero se realizó un scroll de:
driver = webdriver.Chrome(options=chrome_options)
estos escroll con tiempos para poder dejar que cargara la página, para posterior volver a bajar, así hasta llegar al final y poder realizar una extracción.

De esta pagina solo se saco el nombre del producto y el link de este, debido a que se requería ir a la pagina personal del producto para obtener toda la información solicitada.
Una ves obtenido esta lista, de mas de 2900 productos, se paso a realizar una función para que realizara un request de cada uno de las páginas.

Dentro de estas, en el request se iba sacando los elementos solicitados, en este caso se realizo uso de RSS, para poder obtener los datos.
Posterior se le realizo una limpieza dentro de la extracción para obtener los datos lo mejor posible.
Una ves esto se realizo una lista general de todos los productos y se hizo un data frame de este.
Posterior se realizo una limpieza de los datos, ya una ves hecho el data frame.

Como plus, se realizó un segundo request, de los link de las imágenes, para bajar la imagen, renombrarla como imagen_”numero de image”, esto dentro de una carpeta imagen.

Posterior se exporto a un Excel, donde se pego el data frame principal ya limpio, y se le agrego las imágenes, dentro de la columna a la que pertenecía cada imagen.

Los principales retos fueron el tiempo, que demoro el realizar todo el scraping, para que en algunas ocasiones se frenara por diversos errores, al tratar de realizar un scrap en paginas vacías, o en algunos casos donde no contaba con precio, por lo que al realiza el request daba error.
Así también se uso los header para poder obtener información y sobre todo al querer descargar las imágenes, se requería de una librería especifica que también requería un renombre de heades especifico.

Principalmente el tiempo, fue lo difícil debido a que se iba corrigiendo el código con forme se corría el programa y este bajo el camino de los scrap, iban teniendo distintos errores.

el enlace con la carpeta de todos los datos es:
https://drive.google.com/drive/folders/1p80uS_l72on0jYK0b78Jj6yc3CnEXW84?usp=share_link
