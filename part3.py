# Name: Xuenan Xu
# uniqname: xuenanxu
# UMID: 35069066

# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py

# get HTML page content of Michigan Daily site by using request, and parse the page into BeautifulSoup format
base_url = "https://www.michigandaily.com/"
page_content = requests.get(base_url).text
soup = BeautifulSoup (page_content, 'html.parser')

# create two lists to store the url and article titles of the most read articles
most_read_url = []
most_read_name = []

i = 0
for j in soup.ol.contents:
	i += 1
	if (i % 2 == 1):
		most_read_name.append(j.string.strip())
		most_read_url.append(base_url + j.a['href'])

# creat a list to store the author names
author_name = []

# request author data
for url in most_read_url:
	article_page_content = requests.get(url).text
	article_soup = BeautifulSoup(article_page_content, 'html.parser')

	# find title element by using div class 
	author = article_soup.find('div',class_="byline")

	# if the author name is on the page
	if(author != None):
		author_str = author.next_element.next_element.next_element.string
		author_name.append(author_str)
	# if the author name is not on the page
	else:
		author_name.append("Unknown Author")

#print out data
print("Michigan Daily -- MOST READ")

def most_read_print():
	j = 0
	while (j < len(author_name)):
		print(most_read_name[j])
		print("   by " + author_name[j])
		j = j + 1

most_read_print()


