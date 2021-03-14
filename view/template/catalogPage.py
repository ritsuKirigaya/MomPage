from flask import render_template_string
from view.template.builder import Builder
import view.template.header as header
import view.template.footer as footer
import view.template.designs as designs

class CatalogPage:
    def __init__(self, pack,title):
        self.name = title
        self.attsHead = {"title": "Welcome Home", "m-charset": "utf-8", "m-author": "Rojas Justiniano Diego",
         "m-description": "Cosmetic Store", "m-viewport": "width=device-width, initial-scale=1.0"}
    
    def head(self):
         return ("<head>"
        "<title>" + self.attsHead["title"] + "</title>"
        "<meta charset='" + self.attsHead["m-charset"] + "' >"
        "<meta name='author' content='" + self.attsHead["m-author"] + "' >"
        "<meta name='description' content='" + self.attsHead["m-description"] + "' >"
        "<meta name='viewport' content='" + self.attsHead["m-viewport"] + "' >" 
        f"{header.initHead()}"
        "</head>")
    def body(self):
        return ("<body>"
        f"{header.body()}"
        f"{designs.floating_card_text(self.name, "", "")}"
        #
        "</body")
    
    def footer(self):
        return ("<footer>"
        f"{footer.init()}"
        "</footer>")

    def execute(self):
        result = "<html>" + self.head() + self.body() + self.footer() + "</html>"
        return render_template_string(result)


