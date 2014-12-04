'''
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

Output:
0.8475
'''
text = "X-DSPAM-Confidence:    0.8475";

l = list()
num = ('0','1','2','3','4','5','6','7','8','9')
for char in num:
	index = text.find(char,0, len(text))
	
	if index != -1:
		l.append(index)
		

float_num = float(text[min(l):(max(l)+1)])
print float_num
