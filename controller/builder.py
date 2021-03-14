from pathlib import Path
import math
import view.template.designs as designs

class Builder:
    def __init__(self, name):
        db_local_data = Path("./model/datafont.txt").read_text().split("\n")
        def design_type(data):
            if data == f"{name}-fcrd":
                return 0
            elif data == f"{name}-fcrd-rack":
                return 1
            elif data  == f"{name}-carousel":
                return 2
            elif data == f"{name}-fcrd-carousel":
                return 3
            elif data == f"{name}-fcrd-text":
                return 4
            else:
                return -1
        self.order = []
        self.fcrd_title = []
        self.fcrd_url = []
        self.fcrd_content = []
        self.fcrd_count = []
        self.fcrd_className = []
        self.carousel_url = []
        self.carousel_className = []
        self.carousel_title = []
        self.carousel_content = []
        self.carousel_count = []
        y = -1
        count = []
        elements = []
        for x in db_local_data:
            ind = x.find('{')
            if  y == -1 and ind >= 0:
                y = design_type(x[0:ind].strip())
            elif y >= 0:
                ind = x.find('}')
                if ind >= 0:
                    countAux = count.copy()
                    countAux.sort()
                    if len(countAux) > 0:
                        if y == 0:
                            self.fcrd_title.extend(elements[0][: countAux[0]])
                            self.fcrd_url.extend(elements[1][: countAux[0]])
                            self.fcrd_content.extend(elements[2][: countAux[0]])
                            self.fcrd_className.extend(elements[3][: countAux[0]])
                            self.fcrd_count.append(countAux[0])
                            self.order.append(y)
                        elif y == 1:
                            numMath = math.floor(countAux[1] / 3)
                            self.fcrd_title.extend(elements[0][: numMath * 3])
                            self.fcrd_url.extend(elements[1][: numMath * 3])
                            self.fcrd_content.extend(elements[2][: numMath * 3])
                            self.fcrd_className.append(elements[3][0])
                            self.fcrd_count.append(numMath)
                            self.order.append(y)
                        elif y == 2:
                            self.carousel_url.extend(elements[0][: countAux[1]])
                            self.carousel_className.append(elements[1][0])
                            self.carousel_title.extend(elements[2][: countAux[1]])
                            self.carousel_content.extend(elements[3][: countAux[1]])
                            self.carousel_count.append(countAux[1])
                            self.order.append(y)
                        elif y == 3:
                            self.carousel_url.extend(elements[0][: countAux[-1]])
                            self.carousel_className.append(elements[1][0])
                            self.carousel_title.append(elements[2][0])
                            self.carousel_content.append(elements[3][0])
                            self.carousel_count.append(countAux[-1])
                            self.order.append(y)
                        elif y == 4:
                            self.fcrd_title.extend(elements[0][: countAux[1]])
                            self.fcrd_content.extend(elements[2][: countAux[1]])
                            self.fcrd_className.extend(elements[3][: countAux[1]])
                            self.fcrd_count.append(countAux[1])
                            self.order.append(y)
                        
                        elements = []
                        count = []
                        y = design_type(x[ind:].strip())
                        if y > -1:
                            ind = x[ind:].strip().find("{")
                            if ind < 0:
                                y = -1
                else:
                    z = x.split(":=:")
                    if y == 0 or y == 1 or y == 4:    #use commands title, url, content, className
                        if len(count) == 0:
                            count = [0 for x in range(4)]
                            elements = [[] for x in range(4)]
                        if z[0].strip() == "title":
                            elements[0].append(z[1].strip())
                            #self.fcrd_title.append(z[1].strip())
                            count[0] += 1
                        elif z[0].strip() == "url" and y != 4:
                            elements[1].append(z[1].strip())
                            #self.fcrd_url.append(z[1].strip())
                            count[1] += 1
                        elif z[0].strip() == "content":
                            elements[2].append(z[1].strip())
                            #self.fcrd_content.append(z[1].strip())
                            count[2] += 1
                        elif z[0].strip() == "className":
                            if y == 1 and count[3] > 0:
                                    elements[3][len(elements[3]) - 1] = z[1].strip()#.replace(" ", "_")
                                    #self.fcrd_className[len(self.fcrd_className) - 1] = z[1].strip()#.replace(" ", "_")

                            else:
                                elements[3].append(z[1].strip())
                                #self.fcrd_className.append(z[1].strip())
                                count[3] += 1
                    elif y == 2 or y == 3: 
                        if len(count) == 0:     # 1. url, 2. className, 3. title, 4. content
                            count = [0 for x in range(4)]
                            elements = [[] for x in range(4)]
                        if z[0].strip() == "url":
                            elements[0].append(z[1].strip())
                            #self.carousel_url.append(z[1].strip())
                            count[0] += 1
                        elif z[0].strip() == "className":
                            if count[1] > 0:
                                elements[1][len(elements[1]) - 1] = z[1].strip()#.replace(" ", "_")
                                #self.carousel_className[len(self.carousel_className) - 1] = z[1].strip()#.replace(" ", "_")
                            else:
                                elements[1].append(z[1].strip())
                                #self.carousel_className.append(z[1].strip())
                                count[1] += 1
                        elif z[0].strip() == "title":
                            if y == 3 and count[2] > 0:
                                elements[2][len(elements[2]) - 1] = z[1].strip()
                                #self.carousel_title[len(self.carousel_title) - 1] = z[1].strip()
                            else:
                                elements[2].append(z[1].strip())
                                #self.carousel_title.append(z[1].strip())
                                count[2] += 1
                        elif z[0].strip() == "content":
                            if y == 3 and count[3] > 0:
                                elements[3][len(elements[3]) - 1] = z[1].strip()
                                #self.carousel_content[len(self.carousel_content) - 1]
                            else:
                                elements[3].append(z[1].strip())
                                #self.carousel_content.append(z[1].strip())
                                count[3] += 1

    def execute(self):
        body= "" + designs.css()
        i = 0
        if len(self.order) > 0:
            for x in self.order:
                if x == 0:
                    if len(self.fcrd_count) > 0:
                        if self.fcrd_count[0] > 0:
                            for y in range(self.fcrd_count.pop(0)):
                                body += designs.floating_card(str(self.fcrd_url.pop(0) if (len(self.fcrd_url) > 0) else ""), str(self.fcrd_title.pop(0) if (len(self.fcrd_title) > 0) else ""), str(self.fcrd_content.pop(0) if (len(self.fcrd_content) > 0) else ""), str(self.fcrd_className.pop(0) if (len(self.fcrd_className) > 0) else ""))
                elif x == 1:
                    if len(self.fcrd_count) > 0:
                        for y in range(self.fcrd_count.pop(0)):
                            className = self.fcrd_className.pop(0)
                            url = [self.fcrd_url.pop(0) if len(self.fcrd_url) > 0 else "", self.fcrd_url.pop(0) if len(self.fcrd_url) > 0 else "", self.fcrd_url.pop(0) if len(self.fcrd_url) > 0 else ""]
                            title = [self.fcrd_title.pop(0) if len(self.fcrd_title) > 0 else "", self.fcrd_title.pop(0) if len(self.fcrd_title) > 0 else "", self.fcrd_title.pop(0) if len(self.fcrd_title) > 0 else ""]
                            content = [self.fcrd_content.pop(0) if len(self.fcrd_content) > 0 else "", self.fcrd_content.pop(0) if len(self.fcrd_content) > 0 else "", self.fcrd_content.pop(0) if len(self.fcrd_content) > 0 else ""]
                            body += designs.floating_card_rack(url, title, content, className)
                elif x == 2:
                    if len(self.carousel_count) > 0:
                        count = self.carousel_count.pop(0)
                        url = []
                        title = []
                        content = []
                        className = self.carousel_className.pop(0)
                        for y in range(count):
                            url.append(self.carousel_url.pop(0))
                            title.append(self.carousel_title.pop(0))
                            content.append(self.carousel_content.pop(0))
                        body += designs.carousel(url, title, content, className, count)
                elif x == 3:
                    if len(self.carousel_count) > 0:
                        count = self.carousel_count.pop(0)
                        url = []
                        title = self.carousel_title.pop(0)
                        content = self.carousel_content.pop(0)
                        className = self.carousel_className.pop(0)
                        for y in range(count):
                            url.append(self.carousel_url.pop(0))
                        body += designs.floating_card_carousel(url, title, content, className, count)

                elif x == 4:
                    if len(self.fcrd_count) > 0:
                        if self.fcrd_count[0] > 0:
                            for y in range(self.fcrd_count.pop(0)):
                                body += designs.floating_card_text(self.fcrd_title.pop(0), self.fcrd_content.pop(0), self.fcrd_className.pop(0))
        return body
