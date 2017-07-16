import urllib
from bs4 import BeautifulSoup

#url = raw_input('Enter - ')
url = 'http://www.dr-chuck.com/page1.htm'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup('a')

for tag in tags:
	print tag.get('href', None)
