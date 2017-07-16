import urllib
from bs4 import BeautifulSoup

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_181971.html'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

tags = soup('span')
count=0

for tag in tags:
   count += int(tag.contents[0])

print(count)
