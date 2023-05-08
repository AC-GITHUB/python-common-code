# -*- coding: <utf-8> -*-
import urllib.request
from bs4 import BeautifulSoup
import logging
import time
import os


class Page:
    __base_url = ""

    def __init__(self, base_url):
        self.__base_url = base_url

    def get_page(self, url):
        if (not url):
            return
        print(self.__baseUrl + url)
        count = 0
        is_success = False
        while (not is_success and count < 5):
            time.sleep(0.01)
            count = count + 1
            try:
                req = urllib.request.Request(self.__base_url + url,
                                             method="GET")
                response = urllib.request.urlopen(req)
                is_success = True
            except urllib.error.HTTPError:
                print()
        if (not is_success):
            logging.error("{},执行错误".format(self.__base_url + url))
        if (response.status == 200):
            data = response.read()
            soup = BeautifulSoup(data.decode(encoding="utf-8"), 'html.parser')
            title = soup.select("title")
            cc = ('/Users/acc/software/pandoc-2.19.2/bin/pandoc  '
                  '--extract-media=/Users/acc/gitworkspace/数据库内核/cache '
                  '--data-dir=/Users/acc/gitworkspace/数据库内核/cache'
                  ' --pdf-engine=wkhtmltopdf -f html -t pdf '
                  '-o "/Users/acc/gitworkspace/数据库内核/doc/' + title[0].text +
                  '.pdf" ' + self.__base_url + url)
            print(cc)
            os.system(cc)
            print("文章:{},url:{}".format(title, self.__base_url + url))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        filename='/Users/acc/gitworkspace/数据库内核/new.log',
                        filemode='w')
    base_url = "http://mysql.taobao.org"
    page = Page(base_url)
    req = urllib.request.Request(base_url + "/monthly/", method="GET")
    response = urllib.request.urlopen(req)
    if (response.status == 200):
        data = response.read()
        soup = BeautifulSoup(data.decode(encoding="utf-8"), 'html.parser')
        for el in soup.select("#container > div.content.typo > ul > li a"):
            req = urllib.request.Request(base_url + el.attrs['href'],
                                         method="GET")
            response = urllib.request.urlopen(req)
            if (response.status == 200):
                data = response.read()
                soup1 = BeautifulSoup(data.decode(encoding="utf-8"),
                                      'html.parser')
                for el in soup1.select(
                        "#container > div.content.typo > ul > li a"):
                    page.getPage(el.attrs['href'])

    print("完成")
