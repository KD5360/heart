import turtle as t
t.shape("turtle")
import random

t.up()
t.goto(-250,-250)
t.down()
t.goto(-250,250)
t.goto(250,250)
t.goto(250,-250)
t.goto(-250,-250)
t.up()
t.goto(0,0)
a = random.randint(0,45)
t.setheading(a)
for x in range(1000000000000000000000):   
    while t.xcor() < 250 :
        t.forward(1)    
        ang1 = t.heading()    
        t.setheading(90 + ang1)   
    while t.ycor() < 250 :       
        t.forward(1)    
        ang2 = t.heading()   
        t.setheading(90 + ang2)   
    while t.xcor() > -250:      
        t.forward(1)    
        ang3 = t.heading()    
        t.setheading(90 + ang3)   
    while t.ycor() > -250:       
        t.forward(1)   
        ang4 = t.heading()   
        t.setheading(90 + ang4)
