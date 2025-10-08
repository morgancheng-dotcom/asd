# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
num_of_legs = 6
length_of_legs = 70
direction_of_legs = 380 / num_of_legs
spider.pensize(5)
n = 0
while (n < num_of_legs):
  spider.goto(0, 0)
  spider.setheading(direction_of_legs * n)
  spider.forward(length_of_legs)
  n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()