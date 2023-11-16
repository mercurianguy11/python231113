# DemoPyQt.py

# PyQt는 영국의 Riverbank Computing이라는 곳에서 C++의 Cross Platform GUI Frameowrk중의 하나인 Qt를 파이썬 모듈로 변환해 주는 툴을 만들면서 시작되었다. 
# 간단하게 설명하면 Qt라는 GUI화면을 만들어 주는 도구를 원래 파이썬에서 사용할 수 없는 C++용이였는데 
# 파이썬에서도 사용할 수 있게 변환 툴을 만들어 주여서 우리는 파이썬과 Qt를 사용해서 원하는 것을 빠르게 만들 수 있게 되었다. 

# 파이썬 진영에는 PyGTK, PySide, Tkinter등이 있지만 사용에 어려움이 있고 모양이 이쁘지 않다는 치명적인 단점이 있었다. 
# PyQt를 사용해서 얻을 수 있는 가장 큰 장점은 상기 명시된 툴들 중에서 가장 쉽고 예쁘고 직관적인 인터페이스인 
# Qt Designer를 사용해서 작업을 할 수 있다는 것이다

# http://pyqt.sourceforge.net/Docs/PyQt5 에서 파이썬 2.* 또는 3.* 지원 버전을 받을 수 있다. 
# 또는 pip명령으로 바로 설치할 수 있다.

# 첫번째 데모: Qt Designer를 사용해서 라벨에 문자열을 출력하는 간단한 데모. 

# DemoForm.ui(UI단) + DemoForm.py(로직단)
# 앞에서 했던 작업들과 다르게 2개의 파일로 구성한다. Qt 디자이너로 작업한 화면은 XML문서로 저장되며, 이 문서를 로딩해서 폼 클래스에서 사용한다. 

# DemoForm.ui XML 문서 : 좌표계 저장, 화면단..
# DemoForm.py : 클래스 정의(매서드 구현, 복사)

# 이 코드는 DemoForm.py 파일로 저장해서 폼클래스를 정의한 로직파일로 사용한다.  

# PyQt5 폴더:패키지  
# QtWidgets : 모듈 (MicroSoft에서는 control이라 부름)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 

# 사전에 디자인한 파일을 불러옴
# [0] ui tag가 여러개가 있을 수 있음... 우리는 한개만 쓸거임.

form_class = uic.loadUiType("DemoForm.ui")[0]
class DemoForm(QDialog, form_class):   # QDialog 부모 class 와 form_class 상속 : 대화상자 -> 다중 상속
    def __init__(self):
        super().__init__()   # 부모클래스 초기화 함수 호출
        self.setupUi(self)   # U만 대문자... 조심해서 사용
        self.label.setText("첫번째 PyQt데모")

# 이 모듈을 직접 실행하는 경우는 
# __name__이 __main__ 이다. 
# 직접 모듈을 실행했는지의 여부를
# 체크한다. 
# 이 모듈을 sub로 사용할 수 있다. main 함수와 유사..
# 다른쪽에서 import 해서 사용하는 경우 아래 __main__ 수행되지 않는다.

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 실행 프로세스 ,, 초기값 sys.argv 지정
    demoWindow = DemoForm()       # DemoFrom class 초기화
    demoWindow.show()             # UI 띄어준다..
    app.exec_()                   # 계속 대기하고 있어.. execute...

# 만약 exel을 실행한다면.. excel.exe는 프로세스
# excel 내  sheet1(창)  show() -> 화면을 보여준다.