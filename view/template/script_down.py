def Init():
    return("<script type='text/javascript' src='{{ url_for('static', filename='js/jquery-3.5.1.js') }}' ></script>"
        "<script type='text/javascript' src='{{ url_for('static', filename='js/jquery-3.5.1.min.js') }}' ></script>"
        "<script type='text/javascript' src='{{ url_for('static', filename='js/materialize.js') }}' ></script>"
        "<script type='text/javascript' src='{{ url_for('static', filename='js/materialize.min.js') }}' ></script>"
        "<script type='text/javascript' >"
        "$('.dropdown-button').dropdown({"
        "inDuration: 300,"
        "outDuration: 225,"
        "constrainWidth: false, "
        "hover: true, "
        "gutter: 0, "
        "belowOrigin: false, "
        "alignment: 'left',"
        "stopPropagation: false" 
        "}"
        ");"
        "$('.button-collapse').sideNav();"
        "$(document).ready(function(){"
        "$('.carousel').carousel();"
        "});"
        "$('.carousel.carousel-slider').carousel({"
        "fullWidth: true,"
        "indicators: true,"
        "duration: 200"
        "});"
        "$('.crd-hover').mouseover(function(){"
        "var target = $('.crd-hover .crd-scrollable');"
        "target.css('display', 'block');"
        "});"
        "$('.crd-hover').mouseout(function(){"
        "var target = $('.crd-hover .crd-scrollable');"
        "target.css('display', 'none');"
        "});"
        "autoplay();"
        "function autoplay(){"
        "$('.carousel').carousel('next');"
        "setTimeout(autoplay, 8000);"
        "}"
        "</script>")