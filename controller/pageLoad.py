import base64
aa = base64.b64encode(bytes('your string', 'utf-8'))
def CatalogLoad(encodedName):
    from pathlib import Path
    db_local_data = Path("./model/datafont.txt").read_text().split("\n")
    data = {}
    def options(value):
        if value == "page-catalog":
            return 0
        elif value == "page-item":
            return 1
        else:
            return -1
    z= -1
    for x in db_local_data:
        if z == -1:
            ind = x.find("{")
            if ind >= 0:
                z = options(x[0:ind].strip())

        else:
            ind = x.find("}")
            if ind >= 0:
                y = x[ind:].strip()
                ind = y.find("{")
                if ind >= 0:
                    z = options(y[0:ind])
                else:
                    z = -1
            else:
                if z == 0:
                    y = x.split(":=:")
                    if len(y) > 1:
                        if y[0].strip().lower() == "name":
                            data["name"] = y[1].strip()
                        elif y[0].strip().lower() == "title":
                            data["title"] = y[1].strip()
                #elif z == 1:
                    #
