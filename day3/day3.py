#starting variables
visited = list()
x=0
y=0

#read out the file on character at a time
with open('input.txt') as f:
  while True:
	c = f.read(1)
   	if c == '>':
   		x += 1
   	elif c == '<':
   		x -= 1
   	elif c == '^':
   		y+=1
   	elif c == 'v':
   		y-=1
   			
   	spot = (x,y)
   	visited.append(spot)
	if not c:
		print visited
		print len(visited)
		break
	print spot, c



