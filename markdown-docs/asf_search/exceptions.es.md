# Excepciones

**ASFError(Excepción):**

- Excepción ASF base, no destinada al uso directo

**ASFSearchError(ASFError):**

- Excepción relacionada con la búsqueda base

**ASFSearch4xxError(ASFSearchError):**

- Aumentar cuando SearchAPI devuelve un error 4xx 

**ASFSearch5xxError(ASFSearchError):**

- Aumentar cuando SearchAPI devuelve un error 5xx 

**ASFServerError(ASFSearchError):**

- Aumentar cuando SearchAPI devuelve un error desconocido

**ASFBaselineError(ASFSearchError):**

- Aumentar cuando se producen errores relacionados con la línea de base 

**ASFDownloadError(ASFError):**

- Excepción relacionada con la descarga base 

**ASFAuthenticationError(ASFError):**

- Excepción relacionada con la descarga base