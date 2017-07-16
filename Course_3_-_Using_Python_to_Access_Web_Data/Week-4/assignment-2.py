# Install BeautifulSoup with:
# sudo pip install beautifulsoup4

import urllib, re
from bs4 import BeautifulSoup

url = raw_input('Enter URL: ')
count = int( raw_input('Enter count: ') )
pos = int( raw_input('Enter position: ') ) - 1

counter = 0
print('Retrieving: %s' % url)
while counter<=count:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html, 'lxml')
	tags = soup('a')
	url=tags[pos].get('href', None)
	
	counter += 1
	
	if(counter < count):
		print('Retrieving: %s' % url)
		
	elif(counter == count):
		print('Last Url: %s' % url)
		print(re.findall('known_by_(.+).html',url)[0])
	




