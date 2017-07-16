import urllib
import xml.etree.ElementTree as ET

url= 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_181968.xml'

uh = urllib.urlopen(url)
data = uh.read()
stuff = ET.fromstring(data)
lst=stuff.findall('.//count')

counter=0
for number in lst:
	counter += int(number.text)
	
print('Retrieving: %s' % url)
print('Retrieved: %s characters' % len(data) )
print('Count: %s' % len(lst))	
print('Sum: %s' % counter)

