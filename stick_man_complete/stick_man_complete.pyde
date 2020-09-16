# completed stick figure
# change each of the given functions so they accept parameters

def drawHead(x, y):
    """Circle head
    x is the x-coordinate of the centre of the circle
    y is the y-coordinate of the centre of the circle
    """
    ellipse(x, y, 25, 25)


def drawBody(x, y):
    """Stick body
    x is the x-coordinate of the first point of the line
    y is the y-coordinate of the first point of the line
    """
    line(x, y, x, y + 30)


def drawArms(x, y):
    """Stick arms
    x is the x-coordinate of the first point of the left arm
    y is the y-coordinate of the first point of the left arm
    """
    line(x, y, x - 30, y - 7)
    line(x, y, x + 30, y - 7)


def drawLegs(x, y):
    """Stick legs
    x is the x-coordinate of the first point of the left leg
    y is the y-coordinate of the first point of the left leg
    """
    line(x, y, x - 15, y + 45)
    line(x, y, x + 15, y + 45)


size(200, 200)
# call the functions that draw the image below with the specified arguements
# draws the head centered at (100, 35)
drawHead(100, 35)
# draws the body starting at (100, 50) and ending at (100, 80)
drawBody(100, 50)
# draws the arms starting at (100, 52)
drawArms(100, 52)
# draws the legs starting at (100, 80)
drawLegs(100, 80)
