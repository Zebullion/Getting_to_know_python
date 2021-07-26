from turtle import Turtle, Screen 
#make turtle and screen and determine sidelength
t = Turtle() 
s = Screen()
s.bgcolor('green')
t.color('red')
#sideLength: int = float(input('Give a side length: '))
sideLength = s.numinput('Input','Give a number')
# draw square

for x in range(4):
  t.forward(sideLength)
  t.rt(90)   
  t.forward(sideLength)
  
sideNum = 0
while sideNum <4:
  t.forward(sideLength*2)
  t.rt(90)   
  t.forward(sideLength*2)
  sideNum+=1

t.right(180)
while sideNum <8:
  t.forward(sideLength*2)
  t.rt(90)   
  t.forward(sideLength*2)
  sideNum+=1

for x in range(4):
  t.forward(sideLength)
  t.rt(90)   
  t.forward(sideLength)