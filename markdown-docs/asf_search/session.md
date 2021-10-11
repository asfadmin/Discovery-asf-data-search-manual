# ASFSession Class

### auth_with_creds

Authenticates the session using EDL username/password credentials.

#### Parameters
- param username: [EDL](https://urs.earthdata.nasa.gov/) username
- param password: [EDL](https://urs.earthdata.nasa.gov/) password

#### Return
- returns self for convenience

### auth_with_token

Authenticates the session using an EDL Authorization: Bearer token

#### Parameters
- param token: EDL Auth Token for authenticated downloads, see [EDL Tokens](https://urs.earthdata.nasa.gov/user_tokens)

#### Return
- returns self for convenience

### auth_with_cookiejar

Authenticates the session using a pre-existing cookiejar

#### Parameters
- param cookies: Any http.cookiejar compatible object

#### Return
- returns self for convenience
