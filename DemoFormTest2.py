# DemoFormTest2.py
# DemoFormTest2.ui(화면단) + DemoFormTest2.py(로직단)


# 시그널과 슬롯 처리: 버튼을 클릭하면 이벤트 처리하는 데모 -> Event
# 시그널(Signal): 프로그램에서 어떤 버튼이 클릭되면 시그널이 발생했다고 한다. 클릭 이벤트가 발생했다는 의미로 해석해도 된다! 
# 슬롯(Slot):시그널이 발생했을 때 특정 함수나 기능이 실행되도록 명령을 내릴 때 이를 슬롯이라고 한다. -> EventHandler
# self.checkBox1.stateChanged.connect(self.checkBoxState)
# stateChanged -> 시그널
# checkBoxState -> 슬롯메소드

# 1. 디자이너 이용
# 2. 100% 코딩

# 이벤트 루프가 사용자가 버튼을 클릭시 시그널 clicked() 발생 -> 슬롯메서드 호출

import sys
import typing
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget

# 디자인파일 로딩
form_class = uic.loadUiType("DemoFormTest2.ui")[0]

# 폼클래스 정의
class DemoFromTest2(QDialog, form_class):
    # 초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.label.setText("첫번째 화면")

# 직접 모듈을 실행한 경우면 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)        
    demoForm = DemoFromTest2()
    demoForm.show()
    app.exec_()


# Qt 디자이너를 사용해서 폼을
# 만들 때 두번째 데모는 
# Main Window템플릿을 
# 선택해야 한다.
# Dialog는 일반적으로 대화상장(작은창)을 생성할 때 사용하고 메뉴나 툴바등이 추가되면 Main Window템플릿은 선택해야 한다. 

# Main Window : 큰창 (메뉴, 툴바)  QDialog 상속
# Dialog : 대화상자 (작은창)  QMainWindow 상속
