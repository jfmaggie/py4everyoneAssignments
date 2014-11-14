'''
	read from file that user asked for, count the
	number of each word and sort alphabetically
'''
file = raw_input('Enter the file name:')
fhand = open(file)
text = fhand.read()
words = text.split()

counts = dict()
for wrd in words:
	counts[wrd] = counts.get(wrd,0) + 1
	#print wrd, counts[wrd]

#print counts.items()

li = list()

for key, val in counts.items():
	li.append((key,val))
	li.sort()
	 

print li