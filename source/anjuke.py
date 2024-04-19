# encoding:utf-8

from html.parser import HTMLParser

from numpy.core.defchararray import strip


class AnjukeParser(HTMLParser):
    def __init__(self):
        super().__init__()
        # 存储中间数据（安居客为房屋描述、小区名）
        self.span = ""
        # 存储中间数据（安居客为总价）
        self.strong = ""
        # 房屋名称
        self.houseName = []
        # 小区名称
        self.villageName = []
        # 房子介绍
        self.houseNote = []
        # 总价
        self.houseTotlePrice = []
        # 单价
        self.houseUnitPrice = []
        # 房屋链接
        self.houseLink = []
        # 第一张图片
        self.houseImg = []
        # 用于标记数据类型
        self.flag = []
        # aa
        self.aa = ()

    def feed(self, data):
        super().feed(data)
        # 校验数据个数是否统一
        # size = len(self.houseName)
        # if len(self.houseName) != size or len(self.villageName) != size or len(self.houseNote) != size \
        #         or len(self.houseTotlePrice) != size or len(self.houseUnitPrice) != size or len(self.houseLink) != size \
        #         or len(self.houseImg) != size:
        #     raise ValueError("数据个数不一致：houseName-" + str(len(self.houseName)) + ",villageName-" + str(len(self.villageName)) +
        #                      ",houseNote-" + str(len(self.houseNote)) + ",houseTotlePrice-" + str(len(self.houseTotlePrice)) +
        #                      ",houseUnitPrice-" + str(len(self.houseUnitPrice)) + ",houseLink-" + str(len(self.houseLink)) +
        #                      ",houseImg-" + str(len(self.houseImg)))
        return self.houseName, self.villageName, self.houseNote, self.houseTotlePrice, self.houseUnitPrice, self.houseLink, self.houseImg, [0]*len(self.houseImg)

    def handle_starttag(self, tag, attrs):
        from urllib.parse import urlparse
        if tag == "p" and ("class", "property-content-info-comm-name") in attrs:
            self.flag.append("villageName")
        elif tag == "span" and ("class", "property-price-total-num") in attrs:
            self.flag.append("houseTotlePrice_2")
        elif tag == "p" and ("class", "property-price-average") in attrs:
            self.flag.append("houseUnitPrice")
        elif tag == "span":
            self.flag.append("span")
        elif tag == "strong":
            self.flag.append("strong")
        elif tag == "h3" and ("class", "property-content-title-name") in attrs:
            self.flag.append("houseName")
        elif tag == "a" and ("class", "property-ex") in attrs:
            for attr in attrs:
                if attr[0] == "href":
                    linkUrl = urlparse(attr[1])
                    self.houseLink.append('%s://%s%s'%(linkUrl.scheme,linkUrl.hostname,linkUrl.path))
        elif tag == "div" and ("class", "property-content-info") in attrs:
            self.flag.append("houseNote_2")
            self.span = ""
        elif tag == "img" and ("class", "lazy-img cover") in attrs:
            for attr in attrs:
                if attr[0] == "src":
                    self.houseImg.append(attr[1])

    def handle_endtag(self, tag):
        if len(self.flag) != 0:
            if tag == "div" and self.flag[-1] == "houseNote_2" and self.span != "":
                # 此时为houseNote的结束
                # print(self.span.encode('GB18030'))
                self.houseNote.append(self.span)
                self.flag.pop()
                self.span = ""
            elif tag == "div" and self.flag[-1] == "houseNote_2":
                self.flag.pop()

    def handle_data(self, data):
        if len(self.flag) != 0:
            if self.flag[-1] == "span":
                self.span += data
                self.flag.pop()
            elif self.flag[-1] == "strong":
                # print('strong = '+str(data))
                self.strong = data
                self.flag.pop()
            elif self.flag[-1] == "houseName":
                # print('houseName = '+str(data))
                self.houseName.append(str(strip(data)))
                self.flag.pop()
            elif self.flag[-1] == "villageName":
                # print('villageName = '+str(data))
                self.villageName.append(str(strip(data)))
                self.flag.pop()
            elif self.flag[-1] == "houseTotlePrice_2":
                # print('houseTotlePrice_2 = '+str(data))
                self.houseTotlePrice.append(data + '万')
                self.flag.pop()
            elif self.flag[-1] == "houseUnitPrice":
                # print('houseUnitPrice = '+str(data))
                self.houseUnitPrice.append(data)
                self.flag.pop()
