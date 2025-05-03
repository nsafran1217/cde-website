# CDE Themed website

I think I ended up making a very simple static site generator. xslt stylsheets are used to create HTML file from source xml files. the xslt also imports a shared navbar.xml file to remove the dependency on JS.

`gen-index.py` creats the `index.html` homepage, as well as searching in the blog directory for all entries. It adds the 5 most recent to `blogspotlight.xml` which is then included in index.html. It also generates `blog/index.xml` with a list  of all blog entries.

`gen-articles.py` searches the entire working directory for xml files and generates the html for them in the OUTPUT dir, with the same structre.



## TODO:  
- add google search bar on page somewhere
- finish blog articles
- resize images so they take less space and the site loads faster. 115MB of images is kinda of overkill
- 
