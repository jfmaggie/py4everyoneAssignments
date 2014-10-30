largest = None
smallest = None


while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        value = int(num)
    except:
        print 'Invalid input'
        continue
    if largest is None and smallest is None: 
        largest = value
        smallest = value
    elif value >= largest:
        largest = value
    elif value <= smallest:
        smallest = value
       

print "Maximum is", largest
print "Minimum is", smallest
