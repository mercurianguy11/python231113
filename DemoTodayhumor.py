# DemoTodayhumor.py

# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) : 웹봇이 아닌 사용자가 접속하는 것으로 사기치는 것
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        # 오늘의 유머 베스트게시판
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        # list = soup.findAll('a', attrs={'class':'list_subject'})
        list = soup.find_all('td', attrs={'class':'subject'})

#<td class="subject">
#   <a href="/board/view.php?table=bestofbest&amp;no=471881&amp;s_no=471881&amp;page=1" target="_top">
#       KBS 현재 상태.jpg</a>
#   <span class="list_memo_count_span">
#        [13]
#   </span>  
#   <span style="margin-left:4px;">
#   <img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span> <span style="color:#999">3일</span></td>
# </a>
        for item in list:
                try:
                        # #<a class='list_subject'><span>text</span><span>text</span>
                        # span = item.contents[1]
                        # span2 = span.nextSibling.nextSibling
                        # title = span2.text 
                        title = item.find("a").text.strip()
                        # print(title)
                        if (re.search('한국', title)):
                                print(title)
                                # print(title.strip())
                                # print('https://www.clien.net'  + item['href'])
                except:
                        pass  # skip... 
        
