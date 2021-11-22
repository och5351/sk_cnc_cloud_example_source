#-*- coding:utf-8 -*-
from Fetch.Collector.Collector import Collector

class GoogleCollector(Collector):
    def __init__(self):
        super().__init__()
        print('-' * 50)
        print('[System] Google collector on')
        print('-' * 50)
        self.engine_name = 'Google'

    def url_collect(self, html):
        url_list = []
        for href in html.find("div", id='center_col').find_all('a'):
            try:
                if href['href'] == '#':
                    pass
                elif href['href'][:len('/search?')] == '/search?':
                    pass
                elif href['href'][:len('https://webcache')] == 'https://webcache':
                    pass
                elif href['href'][:len('/url?url=https://support.google.com/')] == '/url?url=https://support.google.com/':
                    pass
                else:
                    url_list.append(href['href'])
            except:
                continue

        return url_list

    def page_num_collect(self, html):
        num_link_lst = []
        main_url = 'https://www.google.com'
        try:
            for td in html.find("span", id="xjs").find_all('td'):
                if td.find('a') == None:
                    continue
                num_link_lst.append(main_url + td.find('a')['href'])
        except:
            return num_link_lst

        return num_link_lst
