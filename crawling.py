# crawling.py

f = open('c:\\work\\webtoon.txt', 'a+', encoding='utf-8')
for item in cartoons:
    title = item.find('a').text
    print(title)
    f.write(title+'\n')

    