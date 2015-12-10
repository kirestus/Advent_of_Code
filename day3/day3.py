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
   	if spot not in visited:
   		visited.append(spot)
	if not c:
		print visited
		#added one to account for starting on 0,0
		print len(visited)+1
		break
	print spot, c



