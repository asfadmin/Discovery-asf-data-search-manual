# ASFSession

## Description

This class describes session authorization options.

***

## Methods

### <span style="color: #236192; font-size: 20px;">auth_with_creds()</span>

Authenticates the session using EDL username/password credentials.

**args:**

- username: [EDL](https://urs.earthdata.nasa.gov/) username
- password: [EDL](https://urs.earthdata.nasa.gov/) password

**returns:** returns self for convenience

***

### <span style="color: #236192; font-size: 20px;">auth_with_token()</span>

Authenticates the session using an EDL Authorization: Bearer token

**args:**
token: EDL Auth Token for authenticated downloads, see [EDL Tokens](https://urs.earthdata.nasa.gov/user_tokens)

**returns:** returns self for convenience

***

### <span style="color: #236192; font-size: 20px;">auth_with_cookiejar()</span>

Authenticates the session using a pre-existing cookiejar

**args:**
cookies: Any http.cookiejar compatible object

**returns:** returns self for convenience
