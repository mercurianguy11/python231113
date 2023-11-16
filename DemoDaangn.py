# DemoDaangn.py


# https://www.daangn.com/fleamarket/

# <div class="card-desc">
#       <h2 class="card-title">삼성텔레비전65인치</h2>
#       <div class="card-price ">
#         150,000원
#       </div>
#       <div class="card-region-name">
#         서울 서초구 반포2동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 29
#           </span>
#         ∙
#         <span>
#             채팅 34
#           </span>
#       </div>
#     </div>

# 웹서버와 통신
import requests

#크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

posts = soup.find_all("div", attrs={"class":"card-desc"})


# for post in posts:
#     title = post.find("h2", attrs={"class":"card-title"})
#     price = post.find("div", attrs={"class":"card-price"})
#     addr = post.find("div", attrs={"class":"card-region-name"})
#     print("{0}, {1}, {2}".format(title.text, price.text, addr.text))

f = open("daagn.txt","wt", encoding="utf-8")

for post in posts:
    title = post.find("h2", attrs={"class":"card-title"}).text.strip().replace("\n", "")
    price = post.find("div", attrs={"class":"card-price"}).text.strip().replace("\n", "")
    addr = post.find("div", attrs={"class":"card-region-name"}).text.strip().replace("\n", "")
    print("{0}, {1}, {2}".format(title, price, addr))
    f.write(f"{title}, {price}, {addr}\n") # f는 format 의 약자... 쉽다...

f.close()


# for post in posts:
#     title = post.find("h2", attrs={"class":"card-title"})
#     price = post.find("div", attrs={"class":"card-price"})
#     addr = post.find("div", attrs={"class":"card-region-name"})
#     title = title.text.replace("\n", "")
#     price = price.text.replace("\n", "")
#     addr = addr.text.replace("\n", "")
#     print("{0}, {1}, {2}".format(title, price, addr))


# 페이지 로딩 
# page = open(response.text, "rt", encoding="utf-8").read()  # 메소드 체인 : 함수를 연속헤서 호출한다...

