"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jeremy Roy.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

jeff = rg.SimpleTurtle("turtle")
jeff.pen = rg.Pen('green', 5)
jeff.speed = 10

size = 420

for k in range(13):
    jeff.draw_circle(size)
    jeff.pen_up()
    jeff.forward(15)
    jeff.right(29)
    jeff.pen_down()

    size = size - 69

greg = rg.SimpleTurtle()
greg.pen = rg.Pen('red', 10)
greg.speed = 6

size = 341

for k in range(17):
    greg.draw_square(size)
    greg.pen_up()
    greg.forward(19)
    greg.right(23)
    greg.pen_down()

    size = size - 65



