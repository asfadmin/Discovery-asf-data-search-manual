# Tipo de Búsqueda SBAS

## ¿Qué es SBAS?
SBAS es un acrónimo de **subconjuntos de líneas de base cortas**. Se trata de una técnica utilizada en interferometría. La herramienta SBAS de Vertex proporciona datos de línea de base perpendiculares y temporales, así como pares de escenas, para una escena de referencia elegida.

## ¿Cuáles son algunos usos de SBAS?
SBAS se utiliza ampliamente en la comunidad de las geociencias. Funciona mejor en entornos naturales a gran escala y se puede utilizar para analizar cambios graduales a lo largo del tiempo. SBAS requiere la entrada de una serie de interferogramas y el resultado final es una serie temporal que muestra el movimiento.

Una ventaja de SBAS es que no estás restringido a un solo interferograma. Puede observar cambios graduales a lo largo del tiempo. También puede ser útil para conjuntos de datos más antiguos que a veces tienen adquisiciones irregulares. El filtrado temporal y espacial puede ayudar a aumentar la precisión en la medición de deformaciones.

Debe elegir qué interferogramas utilizar, lo que a veces puede requerir algo de experimentación. La herramienta SBAS de Vertex simplifica esto al proporcionar una buena visualización y facilitar la determinación rápida de qué escenas usar.

Existen otros enfoques preferidos para entornos urbanos o necesidades de mayor resolución. Sin embargo, independientemente de tus necesidades de análisis, la herramienta SBAS es una herramienta de vista general útil y también se puede utilizar como un gráfico de línea de base 2-D. Proporciona una visualización completa pero rápida de las escenas.

Para obtener más información sobre la línea de base, incluidas descripciones de múltiples enfoques, puede consultar [aquí](https://www.sciencedirect.com/science/article/pii/S0924271615002415). También puede encontrar un estudio de caso de comparación entre PS y SBAS [aquí](https://ieeexplore.ieee.org/document/5692806).

## Cómo utilizar la Herramienta SBAS de Vertex
Visita **[Vertex de ASF](https://search.asf.alaska.edu)** para comenzar a usar la herramienta SBAS.
![type:video](https://www.youtube.com/embed/bQPdtuobdcg)

### **Comenzando tu Búsqueda SBAS**

- Si no tiene una escena de referencia específica elegida, puede buscar escenas utilizando la búsqueda geográfica o por lista. La columna central tendrá un botón en la metainformación titulado ***Herramienta SBAS*** para las escenas que sean elegibles. Puede hacer clic en este botón para dirigirte a una búsqueda SBAS. La búsqueda SBAS utilizará la escena elegida como referencia.

- Si tiene una escena de referencia específica elegida, puede seleccionar ***SBAS*** en la lista desplegable Tipo de Búsqueda. Puede ingresar tu escena de referencia y hacer clic en ***Buscar***.

### **Interactuando con los Resultados de la Búsqueda SBAS**
Mientras esté en el tipo de búsqueda SBAS, notarás muchos controles familiares en el panel de resultados. Los pares se muestran en la columna izquierda. La columna central lista la metainformación de los dos extremos del par seleccionado. El Gráfico SBAS se muestra en la columna derecha.

**Controles del Panel de Resultados**

- En la parte superior izquierda del panel de resultados, verás el número de pares listados.
- **Ampliar** permitirá *Ampliar los resultados*, aumentando la área del mapa de la Tierra donde se encuentran las escenas.
- **Lista** permitirá *Agregar todo a Descargas*, lo que te permite agregar todas las escenas a la lista de descargas.
- **On Demand** te permitirá *Agregar todo a la lista On Demand* para realizar un procesamiento personalizado en las escenas. También puede optar por *Crear Suscripción*.
	- Puede elegir entre **RTC GAMMA**, **InSAR GAMMA** o **autoRIFT**, dependiendo de tus necesidades. El procesamiento RTC GAMMA se realiza en las escenas individuales de tu conjunto de resultados. El procesamiento InSAR GAMMA y autoRIFT se realiza en los pares de tu conjunto de resultados.
	- **Nota:** Actualmente, solo las escenas con modo de haz IW son elegibles para el procesamiento On Demand.
- **Pares** te permitirá *Descargar el par CSV*, que lista las escenas en cada par y la URL de descarga para cada una. También incluye los valores de la línea de base.
- En la columna izquierda, resalta el par deseado y haga clic en el ícono **On Demand** para *Agregar el par a la lista On Demand*. Puede elegir el procesamiento *InSAR GAMMA* o *autoRIFT* para cada par que desees agregar.

**Controles del Gráfico**

- Los puntos en el gráfico representan escenas individuales. Al pasar el cursor sobre ellos, se mostrará tu información temporal y perpendicular. Las líneas representan los pares.
- Puede utilizar el ratón para navegar por el gráfico. Hay botones de **Ampliar** y **Reducir** ubicados encima del gráfico. El botón **Ajustar al Tamaño** ajustará todos los pares en el gráfico visible.
- Puede hacer clic en cualquier línea de par en el gráfico. Cuando lo hagas, el par seleccionado se resaltará en rojo y se mostrará la metainformación de ese par en la columna central.
- Puede ajustar la línea de base temporal y perpendicular utilizando los controles deslizantes en el gráfico.
- También puede crear tu propio par si lo desea:
	1. Bajo **Par Personalizado**, haga clic en el **símbolo de más** para *Comenzar a agregar un par personalizado*.
	7. Haga clic en el punto en el gráfico que representa la primera escena.
	2. Haga clic en el punto en el gráfico que representa la segunda escena.
	3. Se creará el nuevo par y se añadirá el detalle del par en la parte inferior de la lista de resultados. Los pares añadidos manualmente se mostrarán con una línea punteada en el gráfico.
	4. **Nota:** También puede agregar pares personalizados a la lista On Demand.
- Si desea dejar de agregar un par después de haber comenzado, puede hacer clic en el **símbolo cuadrado** para *Dejar de agregar un par personalizado*. Ten en cuenta que solo se pueden eliminar los pares añadidos manualmente.

#### Mensaje de Advertencia sobre Detección de Brechas

Si se detectan brechas en tus pares SBAS, se mostrará un mensaje de advertencia. Se recomienda evitar las redes de pares InSAR desconectadas. Las redes de pares desconectadas dificultan la creación de estimaciones imparciales de las velocidades InSAR en un análisis de series temporales.

Si desea eliminar las brechas, puede modificar tus filtros de búsqueda, como aumentar la línea de base temporal hasta que todas las escenas estén conectadas. También puede agregar pares manuales para las conexiones faltantes. Una vez que todas las escenas tengan al menos una conexión, el mensaje de advertencia desaparecerá.

#### Criterios de SBAS

- Haga clic en **Criterios de SBAS...** para obtener opciones de filtrado adicionales.
	- Puede ingresar una fecha de **Inicio** o **Fin**, o seleccionar fechas en el calendario.
	- **Búsqueda Estacional** permite limitar los resultados a ciertos períodos anuales dentro de un rango general de fechas. Haga clic en el interruptor de Búsqueda Estacional y aparecerán opciones adicionales, lo que te permitirá ajustar los controles deslizantes para especificar un rango estacional (*Día de Inicio de la Temporada/Día de Finalización de la Temporada*).
	- **Superposición Latitudinal** te permite establecer el umbral de superposición para los pares. Filtrar los pares que no se superponen puede reducir errores en el procesamiento InSAR On Demand.
		- **Sin Umbral de Superposición** es el valor predeterminado. Se devuelven todos los resultados de pares, incluidos los que no se superponen.
		- **Cualquier Umbral de Superposición** asegurará que todos los pares tengan cierta superposición. Los pares sin superposición se filtrarán de los resultados.
		- **Umbral de Superposición del 50%** garantiza que todos los pares tengan aproximadamente un 50% de superposición. Los pares con menos superposición se filtrarán de los resultados.

## Siguientes Pasos
El siguiente paso es crear interferogramas. Puede hacerlo a través del procesamiento On Demand en Vertex. Primero, debe agregar algunos o todos los pares a la lista On Demand como trabajos InSAR. En la lista , hay opciones limitadas disponibles para personalizar tu procesamiento InSAR. También puede especificar un nombre de proyecto. Envía la lista  cuando hayas seleccionado todas las opciones deseadas. Cuando los interferogramas estén completos, Podrá verlos y descargarlos utilizando el tipo de búsqueda de Productos On Demand en Vertex.

Para áreas con hielo glaciar, autoRIFT es otra opción de procesamiento. Similar a InSAR, debe agregar algunos o todos los pares a la lista On Demand como trabajos autoRIFT. No hay opciones de personalización adicionales disponibles para el procesamiento autoRIFT, pero aún puede especificar un nombre de proyecto. Cuando se complete el procesamiento autoRIFT, Podrá ver y descargar los productos utilizando el tipo de búsqueda de Productos On Demand en Vertex.

Puede encontrar más detalles en la [Guía del Usuario de Vertex](/vertex/manual). También hay documentación de ayuda, incluidos videos, disponible en Vertex [aquí](https://search.asf.alaska.edu/#/?maxResults=250&topic=onDemand).

Para obtener más información, también puede consultar la [documentación de On Demand](https://hyp3-docs.asf.alaska.edu/).
