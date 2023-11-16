# Demoppomppu.py

# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) : 웹봇이 아닌 사용자가 접속하는 것으로 사기치는 것
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        # 뽑뿌 휴대폰 게시판
        data ='https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu2&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        # list = soup.findAll('a', attrs={'class':'list_subject'})
        #list = soup.find_all('td', attrs={'valign':'middle'})
        list = soup.find_all('font', attrs={'class':'list_title'})

# <td valign="middle">
#   <a href="zboard.php?id=sponsor&amp;no=87523&amp;sn=on&amp;ss=off&amp;sc=off&amp;search_type=name&amp;keyword=%C5%B8%BF%E4%C6%F9%21">(통신3사 최저가) 아이폰15  빠른 재고+선착순 특가! 가을 맞이 이벤트!! Galaxy Z Fold5ㅣFlip5 출시 혜택 최저가 이벤트! 갤럭시S23 / 아이폰14...</a>&nbsp;<span class="list_comment2"> <span style="cursor:pointer;" onclick="win_comment(&quot;popup_comment.php?id=sponsor&amp;no=87523&quot;);">1803</span> </span>		  </td>
        for item in list:
                try:
                        # #<a class='list_subject'><span>text</span><span>text</span>
                        # span = item.contents[1]
                        # span2 = span.nextSibling.nextSibling
                        # title = span2.text 
                        title = item.find("a").text.strip()
                        print(title)
                        # if (re.search('한국', title)):
                        #         print(title)
                                 # print(title.strip())
                                # print('https://www.clien.net'  + item['href'])
                except:
                        pass  # skip... 
        



