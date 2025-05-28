# CDE Themed website

I think I ended up making a very simple static site generator. xslt stylsheets are used to create HTML file from source xml files. the xslt also imports a shared navbar.xml file to remove the dependency on JS.


XSLT templates are in `/src/templates`. All the XML and MD files are in `/src/content`. 

`make-website.sh` calls `gen-blog.sh`, which converts the markdown into xml, then creates the `index.html` page for the blog list. 

`gen-articles.py` converts all the xml files into html with xsltproc. ChatGPT made this script and is over complicated. One day I'll replace it with a shell script.

`gen-index.py` is currently a mess. The goal was to get an excerpt from each blog entry to have on the home page. It kind of works, but is very complicated. Also written by ChatGPT.
## TODO:  
- add google search bar on page somewhere
- finish blog articles
- ~~resize images so they take less space and the site loads faster. 115MB of images is kinda of overkill~~
