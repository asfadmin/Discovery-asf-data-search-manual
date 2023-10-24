 ## Visión general
La teledetección por radar se ha convertido en una fuente de datos muy importante en las Geociencias. Esto se debe principalmente a la capacidad del radar para penetrar en las nubes y operar independientemente de la iluminación solar. Además, los sensores de radar se benefician de su capacidad para identificar fácilmente los cambios, rastrear la deformación de la superficie con precisión de cm y mapear grandes áreas regularmente y en escalas de tiempo largas. No es sorprendente que la teledetección por radar se utilice regularmente para estudiar terremotos, volcanes y glaciares, así como para el monitoreo de actividades antropogénicas como la extracción de hidrocarburos y el bombeo de agua subterránea.

Dentro del proyecto SARVIEWS, estamos trabajando en el aprovechamiento de las capacidades de SAR mediante el desarrollo de un sistema de procesamiento totalmente automático que produce productos de valor agregado en apoyo del monitoreo de desastres naturales. El procesador SARVIEWS se implementa en la nube de Amazon y utiliza tecnología de procesamiento moderna para generar series temporales de imágenes geocodificadas y totalmente corregidas por el terreno, así como datos SAR interferométricos sobre áreas afectadas por desastres naturales. Para facilitar la automatización completa, el flujo de procesamiento SARVIEWS se activa automáticamente mediante los sistemas de alerta de peligro existentes, como el [Servicio de notificación de terremotos del USGS] (https://earthquake.usgs.gov/ens/). Actualmente, SARVIEWS está apoyando los peligros relacionados con erupciones volcánicas y terremotos. La inclusión de eventos de inundación está en preparación.

## Criterios de monitoreo de peligros

Las suscripciones SARVIEWS se crean casi en tiempo real en función de los informes de organizaciones de monitoreo como el USGS y el Programa de Vulcanismo Global de la Institución Smithsonian. Las suscripciones se crean automáticamente después de revisar los correos electrónicos del [Servicio de Notificación de Terremotos (ENS)](https://earthquake.usgs.gov/ens/) y los correos electrónicos del [Servicio de Notificación de Volcanes (VNS)](https://volcanoes.usgs.gov/vns2/), o las actualizaciones semanales del Programa de Vulcanismo Global del Instituto Smithsonian para volcanes activos fuera de los Estados Unidos.

### Terremotos

Las suscripciones de terremoto se crean si el evento de terremoto tiene una deformación superficial potencial, que se evalúa aproximadamente en función de la siguiente lógica:

<Tabla>
  <Cabeza>
    <tr>
      <th>Magnitud</th>
      <th>Poca profundidad: 0-35 km</th>
      <ª>Media: 35-100 km</th>
      <th>Profundidad: 100+ km</th>
    </tr>
  </cabeza>
  <Cuerpo>
    <tr>
      <td>Large: Mag 7.5+</td>
      <td>Sí</td>
      <td>Sí</td>
      <td>Sí</td>
    </tr>
    <tr>
      <td>Medio: Mag 7.0 - 7.5</td>
      <td>Si se encuentra a menos de 75 km de la costa</td>
      <td>Si se encuentra a menos de 25 km de la costa</td>
      <td>No</td>
    </tr>
    <tr>
      <td>Small: Mag 6.0 - 7.0</td>
      <td>Si se encuentra a menos de 25 km de la costa</td>
      <td>Si se encuentra a menos de 0.5 km de la costa</td>
      <td>No</td>
    </tr>
  </cuerpo>
</tabla>

Estos criterios proporcionan una estimación rápida de la fuerza del terremoto en relación con la profundidad y la distancia de la tierra para limitar las suscripciones a eventos solo a aquellos con el potencial de deformación superficial. Esta lógica simple se crea en el correo electrónico de ENS, y no espera más datos para calcular la deformación superficial con métodos sismológicos convencionales. Una vez creadas, las suscripciones de terremotos procesan los datos de Sentinel durante 6 meses a partir de la fecha del terremoto.

### Volcanes

Los criterios para las suscripciones a volcanes responden en los correos electrónicos del Aviso de actividad de VNS para volcanes nacionales y en la fuente RSS del Programa de Vulcanismo Global del Smithsonian Institution para volcanes internacionales. Si un volcán se marca como un nivel de alerta de advertencia o un código de aviación RED, se crea una suscripción para el volcán. A nivel mundial, si la actividad del volcán es lo suficientemente alta como para ser activada y publicada por el Programa Global de Vulcanismo, SARVIEWS crea una suscripción. Las suscripciones de Volcano procesan datos a partir de 1 año antes de la actividad y continúan indefinidamente hasta que los niveles de actividad del volcán vuelvan a la normalidad.

## Procesamiento bajo demanda

El procesador SARVIEWS aprovecha al máximo los extensos archivos SAR disponibles en Alaska Satellite Facility (ASF), NASA Distributed Active Archive Center (DAAC) para datos de radar de apertura sintética. A través de ASF, SARVIEWS tiene acceso eficiente a las adquisiciones históricas y futuras de los sensores Sentinel-1, un sistema SAR espacial lanzado y operado por la Agencia Espacial Europea. Sentinel-1 toma imágenes de todas las masas terrestres de la Tierra cada 6 a 12 días, proporcionando datos valiosos para el monitoreo de peligros.

Para acceder y procesar de manera eficiente el flujo entrante de datos SAR de Sentinel-1, SARVIEWS aprovecha ASF HyP3, un sistema de procesamiento basado en la nube que genera productos SAR de valor agregado bajo demanda. El procesamiento bajo demanda a través de HyP3 también está disponible en [ASF's Vertex](https://search.asf.alaska.edu/#/?topic=onDemand). A través de HyP3, SARVIEWS tiene acceso completo a los beneficios de la nube, como el escalado elástico de los recursos informáticos y el almacenamiento y la distribución eficientes basados en la nube. Para obtener más información, visite la [Documentación de HyP3](https://hyp3-docs.asf.alaska.edu/).

## Preguntas frecuentes

**¿SARVIEWS es gratis?**

Todos los productos SARVIEWS disponibles en Vertex están disponibles gratuitamente para su descarga y uso sin restricciones. Estos son productos de valor agregado creados a partir de datos de Sentinel-1 disponibles gratuitamente, sin necesidad de iniciar sesión. Por favor, acredite tanto a ESA como a SARVIEWS cuando utilice nuestros datos.

**¿Cómo puedo descargar productos de forma masiva?**

Cuando elija copiar las URL de cualquier producto de evento, obtendrá una lista de enlaces a todos los productos SARVIEWS seleccionados. Puede pegar estos vínculos en un archivo, como un .csv. Para descargar los productos, utilice un programa como wget con la opción '-i'. Por ejemplo:

    ## Mover a la ubicación donde desea que se descarguen los productos
    Ruta de acceso del CD/hasta/destino

    ## Descargar con la opción -i para especificar el .csv
    wget -i path/to/download_all.csv

También puede descargar y ejecutar el script de descarga masiva de Python para descargar los productos de eventos seleccionados.

**¿Cuándo estará disponible el próximo producto?**

SARVIEWS crea y archiva automáticamente los productos tan pronto como están disponibles. Si falta un producto para una suscripción, significa que la suscripción está esperando que se adquiera una nueva escena o que todavía se está procesando. En general, hay 12 días entre la mayoría de los pasos elevados de Sentinel.

**¿Qué software se utiliza para procesar los datos SARVIEWS?**

Los eventos SARVIEWS se procesan utilizando herramientas de software [GAMMA Remote Sensing](https://www.gamma-rs.ch/software) a través del motor ASF HyP3. Para obtener más información sobre los detalles del algoritmo, visite la [página de productos ASF HyP3](https://hyp3-docs.asf.alaska.edu/products/).

## Agradecimientos y Contacto

El esfuerzo SARVIEWS fue financiado por el [Programa de Desastres de Ciencias Aplicadas de la NASA] (https://appliedsciences.nasa.gov/what-we-do/disasters) a través de subvenciones NNX12AQ38G. Los datos de Sentinel-1 son proporcionados por la Agencia Espacial Europea a través de su programa [Copernicus](https://www.esa.int/Applications/Observing_the_Earth/Copernicus). El acceso a los datos de Sentinel-1 es proporcionado por la [NASA Alaska Satellite Facility (ASF) DAAC](https://asf.alaska.edu/). Los productos SARVIEWS contienen datos modificados de Copernicus Sentinel. Las contribuciones a SARVIEWS fueron hechas por el equipo del proyecto SARVIEWS, incluidos FJ Meyer, S Arko, JB Nicoll, K Hogenson, W Gong, DB McAlpin, P Webley y muchos más. Debemos agradecer a los equipos ASF Advanced Prototype Development (APD) y ASF HyP3 por apoyar la sólida implementación de los procedimientos SARVIEWS y por su asistencia para mover SARVIEWS a la nube. Los muchos beta-testers de nuestro servicio están haciendo contribuciones continuas.

Para obtener más información sobre SARVIEWS, póngase en contacto con [Franz Meyer](mailto:fjmeyer@alaska.edu]. También puede ver la cuenta de [Twitter](https://twitter.com/SARevangelist?).

## Enlaces útiles

- Clase de teledetección por microondas de la Universidad de Alaska Fairbanks (UAF): [UAF GEOS 657](https://radar.community.uaf.edu/)
- Servicio genérico de corrección atmosférica en línea de la Universidad de Newcastle para InSAR: [GACOS](http://www.gacos.net/)
- El Centro Aeroespacial Alemán (DLR) para información de crisis basada en satélite: [DLR ZKI](https://www.dlr.de/eoc/desktopdefault.aspx/tabid-12797#gallery/36755)
- Centro de Peligros Naturales del Laboratorio de Propulsión a Chorro del Laboratorio de Propulsión Rápida Avanzada (ARIA) de la NASA: [JPL ARIA](https://aria.jpl.nasa.gov/)
- Servicio de Gestión de Emergencias Copernicus de la ESA: [Copernicus EMS](https://emergency.copernicus.eu/)
- El Centro de Observación y Modelización de Terremotos, Volcanes y Tectónica: [COMET InSAR](https://comet.nerc.ac.uk/earth-observation/insar/)
- Plataformas de explotación temática de la ESA: [TEPs de la ESA](https://tep.eo.esa.int/home)

