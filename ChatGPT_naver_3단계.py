# 크롤링한 결과를 openpyxl라이브러리를 사용해서 엑셀 파일로 저장해줘. 파일이름은 c:\work\blog.xlsx로 저장해줘


import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

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

        # Create a new workbook and add a worksheet
        workbook = Workbook()
        worksheet = workbook.active

        # Write headers to the worksheet
        worksheet.append(["Blog Address", "Blog Name", "Post Title", "Posting Date"])

        # Loop through the blog entries and add data to the worksheet
        for entry in blog_entries:
            blog_address = entry.find('a', class_='sh_blog_title').get('href')
            blog_name = entry.find('a', class_='sh_blog_title').get_text(strip=True)
            post_title = entry.find('a', class_='sh_blog_title').get('title')
            posting_date = entry.find('dd', class_='txt_inline').get_text(strip=True)

            # Add data to the worksheet
            worksheet.append([blog_address, blog_name, post_title, posting_date])

        # Save the workbook to the specified file
        file_path = r"c:\work\blog.xlsx"
        workbook.save(file_path)

        print(f"Page {page} data saved to {file_path}")

    else:
        # Print an error message if the request was not successful
        print("Error:", response.status_code)

# Loop through pages 1 to 100
for page in range(1, 101):
    crawl_blog_entries("iPhone 15", page)