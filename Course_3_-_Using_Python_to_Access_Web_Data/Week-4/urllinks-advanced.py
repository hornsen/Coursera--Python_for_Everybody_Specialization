import urllib
from bs4 import BeautifulSoup

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_181971.html'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup('span')

for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   print 'Attrs:',tag.attrs

