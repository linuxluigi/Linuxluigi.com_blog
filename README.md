# Linuxluigi.com Blog

Using https://blog.getpelican.com

# Deploy

````bash
$ pelican content -o output -s pelicanconf.py
$ ghp-import output
$ git push origin gh-pages
````