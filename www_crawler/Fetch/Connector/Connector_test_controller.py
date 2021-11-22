#-*- coding:utf-8 -*-
from Fetch.Connector.Connector_agent import Connector_agent
from Fetch.Collector.Collector_agent import Collector_agent

if __name__ == '__main__':

    '''
        Connector Test Controller
    '''

    conn_agent = Connector_agent(word='쿠버네티스')
    coll_agent = Collector_agent()

    # 접속 에이전트에게 검색엔진 접속 명령
    first_real_url = conn_agent.search_getter()

    htmls = coll_agent.page_get_html(urls=first_real_url)

    page_num = coll_agent.get_page_num(htmls)

    conn_agent.check_num_link(page_num)
    num_list = conn_agent.get_pool()

    for engine in num_list.keys():
        print(engine)
        for link in num_list[engine]:
            print(link)

