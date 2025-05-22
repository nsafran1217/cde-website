# This Website's Design
*Published: 22-May-2025 - Last Updated: 22-May-2025*

When I originally made a website, I used Publii, which is a WSYIWYG static site generator. Publii worked good, but I wanted a bit more control over the layout and organization of the site.

[cosam.org](http://www.cosam.org/) was my inspiration for the layout of the site, with a sidebar that changed depending on the page.  
[4dwm.com](https://www.4dwm.com/) inspired me to make the site look like a CDE/HP VUE/4DWM desktop. 

This ended up being a lot of work since I have no experience with web design, except for one class I took in 10th grade making websites in Adobe Dreamweaver CS3 (which was very outdated by then).
Orignally, it was going to look much closer to cosam.org with a simpler theme. I was planning on using [https://simplecss.org/](https://simplecss.org/) for the styling, but ended up just making my own.  

I had a few goals for the site: Make it static, so I can host it on GitHub Pages, no Javascript so older browsers can at least load the site, and for it to be somewhat easy to update with new content.
<a href="https://github.com/nsafran1217/cde-website">GitHub for the website "source"</a>

The first draft of the site was all HTML with a small amount of Javascript to load the navbar on each page, but that didn't meet my goal for no JS. I then came across xslt, which allows you to use a template file to convert an XML file into an HTML file.

With some help from ChatGPT, I started tweaking the template to insert the navbar template on each site. The xslt template also let me generate multiple "Windows" on the site relatively easily. 
