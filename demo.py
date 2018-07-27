from graphics import *

def main():
  win = GraphWin("My Window", 500, 500)
  win.setBackground(color_rgb(255, 255, 255)) # Set the color of BG to white

  cirCentre = Point(250, 250) # Create a point at (250, 250)
  cir = Circle(cirCentre, 20) # Set center point at pt, radius as 50
  cir.setFill(color_rgb(0, 0, 0)) # Set the color of the circle to black
  cir.draw(win) # Draw the circle in win

  pt1 = Point(250, 350)
  pt2 = Point(300, 300)
  pt3 = Point(100, 200)
  pt4 = Point(200, 100)
  """
  pt1.setOutline(color_rgb(0, 0, 0))
  pt2.setOutline(color_rgb(0, 0, 0))
  pt1.draw(win)
  pt2.draw(win)
  """

  ln = Line(pt1, pt2)
  ln.setOutline(color_rgb(100, 100, 100))
  ln.setWidth(3)
  ln.draw(win)

  rect = Rectangle(pt3, pt4)
  rect.setOutline(color_rgb(200, 0, 0))
  rect.setFill(color_rgb(255, 100, 50))
  rect.draw(win)

  poly = Polygon(Point(400, 100), Point(450, 150), Point(350, 300))
  poly.setOutline(color_rgb(255, 100, 255))
  poly.setFill(color_rgb(100, 255, 50))
  poly.draw(win)
  
  win.getMouse()
  win.close()

main()
