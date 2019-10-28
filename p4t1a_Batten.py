#CTI110
#Repeating Squares
#Shyann Batten
#10/09/19
#
import turtle

turtle.right(180)

turtle.speed(0)

length = 505

for times in range (100):
    for endtimes in range (4):
        turtle.forward(length)
        turtle.right(90)
    length -= 5
