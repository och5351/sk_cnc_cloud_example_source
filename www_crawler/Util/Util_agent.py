#-*- coding:utf-8 -*-
import os
import datetime

class Util_agent(object):

    def __init__(self):
        print('-' * 50)
        print('[System] Util agent on')
        print('-' * 50)

    def save_txt(self, data, engine, path, encoding='utf-8'):
        '''
                html 로 save 하는 기능
                :param data: [type = bs4.beautifulsoup]데이터(html)
                :param engine: [type = String] 검색 엔진 이름 (ex. Naver, Google)
                :param path: [type = String] 경로 (util_mkdir return 값의 경로를 추천)
                :param encoding: [type = String] default utf-8
                :return: x
                '''
        if data:
            d = datetime.datetime.now()
            date = str(d.year) + str(d.day).zfill(2) + str(d.day).zfill(2) + str(d.hour).zfill(2) + str(d.minute).zfill(
                2) + str(d.second).zfill(2)
            name = engine.upper() + '_' + str(len(os.listdir(path))) + '_' + date
            file_path_name = path + '/' + name + '.txt'

            f = open(file_path_name, 'w', encoding=encoding)
            f.write(str(data))
            f.close()

            print('[Message]Util agent : ', file_path_name, ' save complete.')
        else:
            print("[Failure Message]Util agent : Can't save data. It's empty.")

    def save_html(self, data, engine, path, encoding='utf-8'):
        '''
        html 로 save 하는 기능
        :param data: [type = bs4.beautifulsoup]데이터(html)
        :param engine: [type = String] 검색 엔진 이름 (ex. Naver, Google)
        :param path: [type = String] 경로 (util_mkdir return 값의 경로를 추천)
        :param encoding: [type = String] default utf-8
        :return: x
        '''
        if data:
            d = datetime.datetime.now()
            date = str(d.year) + str(d.day).zfill(2) + str(d.day).zfill(2) + str(d.hour).zfill(2) + str(d.minute).zfill(2) + str(d.second).zfill(2)
            name = engine.upper() + '_' + str(len(os.listdir(path)))+'_'+ date
            file_path_name = path+'/'+name+'.html'

            f = open(file_path_name, 'w', encoding=encoding)
            f.write(str(data))
            f.close()

            print('[Message]Util agent : ', file_path_name, ' save complete.')
        else:
            print("[Failure Message]Util agent : Can't save data. It's empty.")

    def util_mkdir(self, engine, extension='HTML'):
        '''
        워크 스페이스 안에 Directory 생성
        :param engine: [type = String] 엔진 구분 (ex. Naver, Google)
        :return: [type = String] path
        '''
        # Engine 별 디렉토리
        path = './Data/' + engine.upper() + '_DATA_' + extension
        os.makedirs(path, exist_ok=True)
        print('-' * 50)
        print('[Message]Util agent : ', path, ' complete.')
        print('-' * 50)
        return path

