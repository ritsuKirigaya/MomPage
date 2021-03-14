from pathlib import Path
import connection
import route.requirements as routes
app = connection.app
db = Path("./model/metadata.txt").read_text().split("\n")
pack = {}
pack = {i.split(":=:")[0].strip(): i.split(":=:")[1].strip() for i in db if (len(i.split(":=:")) > 1 and (i.split(":=:")[0].strip().lower() == "author" or i.split(":=:")[0].strip().lower() == "description") and not (i.split(":=:")[0].strip() in pack.keys()))}
#@app.context_processor
#def get_components():
#    from flask import render_template_string
#    return dict(headerCss=headerData[0], headerBody=headerData[1], footer=footerData)
@app.route('/')
def home():
    return routes.home(pack)
#@app.route('/<catalog>')
#def generatorIteamPage(catalog):
#    pack["catalog"] = catalog
#    return routers.catalogPage(pack)
#@app.route('/<catalog>/<product>')
#def generatorCatalog(catalog, product):
#    return routers.itemPage()

@app.route('/about')
def about():
    return routes.about()