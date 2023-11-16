# 1페이지에서 100페이지까지 페이징 처리를 하는 코드로 변경해줘

import requests
from bs4 import BeautifulSoup

def crawl_blog_entries(search_keyword, page):
    # Create the search URL with the specified page
    search_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 + 1}"

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

# Loop through pages 1 to 100
for page in range(1, 101):
    print(f"Page {page}:")
    crawl_blog_entries("iPhone 15", page)