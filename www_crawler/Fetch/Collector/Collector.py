#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup as beauty

class Collector(object):

    def __init__(self):
        pass

    def get_html(self, url):
        '''
        :return: beautifulsoup 검색엔진 검색 결과 html
        '''
        if url:
            soup = beauty(url, 'html.parser', from_encoding='utf-8')
        else:
            soup = url

        return soup

