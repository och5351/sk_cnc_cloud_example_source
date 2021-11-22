#-*- coding:utf-8 -*-
from Fetch.Connector.Connector import Connector
from Fetch.Connector.NaverConnector import NaverConnector
from Fetch.Connector.GoogleConnector import GoogleConnector
from urllib.parse import quote

class Connector_agent(Connector):

    def __init__(self, word):
        """
        생성자, Naver, Google Connector를 실행 시키며, 검색할 단어인 Word를 전달한다.
        :param word: [Type = String] 검색할 단어 '문장도 가능'
        """
        word = quote(word)
        super().__init__(word)
        print('-' * 50)
        print('[System] Connector agent on')
        print('-' * 50)
        self.naver_page_cnt, self.google_page_cnt = (1, 1)
        self.nc = NaverConnector(word)
        self.gc = GoogleConnector(word)

    def search_getter(self, url=False):
        """
        검색 결과 URL을 모아서 가져다 준다.
        :return: [Type = Dictionary | key : [Type = String] , Value : [Type = 'http.client.HTTPResponse']]
        """
        url_dic = {}

        print('-' * 50)
        print('[Message]Connector agent : 링크 연결 기능 동작')
        print('-' * 50)
        if not url:
            url_dic[self.nc.engine_name] = self.nc.naver_get_real_url(url=url)
        else:
            if url[self.nc.engine_name]:
                url_dic[self.nc.engine_name] = self.nc.naver_get_real_url(url=url[self.nc.engine_name])

        print('-' * 50)
        print('[Message]Connector agent : 네이버 Response HTTP 객체 획득')
        print('-' * 50)
        if not url:
            url_dic[self.gc.engine_name] = self.gc.google_get_real_url(url=url)
        else:
            if url[self.gc.engine_name]:
                url_dic[self.gc.engine_name] = self.gc.google_get_real_url(url=url[self.gc.engine_name])

        print('-' * 50)
        print('[Message]Connector agent : 구글 Response HTTP 객체 획득')
        print('-' * 50)

        return url_dic

    def engine_checker(self, engine):
        """
        엔진에 맞는 객체를 Return
        :param engine: [Type = String] ex ( Naver, Google)
        :return: [Type = Class] Collector
        """
        if self.nc.engine_name == engine:
            return self.nc
        elif self.gc.engine_name == engine:
            return self.gc

    def check_num_link(self, page_links):
        """

        :param page_links:
        :return:
        """
        for engine in page_links.keys():
            for link in page_links[engine]:
                conn = self.engine_checker(engine)
                if not conn.is_in_num_link_pool(link):
                    conn.append_num_link_pool(link)
                    self.engine_checker(engine).url_counter()

    def get_pool(self):
        """
        Connector 의 Override 된 메소드
        :return: 각 종 Agent의 풀을 리턴한다.
        """
        return {self.nc.engine_name: self.nc.get_pool(),
                self.gc.engine_name: self.gc.get_pool()}

    def get_current_page(self):
        return {self.nc.engine_name: self.nc.url_num_list[0],
                self.gc.engine_name: self.gc.url_num_list[0]}

    def get_url_num_list(self):
        return {self.nc.engine_name: self.nc.url_num_list,
                self.gc.engine_name: self.gc.url_num_list}

    def pool_pop_left(self):
        # 엔진 페이지 넘버링 풀 pop
        self.nc.url_popleft()
        self.gc.url_popleft()
        return {self.nc.engine_name: self.nc.pool_pop_left(),
                self.gc.engine_name: self.gc.pool_pop_left()}

    def pool_is_empty(self):
        return {self.nc.engine_name: self.nc.pool_is_empty(),
                self.gc.engine_name: self.gc.pool_is_empty()}

    def is_in_pool(self):
        self.nc.is_in_page_num()







