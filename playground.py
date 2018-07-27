from graphics import *
import random

# Generate random points
def genRandomPoints(amount, winWid, winLen):
  pointsSet = []
  for i in range(amount):
    x = random.randint(0, winWid)
    y = random.randint(0, winLen)
    point = {"x": x, "y": y}
    pointsSet.append(point)
  return pointsSet

# Draw points from the points set
def drawPointsSet(pointsSet, color, window):
  for point in pointsSet:
    pt = Point(point["x"], point["y"])
    pt.setOutline(color)
    pt.draw(window)

# Draw lines from the points set
def drawLines(pointsSet, color, window, width):
  for i in range(len(pointsSet)):
    if i < len(pointsSet) - 1:
      point1 = pointsSet[i]
      point2 = pointsSet[i + 1]
      pt1 = Point(point1["x"], point1["y"])
      pt2 = Point(point2["x"], point2["y"])
      ln = Line(pt1, pt2)
      ln.setOutline(color)
      ln.setWidth(width)
      ln.draw(window)

# Linear interpolation
def linearInterpolation(p1, p2, t):
  x = p1.x + (p2.x - p1.x) * t
  y = p1.y + (p2.y - p1.y) * t
  return Point(x, y)

def main():
  # Initialize window
  win = GraphWin("Test", 500, 500)
  win.setBackground(color_rgb(255, 255, 255))

  # Drawing settings
  # amount = 50 # Amount of random points
  # pts = genRandomPoints(amount, 500, 500)
  # drawPointsSet(pts, color_rgb(0, 0, 0), win)
  # drawLines(pts, color_rgb(100, 100, 100), win, 1)

  # Maintain points coords
  pointsCoords = []

  while True:
    mouseCoord = win.getMouse()
    pointsCoords.append(mouseCoord)
    mouseX = mouseCoord.x
    mouseY = mouseCoord.y
    mousePt = Point(mouseX, mouseY)
    mousePt.setOutline(color_rgb(0, 0, 0))
    mousePt.draw(win)

    pointsAmount = len(pointsCoords)
    print(pointsAmount)

    # Draw lines
    if pointsAmount > 1:
      pt1 = pointsCoords[pointsAmount - 2]
      pt2 = pointsCoords[pointsAmount - 1]
      print(pt1, pt2)
      ln = Line(pt1, pt2)
      ln.setOutline(color_rgb(200, 200, 200))
      ln.setWidth(1)
      ln.draw(win)
      ptLI = linearInterpolation(pt1, pt2, 0.5)
      ptLI.setOutline(color_rgb(255, 0, 0))
      ptLI.draw(win)


  win.getKey() # Wait for a key press to stop
  win.close()

main()
