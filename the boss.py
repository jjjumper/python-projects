'''

var counter;

    for (counter = 1; counter <= 300; counter++) {
    penColour(colour_random());
   moveForward(counter);
   turnRight(121);}
'''



from turtle import Turtle

yorktown = Turtle

yorktown.pensize(9)
yorktown.pencolor(lime)

for count in range(1,600):
    yorktown.foward(count)
    yorktown.right(121)
