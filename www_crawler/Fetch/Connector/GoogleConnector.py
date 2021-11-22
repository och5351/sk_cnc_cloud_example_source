#-*- coding:utf-8 -*-
from Fetch.Connector.Connector import Connector
from collections import deque

class GoogleConnector(Connector):

    def __init__(self, word):
        '''
        Connector 모델을 실행 시키며 검색할 단어인 Word를 전달한다.
        :param word: [Type = String] 검색할 단어
        '''
        self.url_cnt = 0
        self.url_num_list = []
        self.word = word
        self.engine_name = 'Google'
        self.num_link_pool = deque([])
        super().__init__(self.word)
        print('-' * 50)
        print('[System] Google connector on')
        print('-' * 50)

    def google_get_real_url(self, url=False):
        '''
        구글 검색엔진 URL을 통해 Get 으로 검색 화면을 찾는다.
        :return: [Type = 'http.client.HTTPResponse'] URL
        '''

        if not url:
            self.url = 'https://www.google.com/search?q=' + self.word + \
                       '&sxsrf=AOaemvJMIbwvVgP-1T0hUh2OuF_Io6niUw%3A1631154201497&source=hp&ei=GXA5YfXoG8TP-Qa9pKbgBg&iflsig=ALs-wAMAAAAAYTl-KXt24Vr4nWoqYmTc1AYcBO5TBzPO&oq=' + \
                       self.word + \
                       '&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIIxDqAhAnOgsIABCABBCxAxCDAToHCAAQgAQQCjoJCAAQgAQQChAqOgQIABBDUN8JWJIXYKwYaAdwAHgEgAGfAYgB4QqSAQQwLjEymAEAoAEBsAEK&sclient=gws-wiz&ved=0ahUKEwi12YH26vDyAhXEZ94KHT2SCWwQ4dUDCAc&uact=5'

            real_url = super().search_engine(url=self.url)
        else:
            real_url = super().search_engine(url=url)

        return real_url


