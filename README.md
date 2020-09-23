# ASF Data Search Manual
Documentation for ASF Search applications is built using MkDocs,
[mkdocs.org](https://www.mkdocs.org/#mkdocs).

### Developing Documentation
MkDocs comes with a built-in dev-server that lets you preview
your documentation as you work on it. Make sure you're in the
same directory as the mkdocs.yml configuration file, and then
start the server by running the `mkdocs serve` command:

>`$ mkdocs serve`  
`INFO    -  Building documentation...`  
`INFO    -  Cleaning site directory`  
`[I 160402 15:50:43 server:271] Serving on http://127.0.0.1:8000`    
`[I 160402 15:50:43 handlers:58] Start watching changes`  
`[I 160402 15:50:43 handlers:60] Start detecting changes`  

Open up `http://127.0.0.1:8000/` in your browser, and you'll see the
default home page for the documentation.

### Building The Site

`mkdocs build --clean`

This command will build documentation as an html website within the 'site'
directory.

After some time, files may be removed from the documentation but they will
still reside in the site directory. That is why the --clean switch is used.
It will erase the old files from the site directory.

The .gitignore file lists the MkDocs site directory so the generated site files
are not stored in the repository. The site directory should be built dynamically
as part of the merge process in github.

### Deploying The Site

Merge to the branches: prod, test, and dev triggers an appropriate
AWS CodeBuild process creating the site in an S3 bucket.
The S3 bucket is then accessible via CloudFront. Since CloudFront doesn't automatically
redirect to index.html when supplied with a path, a Lambda function handles the
redirect.




