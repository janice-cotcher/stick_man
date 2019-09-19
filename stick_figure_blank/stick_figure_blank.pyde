# change each of the given functions so they accept parameters

def drawHead():
    """Circle head"""
    ellipse(100, 35, 25, 25)


def drawBody():
    """Stick body"""
    line(100, 50, 100, 80)


def drawArms():
    """Stick arms"""
    line(100, 52, 70, 45)
    line(100, 52, 130, 45)


def drawLegs():
    """Stick legs"""
    line(100, 80, 85, 125)
    line(100, 80, 115, 125)


size(200, 200)
# call the functions that draw the image below with the specified arguements
# draws the head centered at (100, 35)

# draws the body starting at (100, 50) and ending at (100, 80)

# draws the arms starting at (100, 52)

# draws the legs starting at (100, 80)
