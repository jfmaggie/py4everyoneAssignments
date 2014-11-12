text = "X-DSPAM-Confidence:    0.8475";

l = list()
num = ('0','1','2','3','4','5','6','7','8','9')
for char in num:
	index = text.find(char,0, len(text))
	
	if index != -1:
		l.append(index)
		

float_num = float(text[min(l):(max(l)+1)])
print float_num
