#-*- coding:utf-8 -*-
from Fetch.Collector.Collector import Collector
from Fetch.Collector.NaverCollector import NaverCollector
from Fetch.Collector.GoogleCollector import GoogleCollector

class Collector_agent(Collector):
    def __init__(self):
        super().__init__()
        print('-' * 50)
        print('[System] Collector agent on')
        print('-' * 50)
        self.nc = NaverCollector()
        self.gc = GoogleCollector()

    def get_url(self, htmls):
        '''
        본문의 url을 Collector 모델의 기능으로 추출한다.
        :param htmls: 본문을 Collector 모델의 기능으로  url을 추출한다.
        :return: url list
        '''
        url_list = {}
        for engine in htmls.keys():
            print('-' * 50)
            print('[Message]Collector agent : {} 페이지 내 URL 획득'.format(engine))
            print('-' * 50)
            if engine == self.nc.engine_name: url_list[engine] = self.nc.url_collect(htmls[engine])
            elif engine == self.gc.engine_name: url_list[engine] = self.gc.url_collect(htmls[engine])


        return url_list

    def page_get_html(self, urls):
        '''
        url의 본문을 Collector 모델의 기능으로 추출한다.
        :param urls: url list
        :return: html list
        '''
        html_list = {}
        for engine in urls.keys():
            print('-' * 50)
            print('[Message]Collector agent : {} 페이지(html) 획득'.format(engine))
            print('-' * 50)
            html_list[engine] = super().get_html(urls[engine])
        return html_list

    def get_page_num(self, htmls):
        '''
        네이버의 경우 현재 페이지의 링크가 나옴
        구글의 경우 현재 페이지의 링크는 나오지 않고 다음 페이지 링크부터 나옴
        :param htmls:
        :return: [Type = Dictionary] page_num_dic ( key = 'Naver' or 'Google' ... : Value = page_num_url )
        '''

        page_num_dic = {}

        for engine in htmls.keys():
            print('-' * 50)
            print('[Message]Collector agent : {} 페이지 넘버 링크 획득'.format(engine))
            print('-' * 50)
            if engine == self.nc.engine_name:
                page_num_dic[self.nc.engine_name] = self.nc.page_num_collect(htmls[engine])
            elif engine == self.gc.engine_name:
                page_num_dic[self.gc.engine_name] = self.gc.page_num_collect(htmls[engine])

        return page_num_dic





