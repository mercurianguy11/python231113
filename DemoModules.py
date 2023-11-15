# DemoModules.py

# time 모듈
# datetime 모듈
# random 모듈
# os.path 모듈
# os 모듈
# glob 모듈 

# 시간(time) 모듈:
# 타임스탬프(Time Stamp) : 컴퓨터에서 시간을 측정하는 방법으로 1970년 1월 1일 자정 이후로 초 단위로 측정한 절대 시간
# 협정 세계시(UTC-Universal Time Coordinated) :  1972년부터 시행된 국제 표준시이다. 
# 그리니치 평균시(GMT-Greenwich Mean Time) : 런던 그리니치 천문대의 자오선상에서의 평균 태양시이다. 1972년부터 협정 세계시를 사용한다. 
# 지방 표준시(LST-Local Standard Time) : UTC를 기준으로 경도 15도마다 1시간 차이가 발생한다. 

# time.time() : 1970년 1월 1일 자정 이후로 누적된 초를 float단위로 반환한다. 
# time.sleep(secs) : 현재 동작 중인 프로세스를 주어진 초만큼 정지시킨다.
# time.gmtime([secs]) : 입력된 초를 변환해 UTC 기준의 struct_time 시퀀스 객체로 반환한다.
# time.localtime([secs]) : 입력된 초를 변환해 지방 표준시 기준의 struct_time 시퀀스 객체를 반환한다. 

import time
print(dir(time))
print(time.time())
print(time.gmtime())
print(time.localtime())
print(time.gmtime().tm_year)

time.sleep(10)
