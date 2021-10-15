# Exceptions

**ASFError(Exception):**

- Base ASF Exception, not intended for direct use

**ASFSearchError(ASFError):**

- Base search-related Exception

**ASFSearch4xxError(ASFSearchError):**

- Raise when SearchAPI returns a 4xx error

**ASFSearch5xxError(ASFSearchError):**

- Raise when SearchAPI returns a 5xx error

**ASFServerError(ASFSearchError):**

- Raise when SearchAPI returns an unknown error

**ASFBaselineError(ASFSearchError):**

- Raise when baseline related errors occur

**ASFDownloadError(ASFError):**

- Base download-related Exception

**ASFAuthenticationError(ASFError):**

- Base download-related Exception