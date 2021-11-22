#-*- coding:utf-8 -*-
from Fetch.Collector.Collector import Collector

class NaverCollector(Collector):
    def __init__(self):
        super().__init__()
        print('-'*50)
        print('[System] Naver collector on')
        print('-' * 50)
        self.engine_name = 'Naver'

    def url_collect(self, html):
        url_list = []
        for href in html.find("div", id='content').find_all('li'):
            try:
                if href.find('a')['href'][0] == '?':
                    continue
                elif href.find('a')['href'] == '#':
                    url_list.append(href.find('a')['data-url'])
                else:
                    url_list.append(href.find('a')['href'])
            except:
                continue

        return url_list

    def page_num_collect(self, html):
        num_link_lst = []
        main_url = 'https://search.naver.com/search.naver'
        try:
            for link in html.find("div", class_='sc_page_inner').find_all('a'):
                if link['href'] == None:
                    continue
                num_link_lst.append(main_url + link['href'])
        except:
            return num_link_lst

        return num_link_lst