import urllib
fhand = urllib.urlopen('http://py4inf.com/code/romeo.txt')

for line in fhand:
	print(line.strip() )
