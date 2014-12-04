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

