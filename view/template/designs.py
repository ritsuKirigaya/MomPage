def css():
    return ("<style type='text/css' >"
    ".row .col"
    "{"
    "padding: 0;"
    "}"
    f".fcrd_rack > div > div"
    "{"
    "width: 330px;"
    "min-width: 235px;"
    "display: flex !important;"
    "flex-direction: column;"
    "margin: 13px;"
    "}"
    f".fcrd_rack > div > div > div"
    "{"
    "width: 300px !important;"
    "}"
    f".fcrd_rack > div > div > div > h5"
    "{"
    "font-size: 1em;"
    "}"
    f".fcrd_rack > div > div > div > p"
    "{"
    "font-size: 0.8em;"
    "}"
    f".fcrd_rack > div > div img"
    "{"
    "margin: 0 !important;" 
    "width: 100% !important;"
    "height: 14em !important;"
    "}"
    "@media only screen and (min-width: 1200px){"
    ".fcrd"
    "{"
    "width: 100% !important;"
    "}"
    ".carousel"
    "{"
    "height: 37em !important;"
    "}"
    ".carousel .indicators .indicator-item"
    "{"
    "width: 0.53em;"
    "height: 0.53em;"
    "margin: 2.2vw 0.4vw;"
    "}"
    ".fcrd_rack > div > div > div {"
    "width: 24vw !important;"
    "}"
    #".fcrd_carousel"
    #"{"
    #"width: 100vw !important;"
    #"}"
    "}"
    "</style>")


def floating_card(img_url, title, content, className):
    return (f"<div class='container row white fcrd {className}' style='margin-top: 10px;' >"
        f"<img src='{img_url}' style='width: 10em; height: 10em; margin-top: 20px; margin-left: 10px; margin-bottom: 10px; margin-right: 0;' class='col' > "
        "<div class='container col s10 m9' style='margin: 15px;' >"
        f"<h5>{title}</h5>"
        f"<p>{content}</p>"
        "</div>"
        "</div>")

def floating_card_rack(img_url, title, content, className):
    return (f"<div class='fcrd_rack' style='display: flex !important; flex=direction: row; flex-wrap: wrap; justify-content: space-evenly;' >"
    "<div class='col s4' >" +
    floating_card(img_url[0] if len(img_url) > 0 else "", title[0] if len(title) > 0 else "", content[0] if len(content) > 0 else "", className) +
    "</div>"
    "<div class='col s4' >" +
    floating_card(img_url[1] if len(img_url) > 1 else "", title[1] if len(title) > 1 else "", content[1] if len(content) > 1 else "", className) +
    "</div>"
    "<div class='col s4' >" +
    floating_card(img_url[2] if len(img_url) > 2 else "", title[2] if len(title) > 2 else "", content[2] if len(content) > 2 else "", className) +
    "</div>"
    "</div>")

def carousel(img_url, title, content, className, count):
    covers = ""

    for y in range(count):
        covers += (f"<div class='carousel-item red white-text' href='#one!' style='background: url({img_url.pop(0)}) no-repeat; background-size: 100% 100%' >"
        f"<h2>{title.pop(0)}</h2>"
        f"<p class='white-text'>{content.pop(0)}</p>"
        "</div>")

    return (f"<div class='carousel carousel-slider center {className}' >"
    #"<div class='carousel-fixed-item center'>"
    #"<a class='btn waves-effect white grey-text darken-text-2'>button</a>"
    #"</div>"
    f"{covers}"
    "</div>")

def floating_card_carousel(img_url, title, content, className, count):
    return (f"<div class='container row white fcrd_carousel {className}' style='margin-top: 10px; width: 90% !important;' >"
    "<div style='width: 98% !important; margin-top: 20px; margin-left: 10px; margin-bottom: 10px; margin-right: 0;' class='col' > " +
    carousel(img_url, ["" for x in range(count)], ["" for x in range(count)], "", count) +
    "</div>"
    "<div class='container col s10 m9' style='margin: 15px;' >"
    f"<h5>{title}</h5>"
    f"<p>{content}</p>"
    "</div>"
    "</div>")

def floating_card_text(title, content, className):
    return (f"<div class='container row white {className}' style='margin-top: 20px; width: 98% !important; max-width: 98% !important;' >"
    "<div class='col s12' style='padding: 2vw;' >"
    f"<h4 style='font-family: rockwell;' >{title}</h4>"
    f"<p style='font-family: robotoSlab;' >{content}</p>"
    "</div>"
    "</div>")

def floating_card_hover(img_url, title, content):
    return ("<div class='row'>"
        "<div class='container col s3 offset-s1 crd-hover' >"
        f"<div class='col s12 red' style=\"background: url('{img_url}'); background-size: 100% 100%; height: 15vw;\" ></div>"
        "<div class='col s12 white crd-scrollable' style='display: none; padding-top: 0px; padding-bottom: 20px; opacity:0.65;' >" #onmouseover=\"this.style.display='block';\" onmouseout=\"this.style.display='none';\" >"
        f"<h4>{title}</h4>"
        f"<p style='font-size: 1vw;' >{content}</p>"
        "</div>"
        "</div>"
        "</div>")