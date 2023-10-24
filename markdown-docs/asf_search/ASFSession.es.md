 #SesiónASF

## Descripción

Esta clase extiende 'requests.session' para proporcionar opciones de autorización específicas de ASF. 'ASFSession' es una subclase de 'Session'. Más información se puede encontrar [aquí](https://docs.python-requests.org/en/master/user/authentication/)



## Métodos

### <span style="color: #236192; tamaño de fuente: 20px;" >auth_with_creds()</span>

Autentica la sesión (self) utilizando las credenciales de nombre de usuario/contraseña de [Earthdata Login](https://urs.earthdata.nasa.gov/).

**args:**

- nombre de usuario: [Earthdata Login](https://urs.earthdata.nasa.gov/) nombre de usuario
- contraseña: [Earthdata Login](https://urs.earthdata.nasa.gov/) contraseña

**Devuelve:**

- Devuelve auto para mayor comodidad



### <span style="color: #236192; tamaño de fuente: 20px;" >auth_with_token()</span>

Autentica la sesión (self) utilizando un token 'Authorization: Bearer' de inicio de sesión de Earthdata.

**args:**

- token: token de inicio de sesión de Earthdata para descargas autenticadas, consulte [Earthdata Login Tokens](https://urs.earthdata.nasa.gov/user_tokens)

**Devuelve:**

- Devuelve auto para mayor comodidad



### <span style="color: #236192; tamaño de fuente: 20px;" >auth_with_cookiejar()</span>

Autentica la sesión (self) utilizando un cookiejar preexistente.

**args:**

- cookies: Un objeto compatible con 'http.cookiejar'

**Devuelve:**

- Devuelve auto para mayor comodidad
