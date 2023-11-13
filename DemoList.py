# DemoList.py
colors=["red","green","blue"]
print(colors)
print(type(colors))
print(len(colors))

colors.append("white")
print(colors)


colors.insert(1,"pink")
print(colors)

print(colors.index("pink"))

colors+=["red"]
print(colors)

#colors+="red"
#print(colors)

print(colors.count("red"))
print(colors.pop())
print(colors.pop(1))
print(colors)

colors.remove("blue")
print(colors)

colors.extend(["black", "yellow", "green"])
print(colors)

colors.sort()
print(colors)

print(colors.count("green"))
print("test")
print(colors)
colors.pop(2)
print(colors)
colors.reverse()
print(colors)

#디버깅할 때 중단점(break point)
for item in colors:
    print(item)