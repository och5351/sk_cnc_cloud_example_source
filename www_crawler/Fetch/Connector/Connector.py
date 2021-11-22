#-*- coding:utf-8 -*-
from urllib.request import Request, urlopen

'''
Connector 클래스

하위 클래스
NaverConnector, GoogleConnector, Connect_agent
'''

class Connector(object):

    def __init__(self, word):
        '''
        :param word: 검색 단어
        '''
        self.word = word

    def search_engine(self, url):
        '''
        :param url:  url 링크
        :return: url_link
        '''

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        re = Request(url + self.word, headers=headers)
        source_code_from_URL = urlopen(re)

        return source_code_from_URL

    def url_opener(self, url):
        '''
        매개변수로 받은 url을 오픈 하여 return 한다.
        :param url: [Type = String] url
        :return: Response HTTP
        '''

        try:
            result = urlopen(url)
        except:
            result = False

        return result

    def get_pool(self):
        '''
        페이지를 이동할 수 있는 Number 링크들이 담긴 풀의 내용을 확인 가능하다.
        :return:
        '''
        return self.num_link_pool

    def is_in_num_link_pool(self, link):
        '''
        페이지를 이동할 수 있는 Number 링크가 풀에 들어있는 지 확인 하는 메소드
        :param link: [Type = String] 페이지 넘버 URL
        :return: [Type = Bool] 들어있을 경우 True 아닐 경우 False
        '''
        return link in self.num_link_pool

    def append_num_link_pool(self, link):
        '''
        풀에 링크를 담는 메소드
        :param link: [Type = String] URL
        :return: X
        '''
        self.num_link_pool.append(link)

    def pool_pop_left(self):
        try:
            return self.num_link_pool.popleft()
        except:
            return False

    def pool_is_empty(self):
        return False if self.num_link_pool else True

    def url_counter(self):
        self.url_cnt += 1
        self.url_num_list.append(self.url_cnt)

    def url_popleft(self):
        self.url_num_list.pop(0)

    def is_in_pool(self):
        return self.url_num_list

    def stopper(self):
        self.working = False




