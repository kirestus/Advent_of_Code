#read the input file
input = open('input.txt', 'r')

#arange each line into a list
with input as f:
	boxsize = f.readlines()

#variable to total the sq feet
total = 0
#run the equation on each box
for box in boxsize:
	value = box.split('x')
	l = int(value[0])
	w = int(value[1])
	h = int(value[2])
		
	if (l*w <= l*h) and (l*w <= h*w):
		smallest = l*w
	elif (h*w <= l*w) and (h*w <= l*h):
		smallest = h*w
	else:
		smallest = h*l
	
	#the amount of paper per box
	sum = (2*l*w)+(2*w*h)+(2*h*l)+smallest
	#add the box to the total
	total += sum
		
print total
