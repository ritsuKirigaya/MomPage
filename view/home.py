from flask import render_template_string
#from pathlib import Path
from controller.builder import Builder
import view.template.header as header
import view.template.footer as footer
class Home:
    def __init__(self, pack):
        self.name = "home"
        self.attsHead = {"title": "Welcome Home", "m-charset": "utf-8", "m-author": f"{pack['author']}",
         "m-description": f"{pack['description']}", "m-viewport": "width=device-width, initial-scale=1.0"}
        

    def head(self):
        return ("<head>"
        "<title>" + self.attsHead["title"] + "</title>"
        "<meta charset='" + self.attsHead["m-charset"] + "' >"
        f"<meta name='author' content='{self.attsHead['m-author']}' >"
        "<meta name='description' content='" + self.attsHead["m-description"] + "' >"
        "<meta name='viewport' content='" + self.attsHead["m-viewport"] + "' >" 
        f"{header.initHead()}"
        "</head>")
    
    def body(self):
        return ("<body>"
        f"{header.body()}"
        #"<img src='https://www.viatrading.com/sku/COVER/wholesale-assorted-case-packs-of-new-overstock-cover-girl-cosmetics-16.jpeg' style='width: 100% !important; height: 400px;' >"
        f"{Builder(self.name).execute()}"
        "</body>")

    def footer(self):
        return ("<footer>"
        f"{footer.init()}"
        "</footer>")

    def execute(self):
        result = "<html>" + self.head() + self.body() + self.footer() + "</html>"
        return render_template_string(result)