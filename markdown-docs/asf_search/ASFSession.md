# ASFSession

## Description

This class extends `requests.session` to provide convenient ASF-specific authorization options. `ASFSession` is a subclass of `Session`. More information can be found [here](https://docs.python-requests.org/en/master/user/authentication/)

***

## Methods

### <span style="color: #236192; font-size: 20px;">auth_with_creds()</span>

Authenticates the session (self) using [Earthdata Login](https://urs.earthdata.nasa.gov/) username/password credentials.

**args:**

- username: [Earthdata Login](https://urs.earthdata.nasa.gov/) username
- password: [Earthdata Login](https://urs.earthdata.nasa.gov/) password

**returns:**

- returns self for convenience

***

### <span style="color: #236192; font-size: 20px;">auth_with_token()</span>

Authenticates the session (self) using an Earthdata Login `Authorization: Bearer` token.

**args:**

- token: Earthdata Login token for authenticated downloads, see [Earthdata Login Tokens](https://urs.earthdata.nasa.gov/user_tokens)

**returns:**

- returns self for convenience

***

### <span style="color: #236192; font-size: 20px;">auth_with_cookiejar()</span>

Authenticates the session (self) using a pre-existing cookiejar.

**args:**

- cookies: An `http.cookiejar` compatible object

**returns:**

- returns self for convenience
