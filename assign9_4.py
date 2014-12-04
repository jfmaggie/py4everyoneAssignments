''' 9.4 Write a program to read through the mbox-short.txt and figure out who
has the sent the greatest number of mail messages. The program looks for 'From
' lines and takes the second word of those lines as the person who sent the
mail. The program creates a Python dictionary that maps the sender's mail
address to a count of the number of times they appear in the file. After the
dictionary is produced, the program reads through the dictionary using a
maximum loop to find the most prolific committer. 

Output: 
cwen@iupui.edu 5

''' 

name = raw_input("Enter file:") 
if len(name) < 1 : name = "mbox-short.txt" 
handle = open(name)

li = list()
li_sort = list()
maps = dict()
for line in handle:
	line.rstrip()
	if line.startswith('From '):
		a = line.split()
		#print a[1]
		li.append(a[1])

for wrd in li:
	maps[wrd] = maps.get(wrd,0) + 1
	#print wrd, maps[wrd]

for key, val in maps.items():
	li_sort.append((val, key))
	li_sort.sort()

print li_sort[-1][1],li_sort[-1][0]

