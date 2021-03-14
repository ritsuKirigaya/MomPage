from flask import render_template_string
from view.template.builder import Builder
import view.template.header as header
import view.template.footer as footer

class ItemPage:
    def __init__(self):
        self.name = "home"
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
        "<div class='row white' style='margin-bottom: 0px;' >"
        "<div class='col s6' style=\"background: url('https://www.viatrading.com/sku/COVER/wholesale-assorted-case-packs-of-new-overstock-cover-girl-cosmetics-16.jpeg'); background-size: 100% 100%; height: 30em;\" >"
        "</div>"
        "<div class='container col s5' style='height: 30em; margin-left: 2vw;' >"
        "<h4>Hola mundo</h4>"
        "<p>Como esta mi gente!! Como esta mi gente!! Como esta mi gente!!"
        "Como esta mi gente!! Como esta mi gente!! Como esta mi gente!!"
        "Como esta mi gente!! Como esta mi gente!! Como esta mi gente!!"
        "Como esta mi gente!! Como esta mi gente!! Como esta mi gente!!"
        "Como esta mi gente!! Como esta mi gente!! Como esta mi gente!!"
        "Como esta mi gente!! Como esta mi gente!! Como esta mi gente!!"
        "Como esta mi gente!! Como esta mi gente!! Como esta mi gente!!"
        "Como esta mi gente!! Como esta mi gente!! Como esta mi gente!!"
        "Como esta mi gente!! Como esta mi gente!! Como esta mi gente!!</p>"
        "</div>"
        "</div>"
        "</body")
    
    def footer(self):
        return ("<footer>"
        f"{footer.init()}"
        "</footer>")

    def execute(self):
        result = "<html>" + self.head() + self.body() + self.footer() + "</html>"
        return render_template_string(result)



#<!DOCTYPE html>
#<html>
#    <head>
#        <title>{{ pack[0] }}</title>
#        <meta charset=" + self.attsHead[m-charset] + " >
#        <meta name="author" content="{{ author }}" >
#        <meta name="description" content=" {{ description }} " >
#        <meta name="viewport" content="width=device-width, initial-scale=1.0" >
#        {{header[0]}}
#    </head>
#    <body>
#    {{header[1]}}
#    </body>
#</html>