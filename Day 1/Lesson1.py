from os import remove
from turtle import *
speed(8)

#construction of the house

pensize(4)
penup()

left(180)
forward(250)

left(90)
forward(300)

left(180)

pendown()

color ("silver")
begin_fill()

forward(300)
right(90)

forward(220)
right(90)

forward(300)
right(90)

forward(220)
color("grey")
end_fill()

penup()
right(180)
forward(220)

left(30)

pendown()

color("silver")
begin_fill()

forward(300)

left(60)
forward(200)

left(100.7)
forward(265)

color("grey")
end_fill()

# saxuravi
color("silver")
begin_fill()

right(54.5)
forward(160)

left(90.5)
forward(153)

left(133.3)
forward(222)

color("grey")

end_fill()

begin_fill()
color("silver")

left(11)
forward(265)

left(128)
forward(135)

left(46.6)
forward(276)

left(130)
forward(162)

end_fill()

# windows

color("white")
begin_fill()

penup()

goto(-220,-150)

pendown()
pensize(3)

left(44.5)
forward(55)

left(90)
forward(100)

left(90)
forward(55)

left(90)
forward(100)

color("silver")

end_fill()

color("white")
goto(-195,-150)

left(180)
forward(100)

penup()

color("white")
goto(-120,-150)

pendown()

begin_fill()

right(90)
forward(55)

left(90)
forward(100)

left(90)
forward(56)

left(90)
forward(100)

color("silver")
end_fill()

penup()

goto(-95,-150)

pendown()
color("white")

left(180)
forward(100)

penup()

# karebi
color("white")
goto(-169,-298)

pendown()
begin_fill()

forward(100)

right(90)
forward(50)

right(90)
forward(100)

right(90)
forward(50)

color("silver")
end_fill()

penup()

color("black")
goto(-163,-250)

pendown()

left(180)
forward(8)

end_fill()

# side windows :d
penup()
left(180)
color("white")
goto(10,-150)
right(158)

pendown()
begin_fill()

forward(190)

left(68)
forward(76)

left(105)
forward(183)

left(75)
forward(100)
color("silver")
end_fill()

penup()

goto(10,-100)

pendown()
color("white")

left(108)
forward(185)

# remove pen
penup()
goto(1000,1000)
pendown()

exitonclick()