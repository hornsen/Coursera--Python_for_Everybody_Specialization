import urllib
fhand = urllib.urlopen('http://py4inf.com/code/romeo.txt')

counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1
		print(word)

print(counts)
