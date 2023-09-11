
import turtle as trtl

bear = trtl.Turtle()
bear.begin_fill()
bear.circle(5)
bear.end_fill()

'''
# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []


# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
# Set up lists for changing turtle shapes and turtle colors horizontally
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)
# Set up lists for changing turtle shapes and turtle colors vertically
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
# change the angle of direction turtles go
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions
for step in range(50):
  for ht in horiz_turtles:
    for vt in vert_turtles:
      ht.forward(3)
      vt.forward(3)
      if (abs(ht.xcor() - vt.xcor()) < 20):
        horiz_turtles.remove(ht)
      if (abs(ht.ycor() - vt.ycor()) < 20):
        vert_turtles.remove(vt)
'''
wn = trtl.Screen()
wn.mainloop()
