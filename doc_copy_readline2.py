# 're' 모듈을 불러옵니다. 이 모듈은 정규 표현식을 사용할 수 있게 해줍니다.
import re

# 'c:\\work\\PV3.txt' 파일을 읽기 모드('rt')로 엽니다.
f = open('c:\\work\\PV3.txt', 'rt')

# 'c:\\work\\PV3_copy.txt' 파일을 쓰기 모드('wt')로 엽니다. 텍스트를 UTF-8로 인코딩합니다.
g = open('c:\\work\\PV3_copy.txt', 'wt', encoding='utf-8')

# 파일에서 한 줄을 읽어옵니다.
line = f.readline()

# 파일의 끝에 도달할 때까지 반복합니다.
while (line != ''):
    # 만약 현재 줄에 "error"라는 단어가 포함되어 있다면,
    if (re.search("error", line)):
        # 해당 줄을 'g' 파일에 쓰고, 다음 줄로 이동합니다.
        g.write(line + "\n")
    
    # 다음 줄을 읽어옵니다.
    line = f.readline()

# 파일을 닫습니다.
f.close()
g.close()





