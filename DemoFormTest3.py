# DemoFormTest3.py
# DemoFormTest3.ui(화면단) + DemoFormTest3.py(로직단)

# https://wikidocs.net/book/110  참고...


import sys
import typing
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget


# 웹서버와 통신
import requests

#크롤링
from bs4 import BeautifulSoup

# .exe 배포 with .ui file
import os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# 디자인파일 로딩
form_class = uic.loadUiType("DemoFormTest3.ui")[0]

# 폼클래스 정의(QMainWindow 변경)
class DemoFromTest3(QMainWindow, form_class):
    # 초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.label.setText("첫번째 화면")
    def firstClick(self):
        url = "https://www.daangn.com/fleamarket/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        posts = soup.find_all("div", attrs={"class":"card-desc"})
        f = open("daangn.txt","wt", encoding="utf-8")
        for post in posts:
            title = post.find("h2", attrs={"class":"card-title"}).text.strip().replace("\n", "")
            price = post.find("div", attrs={"class":"card-price"}).text.strip().replace("\n", "")
            addr = post.find("div", attrs={"class":"card-region-name"}).text.strip().replace("\n", "")
            print("{0}, {1}, {2}".format(title, price, addr))
            f.write(f"{title}, {price}, {addr}\n")
        f.close()
        self.label.setText("당근에서 크롤링 완료~~")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭 !!")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭 !!!")

# 직접 모듈을 실행한 경우면 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)        
    demoForm = DemoFromTest3()
    demoForm.show()
    app.exec_()
