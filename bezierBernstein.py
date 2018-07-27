from graphics import *
from math import factorial

# Draw lines from the points set
def drawLines(ptSet, color, window, width):
  for i in range(len(ptSet)):
    if i < len(ptSet) - 1:
      pt1 = ptSet[i]
      pt2 = ptSet[i + 1]
      ln = Line(pt1, pt2)
      ln.setOutline(color)
      ln.setWidth(width)
      ln.draw(window)

# Calculate the result of Bernstein Polynomial
def bernstein(n, j, t):
  return (factorial(n) / (factorial(j) * factorial(n - j))) * (t ** j) * ((1 - t) ** (n - j))


def main():
  # Initialize window
  win = GraphWin("Bezier Curve (Bernstein)", 512, 512)
  win.setBackground(color_rgb(255, 255, 255))

  ptList = []  # Create a list for control points
  sampleCount = 10  # Number of points on the curve

  while True:
    mouseCoord = win.getMouse()  # Get the coordinates when the mouse is clicked

    if mouseCoord:
      # Draw a white rectangle to clear the previous result if the mouse is clicked
      windowClearer = Rectangle(Point(0, 0), Point(512, 512))
      windowClearer.setOutline(color_rgb(255, 255, 255))
      windowClearer.setFill(color_rgb(255, 255, 255))
      windowClearer.draw(win)

      # Draw a point based on the mouse's coordinates
      pt = Point(mouseCoord.x, mouseCoord.y)
      pt.setOutline(color_rgb(0, 0, 0))
      pt.draw(win)
      print(pt)

      ptList.append(pt)  # Add the point to the control points list
      controlPointsCount = len(ptList)
      n = controlPointsCount - 1
 
    if controlPointsCount > 1:
      drawLines(ptList, color_rgb(200, 200, 200), win, 1) # Draw periphery lines

      bList = [] # Create a list for points on the curve

      # Calculate points on the curve
      for k in range(sampleCount + 1):
        t = k / sampleCount
        
        # Reset b
        bX = 0
        bY = 0

        # Calculate the point on the curve using Bernstein Polynomials
        for j in range(n + 1):
          bX += ptList[j].x * bernstein(n, j, t)
          bY += ptList[j].y * bernstein(n, j, t)

        # Draw a point on the curve
        b = Point(bX, bY)
        b.setOutline(color_rgb(255, 0, 0))
        b.draw(win)
        bList.append(b)

      # Draw Beizer curve
      drawLines(bList, color_rgb(0, 0, 0), win, 1)


# Run the program
main()
