import urllib, json

#url = raw_input('Enter location: ') 
url= 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_181972.json'

uh = urllib.urlopen(url)
data = uh.read() 

info = json.loads(data)

counter=0
for x in range(len(info['comments'])):
	counter += info['comments'][x]['count']


print json.dumps(info, indent=4)
print('')

print 'Retrieving: ', url
print 'Retrieved ', len(data),'characters'
print 'Count: ', len( info['comments'] ) 
print 'Sum: ', counter
