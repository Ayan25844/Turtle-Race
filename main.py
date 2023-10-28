import random
from turtle import Turtle,Screen

turtles=[]
start_race=False

screen=Screen()
screen.setup(500,400)
colors=["red","orange","yellow","green","blue","purple"]
bet=screen.textinput("Make your bet","Which turtle will win the race? Enter a color: ")

for i in range(0,len(colors)):
    participant=Turtle("turtle")
    participant.penup()
    turtles.append(participant)
    participant.color(colors[i])
    participant.goto(-235,-100+(i*50))

if bet:
    start_race=True

while start_race:
    for i in turtles:
        if i.xcor()>230:
            start_race=False
            if bet==i.pencolor():
                print(f"You have won! The {bet} turtle is the winner!")
            else:
                print(f"You have lost! The {i.pencolor()} turtle is the winner!")
        i.fd(random.randint(0,10))
        
screen.exitonclick()