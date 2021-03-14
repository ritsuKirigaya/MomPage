def home(pack):
    from view.home import Home
    return Home(pack).execute()

def about():
    return "estas en about"

#def itemPage(pack):
#    from flask import render_template
#    return render_template("itemPage.html", pack=pack)
#
#def catalogPage(pack):
    #