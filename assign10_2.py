'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.

output:
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

li = list()
li_a = list()
li_s = list()
hours = dict()
for line in handle:
	line.rstrip()
	if line.startswith('From '):
		a = line.split()
		#print a[5]
		li.append(a[5])

for str in li:
    hr = str.split(':')
    del hr[1:]
    li_a.append(hr[0])

for wrd in li_a:
    hours[wrd] = hours.get(wrd,0) + 1
    #print wrd, hours[wrd]

#print li,'\n', li_a,'\n', hours

for k,v in hours.items():
    li_s.append((k,v))
    li_s.sort()
    
for num in li_s:
    print num[0],num[1]
   
    
    
    
