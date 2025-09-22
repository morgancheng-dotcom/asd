# import the turtle module
import turtle
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

print("making a circle...")

# ask user for a color (such as red, green, blue, pink, purple)
color = input("Would color would you like?")
painter.pencolor(color)
radius = input("How big do you want the radius to be?")
# draw a circle with the radius and line color entered by the user
painter.color(color)
painter.circle(int(radius))
# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()