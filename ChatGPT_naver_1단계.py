# ChatGPT_naver_1단계.py

# search_keyword = "아이폰15"
# https://search.naver.com/search.naver?where=view&sm=tab_jum&query=search_keyword
# 파이썬에서 BeautifulSoup라이브러리를 사용해서 search_keyword로 검색어를 입력받아서
# 블로그주소, 블로그명, 글의 제목, 포스팅날짜를 크롤링하는 코드를 작성해줘

import requests
from bs4 import BeautifulSoup

# Define the search keyword
search_keyword = "iPhone 15"

# Create the search URL
search_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"

# Send an HTTP request to the search URL
response = requests.get(search_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract information from the parsed HTML
    blog_entries = soup.find_all('li', class_='sh_blog_top')

    # Loop through the blog entries and print relevant information
    for entry in blog_entries:
        blog_address = entry.find('a', class_='sh_blog_title').get('href')
        blog_name = entry.find('a', class_='sh_blog_title').get_text(strip=True)
        post_title = entry.find('a', class_='sh_blog_title').get('title')
        posting_date = entry.find('dd', class_='txt_inline').get_text(strip=True)

        # Print the information
        print("Blog Address:", blog_address)
        print("Blog Name:", blog_name)
        print("Post Title:", post_title)
        print("Posting Date:", posting_date)
        print("\n---\n")

else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)