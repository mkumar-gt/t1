from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')

for article in soup.find_all('div', class_='article'):

	headline = article.h2.a.text

	article_content = article.p.text

	print(headline)
	print(article_content)

	print()