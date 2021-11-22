#-*- coding:utf-8 -*-
from Fetch.Connector.Connector import Connector
from collections import deque

class NaverConnector(Connector):

    def __init__(self, word):
        '''
        Connector 모델을 실행 시키며 검색할 단어인 Word를 전달한다.
        :param word: [Type = String] 검색할 단어
        '''
        self.url_cnt = 0
        self.url_num_list = []
        self.word = word
        self.engine_name = 'Naver'
        self.num_link_pool = deque([])
        super().__init__(self.word)
        print('-' * 50)
        print('[System] Naver connector on')
        print('-'*50)

    def naver_get_real_url(self, url=False):
        '''
        네이버 검색엔진 URL을 통해 Get 으로 검색 화면을 찾는다.
        :return: [Type = 'http.client.HTTPResponse'] URL
        '''
        if not url:
            self.url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='+self.word
            real_url = super().search_engine(url=self.url)
        else:
            real_url = super().search_engine(url=url)

        return real_url




