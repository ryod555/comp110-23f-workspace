"""Drawing a beautiful gorgeous hexagonal butterfly using turtle!"""
 
__author__ = "730660144"
 
from turtle import Turtle, tracer, update, colormode, done 
doug: Turtle = Turtle()
colormode(255)


def hexagon(turt: Turtle, x: float, y: float, width: float) -> None:
    """Draws a hexagon."""
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    i: int = 0
    while i < 6:
        turt.forward(width)
        turt.left(60)  # The angles of a shape add up to 360, so a shape with 6 equal sides would have each angle 60 degrees.
        i += 1


def octagon(turt: Turtle, x: float, y: float, width: float) -> None:
    """Draws an octagon."""
    turt.pensize(2)
    turt.pencolor(35, 0, 35)
    turt.fillcolor(0, 255, 255)
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.begin_fill()
    i: int = 0
    while i < 8:
        turt.forward(width)
        turt.left(45)  # The angles of a shape add up to 360, so a shape with 6 equal sides would have each angle 60 degrees.
        i += 1
    turt.end_fill()
            

def draw_wings(x_start: float, y_start: float, x_axis: float, y_axis: float, hex_width: float, outline: bool) -> None:
    """Draws a line of scaling vertical hexagons, creating a wing shape."""
    i: int = 0
    blue: int = 50
    green: int = 120
    while i < 10:
        if outline:  # if the boolean parameter is set to true, the color will be set to blue, if not, the color will be black.
            doug.color(29, green, blue)
        else: 
            doug.color(0, 0, 0)
        doug.begin_fill()
        hexagon(doug, x_start, y_start, hex_width)
        doug.end_fill()
        i += 1
        x_start += x_axis  # x_axis is the increment it adds each time, the distance between the prior hexagon, depending on if the float is positive or negative, goes a different dirrecton. 
        y_start += y_axis
        hex_width += 10
        blue += 15
        green -= 5  # these change the color with each loop, creating a smooth gradient.


def draw_body(x: int, y: int, width: int) -> None:
    """Draws a line of hexagons for the body of the butterfly."""
    i: int = 0
    doug.color("black")
    while i < 2:
        doug.begin_fill()
        hexagon(doug, x, y, width - 10)
        doug.end_fill()
        i += 1
        y += 40
    while i < 6:
        if i == 2:
            x -= 10
        doug.begin_fill()
        hexagon(doug, x, y, width + 10)
        doug.end_fill()
        i += 1
        y += 30
    while i < 8:
        if i == 6:
            x -= 10
        doug.begin_fill()
        hexagon(doug, x, y, width + 20)
        doug.end_fill()
        i += 1
        y += 20  # The first 2 hexagons will be the least wide, the next 4 will be medium width and the last 4 will be most wide but also closer together. This creates a scaling model of hexagons, looking similar to the tail, body and head of the butterfly!
        

def antenna(turt: Turtle, x: float, y: float, side: bool, width: int) -> None:
    """Draws an antenna using methods learned to draw a hexagon, with slight adjustments."""
    doug.penup()
    doug.goto(x, y)
    doug.pensize(width)  # function which was not mentioned in the turtorial! also, a parameter width will let me give the antennas a white outline.
    doug.pendown()
    i: int = 0
    if side:
        doug.goto(x + 10, y + 20)
        while i < 13:
            doug.forward(40 - i * 3)  # the distance traveled with each loop with become smaller as the index increases.
            doug.left(60)
            i += 1
    else:
        doug.goto(x - 10, y + 20)
        while i < 13:
            doug.backward(40 - i * 3)  
            doug.right(60)  # going right with each loop with reflect the antenna
            i += 1


def background() -> None:
    """Technically doesnt need to be its own function, but cleans up main() a little. Creates a background using a hexagonal gradient pattern."""
    blue: int = 0
    green: int = 255
    red: int = 0
    i: int = 0
    doug.pensize(20)
    doug.goto(0, 0)
    while i < 150:
        doug.pencolor(red, green, blue)
        doug.forward(i * 4)  # exponentially gets larger with each loop.
        doug.left(60)  # will create a hexagonal gradient background
        i += 1
        if i % 6 == 0:
            blue += 10
            green -= 10
            red += 5  # after a hexagon is completed, the color will slightly change with the variables refrencing the blue and green rgb values of the turtle.
    doug.pensize(0)
        

def main() -> None:
    """Constructing the butterfly out of functions created."""
    doug.speed(0)
    background()
    tracer(0, 0)

    draw_wings(-5, -10, 10, 10, 60, False)
    draw_wings(-55, -10, -20, 10, 60, False)
    draw_wings(-5, -60, 10, -20, 60, False)
    draw_wings(-55, -60, -20, -20, 60, False)  # creates a black outline of the butterfly by using the almost same code as the wings but with a larger width
    
    draw_wings(0, 0, 10, 10, 50, True)
    draw_wings(-50, 0, -20, 10, 50, True)
    draw_wings(0, -50, 10, -20, 50, True)
    draw_wings(-50, -50, -20, -20, 50, True)

    draw_body(-20, -105, 50)

    octagon(doug, 190, 210, 40)
    octagon(doug, 130, 150, 20)
    octagon(doug, 210, 110, 20)

    octagon(doug, -210, 210, 40)
    octagon(doug, -150, 150, 20)
    octagon(doug, -230, 110, 20)

    octagon(doug, 190, -210, 40)
    octagon(doug, 130, -150, 20)
    octagon(doug, 210, -110, 20)

    octagon(doug, -210, -210, 40)
    octagon(doug, -150, -150, 20)
    octagon(doug, -230, -110, 20)
    
    #  For the functions which i repeated multiple times but in different axis, i adjusted the x and y's positive/negative value, and tweaked the placement a little because turtle got a weird angle or somethin.

    doug.pencolor("white")
    antenna(doug, 30, 220, True, 5)
    antenna(doug, -30, 220, False, 5)

    doug.pencolor("black")
    antenna(doug, 30, 220, True, 4)
    antenna(doug, -30, 220, False, 4)

    update()
    done()


if __name__ == "__main__":
    main() 
