# DemoWebCrawling.py

# pip명령으로 모듈 설치하기 
# HTML 과 CSS 정리하기 
# BeautifulSoup을 사용한 크롤링
# Selenium, requests, clipboard을 추가로 사용한 크롤링 

# 파이썬 개발 환경에 새로운 모듈을 설치하기
# pip(Python Install Package)를 사용하면 쉽게 설치할 수 있다.  python310\Scripts\pip.exe
# pip list : 설치된 목록을 볼 수 있다. 
# pip install BeautifulSoup4: 새로운 패키지를 설치할 수 있다. 
# pip uninstall BeautifulSoup4: 설치된  패키지를 언인스톨 할 수 있다. 
# 에러가 발생하는 경우는 pip3.exe를 사용해도 된다. 

# 설치된 목록을 본다.
# 	pip list
# 실제 모듈을 설치한다. 
# 	pip install beautifulsoup4


# C:\Users\student>pip list
# Package                   Version
# ------------------------- --------
# altgraph                  0.17.4
# packaging                 23.2
# pefile                    2023.2.7
# pip                       23.3.1
# pygame                    2.5.2
# pyinstaller               6.2.0
# pyinstaller-hooks-contrib 2023.10
# pywin32-ctypes            0.2.2
# setuptools                65.5.0

# C:\Users\student>pip install BeautifulSoup4
# Collecting BeautifulSoup4
#   Downloading beautifulsoup4-4.12.2-py3-none-any.whl (142 kB)
#      ---------------------------------------- 143.0/143.0 kB 4.3 MB/s eta 0:00:00
# Collecting soupsieve>1.2 (from BeautifulSoup4)
#   Downloading soupsieve-2.5-py3-none-any.whl.metadata (4.7 kB)
# Downloading soupsieve-2.5-py3-none-any.whl (36 kB)
# Installing collected packages: soupsieve, BeautifulSoup4
# Successfully installed BeautifulSoup4-4.12.2 soupsieve-2.5

# C:\Users\student>pip list
# Package                   Version
# ------------------------- --------
# altgraph                  0.17.4
# beautifulsoup4            4.12.2   -> 설치확인..
# packaging                 23.2
# pefile                    2023.2.7
# pip                       23.3.1
# pygame                    2.5.2
# pyinstaller               6.2.0
# pyinstaller-hooks-contrib 2023.10
# pywin32-ctypes            0.2.2
# setuptools                65.5.0
# soupsieve                 2.5


# 혹시 회사 내부에 보안상 인터넷이 안되는 PC나 노트북이 있는 상황이라면 다음과 같이 하면 된다.
# 파이썬이 c:\python310에 설치되어 있고 미리 BeautifulSoap이 설치된 PC의 c:\python310\lib\site-packages폴더를 다른 PC에 복사해 주면 된다. 


# 웹크롤링 설치 
# cmd
# pip install beautifulsoup4
# pip install requests : 웹페이지 연결 요청

# 셀리니엄 설치 
# pip install selenium : 원격으로 웹브라우저 핸들링
# pip install webdriver_manager : 웹브라우저 원격으로 핸들링시 편하게 쓰기위한 드라이버
# pip install chromedriver_autoinstaller
# pip install clipboard
# pip install openpyxl

# C:\Users\student>pip list
# Package                    Version
# -------------------------- -----------
# altgraph                   0.17.4
# attrs                      23.1.0
# beautifulsoup4             4.12.2
# certifi                    2023.7.22
# cffi                       1.16.0
# charset-normalizer         3.3.2
# chromedriver-autoinstaller 0.6.2
# clipboard                  0.0.4
# et-xmlfile                 1.1.0
# exceptiongroup             1.1.3
# h11                        0.14.0
# idna                       3.4
# openpyxl                   3.1.2
# outcome                    1.3.0.post0
# packaging                  23.2
# pefile                     2023.2.7
# pip                        23.3.1
# pycparser                  2.21
# pygame                     2.5.2
# pyinstaller                6.2.0
# pyinstaller-hooks-contrib  2023.10
# pyperclip                  1.8.2
# PySocks                    1.7.1
# python-dotenv              1.0.0
# pywin32-ctypes             0.2.2
# requests                   2.31.0
# selenium                   4.15.2
# setuptools                 65.5.0
# sniffio                    1.3.0
# sortedcontainers           2.4.0
# soupsieve                  2.5
# trio                       0.23.1
# trio-websocket             0.11.1
# urllib3                    2.1.0
# webdriver-manager          4.0.1
# wsproto                    1.2.0

# c:\python310\lib\site-packages 폴더 확인...

# 선언적 태그를 가지고 모양을 꾸밈
# HTML(HyperText Markup Language)5는 이전 버전을 넘는 많은 확장들을 제공한다: html 4.01 -> 5.0
# 브라우져 밴더들을 위한 룰들
# 모던한 웹 애플리케이션 개발을 반영한                  새로운 요소들
# 데스크탑과 모바일 애플리케이션의            지원능력을 지원하는 JavaScript API들
# 2014년 10월 28일 HTML5 권고안 발표됨
# CSS(Cascading Style Sheet)3은 HTML문서에 있는 태그들을 시각적으로 꾸며주는 역할을 담당한다.  

# https://opentutorials.org/course/2039 강의 참고...

# p : 단락
# br : 줄바꿈
# img : 이미지 
# table : 표
# form : 입력양식

# IE : Internet Explorer 6.0 -> 7.0 (Microsoft)
# open Web : chrome, safari
# web으로 게임이 동작한다... ex ) M365

# html -> 모양, css -> 스타일

# <html>
#   <head>
#
#   <body>
#
#

# Web browser 가 웹 페이지를 parsing... 해석된 결과를 user가 확인
# 동적인 코드는 javascript 코드가 실행..

# HTML 태그(Tag, Element)들은 웹페이지의 컨텐츠에 대해 구조와 의미를 정의한다. 
# 태그(Tag, Element)들은 시작 태그와 끝 태그로 컨텐츠를 감싸서 사용할 수 있다:

# strong : 볼드체
# em : 이탤릭체
# <p>
#     <strong>Elements</strong> consist of 
#     <strong>content</strong> bookended by a 
#     <em>start</em> tag and an <em> end</em> tag.
# </p>

# 태그(Tag, Element) 의 컨텐츠에 대해 추가적인 정보를 제공하려면 속성(Attribute)들을 사용한다. 
# <img src="log.jpg" alt="My Web site logo" height="100" width="100" />  : alt, height, width -> attributes

# HTML 안에 텍스트는 아래와 같이 마크업 된다: 
# heading들과  paragraph들  h1~h6 : header...

# <h1>An Introduction to HTML</h1>
# <p>In this module, we look at the history of HTML and CSS.</p>
# <h2>In the Beginning</h2>
# <p>WorldWideWeb was created by Sir Tim Berners-Lee at CERN. </p>

# 아래와 같이 강조 

# To <strong>emphasize</strong> is to give extra weight to (a communication); <em>"Her gesture emphasized her words"</em> 


# 리스트 
# ul
# ol : ordered list

# table태그를 사용한다면 다음과 같다. <tr>은 행을 정의하고 <td>는 컬럼을 정의한다.  
# <table border="1">
#     <tr>
#         <td>번호</td>
#         <td>책 제목</td>
#         <td>출판사</td>
#         <td>저자</td>        
#         <td>가격</td>
#     </tr>
#     <tr>
#         <td>1</td>
#         <td>파이썬</td>
#         <td>마이북스</td>
#         <td>전우치</td>        
#         <td>25000</td>
#     </tr>
# </table>

# 앵커 -> 대상 사이트로 이동
# <a href="default.html" alt="Home Page">Home</a>

# CSS3 설명
# 모든 CSS 룰들은 동일한 문법을 사용한다:

# selector {
#   property1:value;
#   property2:value;
#   ..
#   propertyN:value;
# }


# 선택자(selector)는 태그
# (tag)를 지정 할수있다. 
# 특정 태그에 적용되는 
# 스타일을 정의한다.  

# /* Targets level 1 headings  */ 선택자...
# h1 {
#   font-size: 42px;
#   color: pink;
#   font-family: 'Segoe UI';
# }

# 3개의 기본 CSS 선택자(selector)들이 있다. 
# tag selector:  h2{} 이런 형태로 사용하면 웹페이지에 있는 모든 h2 태그에 적용된다. -> 잘 사용 안한다...
# class selector:  .title {} 디자인을 위해 class=title로 되어 있는 태그만을 특정해서 필터링을 할 수 있다.  . -> class attribute 의미
# 웹툰의 제목에만 title스타일을 적용하겠다는 의미이다. 
# id selector:   #first {} 특정 태그(tag)만을 지정하는 경우라면 id=first와 같이 지정할 수 있다.   # -> id 속성을 의미.

# div, span 영역을 분리하는 표시
# <div class=“title”>이 제품에 대한 설명</div>  .title
# <span class=“title”>다양한 데모</span>
# <p id="first">여기를 지정한다</p> : #first

# 태그에 스타일을 저장할 때 style 속성을 사용한다:  -> 색깔 변경시 100군데 이상을 바꿔야 할 경우 발생
# <p style="color:blue;"> some text </p>

# 페이지에 스타일들을 포함하기 위해 <head>에 <style> 태그를 지정한다: 
# <style type="text/css">
#     p { color: blue; }
# </style>
# p 는 선택자... p 를 바꾸면 P style 모두 바뀜.. 페이지별 작업 필요....잘 안씀..

# 외부 스타일 시트를 참조하기 위해 <link> 요소를 사용한다:
# <link rel="stylesheet" type="text/css" href="mystyles.css" media="screen">

# .js => javascript , .css => 스타일
# default, detail, list 임베딩...

# 모듈인지 패키지인지 구분 어려움.... 개발자 문서 참고해라...
# 웹크롤링을 위한 선언
from bs4 import BeautifulSoup

# 페이지 로딩 
page = open("test01.html", "rt", encoding="utf-8").read()  # 메소드 체인 : 함수를 연속헤서 호출한다...

# 검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")

# xml문서 (저장, 교환)
# BeautifulSoup option : html.parser, lxml, xml, html5lib

# 전체 페이지 보기
print(soup.prettify())
