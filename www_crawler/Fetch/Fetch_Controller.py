#-*- coding:utf-8 -*-

from Fetch.Collector.Collector_agent import Collector_agent
from Fetch.Connector.Connector_agent import Connector_agent
from Util.Util_agent import Util_agent
import sys

if __name__ == '__main__':

    # 검색 단어
    word, stop_num = input().split()
    # 원하는 검색할 페이지 수
    stop_num = int(stop_num)
    cnt = 0

    # Agent 생성
    # conn_agent = Response 객체 획득 및 넘버 페이지 링크를 관리하는 Agent
    # coll_agent = Response 객체 에서 html, link를 추출하는 Agent
    # util_agent = 파일 입출력 및 기타 기능을 담당하는 Agent
    conn_agent = Connector_agent(word=word)
    coll_agent = Collector_agent()
    util_agent = Util_agent()

    # connect Agent 에게 Naver, Google 검색 엔진 결과 Response 객체 수신 명
    first_real_url = conn_agent.search_getter()

    # collect Agent 에게 수신한 Response 에게 Html 획득 명령
    htmls = coll_agent.page_get_html(urls=first_real_url)

    # 모든 페이지를 조회 할 때 까지 (풀이 빌 떄 까지)
    while first_real_url:


        cnt += 1

        print('-' * 50)
        print('[System] {} 페이지'.format(cnt))
        print('-' * 50)

        # collect Agent 에게 페이지 내의 url 획득 명령
        search_urls = coll_agent.get_url(htmls)

        # Collect Agent 에게 페이지 숫자 추출 명령
        page_num = coll_agent.get_page_num(htmls)

        # Connect Agent 에게 페이지 링크를 체크하여 풀에 저장
        conn_agent.check_num_link(page_num)

        # 획득한 url 접속 후 html scrap & save(Parsing 과정 생략)
        for engine in search_urls.keys():
            # Util Agent 에게 디렉터리가 없을 시 엔진 별 디렉터리 생성 명령
            # path = util_agent.util_mkdir(engine=engine, extension='HTML')
            path = util_agent.util_mkdir(engine=engine, extension='TEXT')

            if len(conn_agent.get_pool()[engine]) == 0:
                print('-' * 50)
                print('[System] {} 페이지 더 이상 없음'.format(engine))
                print('-' * 50)
                continue

            for url in search_urls[engine]:
                # Connect Agent에게 url open 명령
                soup = conn_agent.url_opener(url)
                # Collect Agent 에게 Response 객체에서 html 획득 명령
                html_data = coll_agent.get_html(soup)
                # Util Agent 에게 획득한 html 저장 명령 ( 경로 : ./Data/' + engine.upper() + '_DATA_HTML' )
                #util_agent.save_html(data=html_data, engine=engine, path=path, encoding='utf-8')
                util_agent.save_txt(data=html_data, engine=engine, path=path)

        if cnt == stop_num:
            break

        # Connect Agent 에게 풀 popleft 명령
        search_link = conn_agent.pool_pop_left()

        # connect Agent 에게 Naver, Google 검색 엔진 결과 Response 객체 수신 명
        first_real_url = conn_agent.search_getter(search_link)

        # collect Agent 에게 수신한 Response 에게 Html 획득 명령
        htmls = coll_agent.page_get_html(urls=first_real_url)

    print('stop_crawler_program')
    sys.exit()



