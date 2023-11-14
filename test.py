# test.py

result = 3 + 5
print(result)
    
strA="python is powerful"

print(strA[0:6])
print(strA[:6])
print(strA[-1])
print(strA[-3:])
print(strA[-8:])
print(strA[7:18])

colors=["red","green","blue","white","yellow"]
print(colors)
colors.sort()
print(colors)

def calc(a,b):
    return a+b, a*b

result=calc(5,6)
print(result)
print("------ dictionary ---------")
device={"아이폰":5, "아이패드":10, "윈도우타블렛":20}
print(device)
device["맥프레"]=15
print(device)
device["아이폰"]=6
print(device)