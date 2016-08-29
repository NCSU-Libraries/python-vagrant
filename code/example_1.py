#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import os
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import urllib.request

# Create pdf directory
if not os.path.exists('pdf_files/'):
    os.makedirs('pdf_files/')

list_requests = ['https://scholar.google.com/scholar?hl=en&q=static+analysis+tools&btnG=&as_sdt=1%2C34&as_sdtp=', 'https://scholar.google.com/scholar?start=10&q=static+analysis+tools&hl=en&as_sdt=0,34', 'https://scholar.google.com/scholar?start=20&q=static+analysis+tools&hl=en&as_sdt=0,34']

# TODO: iterate over list_requests
r = requests.get(list_requests[0])
data = r.text

soup = BeautifulSoup(data, 'html.parser')

for script in soup(['script', 'style']):
    script.extract()

text = soup.get_text()
# print(text)

# Subtask 1
wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud)
plt.axis("off")
print('Close the graphic window to continue.')
plt.show()

# Subtask 2
urls = []

# for link in soup.find_all('a'):
#     item = link.get('href')
#     urls.append(item)

for link in soup.find_all('a'):
    if link.get('data-clk') != None and link.get('href') != None:
        if '.pdf' in link.get('href'):
            item = link.get('href')
            urls.append(item)

for url in urls:
    print(url)
    current_link = url
    file_name = current_link[7:]
    file_name = file_name.replace("/", "")
    file_name = file_name.replace(".","")
    fn = file_name + ".pdf"
    # print(fn)

    # Subtask 3
    try:
        response = requests.get(current_link)
        file = open('pdf_files/' + fn, 'wb')
        file.write(response.content)
        file.close
    except:
        print("Oops! Could not download " + current_link + "!")
        pass
