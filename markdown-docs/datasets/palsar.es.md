##L1.0 Productos
Este producto se genera a partir de los datos de observación sin procesar (Nivel 0) a través de la edición de datos, como la realineación de bits y la adición de información de órbita. Se trata de datos de señal reconstruidos, sin procesar, con coeficientes de corrección radiométricos y geométricos (adjuntos, pero no aplicados).

##L1.1 Productos
Este producto se genera a partir de productos Single Look Complex (SLC) igualmente espaciados en el rango de inclinación (igual al espaciado de la medición de muestreo), generados después de renderizar el procesamiento SAR a un producto de nivel 1.0. Estos productos están comprimidos en rango y azimut. Se conserva la información de amplitud y fase. Se proporcionan archivos individuales para cada polarización para modos de polarización múltiple.

##L1.5 Productos
Este producto se genera a partir de imágenes de amplitud Multi-look proyectadas en coordenadas de mapa (georreferenciadas). Esto se representa desde el procesamiento SAR hasta productos de nivel 1.0, y se adquiere en modo de alta resolución de polarización única. Estos productos pueden visualizarse sin procesamiento adicional. Se proporcionan archivos individuales para cada polarización para modos de polarización múltiple.

##KMZ Productos
Este producto es un archivo comprimido que incluye un archivo KML y un archivo de imagen de exploración de color (PNG). El KMZ se puede descomprimir cambiando la extensión del archivo .kmz a .zip y descomprimiéndola.

Puede ver el .kmz en Google Earth o en un programa similar. Una vez descomprimido, el archivo .kml también se puede ver en Google Earth. Abierto en Google Earth, el archivo se muestra en un contorno de la huella de la escena en la Tierra, e incluye áreas sin datos, y una exploración en color de la imagen geocorregida en su orientación correcta dentro del contorno. El archivo .png se geocodifica y gira en el espacio proyectado.

##Low-Res y Hi-Res Productos Corregidos por Terreno
Los productos de corrección del terreno se generan para todos los modos de haz FBS, FBD y PLR, e incluyen todos los modos de haz disponibles para datos de doble pol y qual-pol. Cualquier dato de haz ancho, así como los datos de red de fuente directa (DSN) de enlace descendente directo, adquiridos por ASF a resolución reducida, no se corrigen en el terreno.

Los productos corregidos del terreno se derivan de datos complejos de aspecto único ALOS PALSAR Nivel 1.1, generados por el procesador JAXA Sigma SAR (versión 12.01) del software central ALOS (versión 6.07).

Los productos RTC se distribuyen en dos resoluciones. Los productos de alta resolución tienen un tamaño de píxel de 12,5 m y se generan a partir de DEM de alta resolución (NED13) y resolución media (SRTM 30m, NED1 y NED2). Los productos de baja resolución se generan a un nivel de 30 m para todos los DEM disponibles. Todos los productos son terreno corregido en el tamaño de píxel nativo del DEM que se utiliza para la corrección. No se requiere un nuevo muestreo adicional. Todos los productos RTC están geocodificados a la proyección Universal Transverse Mercator (UTM) y se proporcionan como valores de potencia de punto flotante en formato GeoTIFF. La referencia para los productos RTC es píxel como punto.

##Further Lectura
- [Información DEM](https://asf.alaska.edu/information/palsar-rtc-dem-information/)
- [Descripción del formato del producto de nivel 1.0](http://www.ga.gov.au/__data/assets/pdf_file/0019/11719/GA10287.pdf)
- [Nivel 1.1/1.5 Descripción del formato del producto](https://www.eorc.jaxa.jp/ALOS/en/doc/fdata/PALSAR_x_Format_EL.pdf)
- [Sistema de procesamiento de radar USGS ALOS PALSAR](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-radar-alos-palsar-radar-processing-system?qt-science_center_objects=0#qt-science_center_objects)
- [¿Qué es un archivo KMZ?] (https://developers.google.com/kml/documentation/kmzarchives)
- [Diferencia entre KML y KMZ](https://whyisdifference.com/technology/software-technology/difference-between-kml-and-kmz.html)
- [Guía del producto RTC](https://asf.alaska.edu/wp-content/uploads/2019/03/rtc_product_guide_v1.2.pdf)
- [RTC Algorithm Technical Basis Document](https://asf.alaska.edu/wp-content/uploads/2019/03/rtc_atbd_v1.2_final.pdf)
- [Especificación de formato del producto](https://asf.alaska.edu/wp-content/uploads/2019/03/rtc_product_specification_v1.1.pdf)





