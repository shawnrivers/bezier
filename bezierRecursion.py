from graphics import *

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

# de Casteljau recursion for X coordinates
def deCasteljauX(r, i, t, controlPtList):
  if r == 0:
    return controlPtList[i].x
  else:
    return (1 - t) * deCasteljauX(r - 1, i, t, controlPtList) + t * deCasteljauX(r - 1, i + 1, t, controlPtList)

# de Casteljau recursion for Y coordinates
def deCasteljauY(r, i, t, controlPtList):
  if r == 0:
    return controlPtList[i].y
  else:
    return (1 - t) * deCasteljauY(r - 1, i, t, controlPtList) + t * deCasteljauY(r - 1, i + 1, t, controlPtList)


def main():
  # Initialize window
  win = GraphWin("Bezier Curve (recursion)", 512, 512)
  win.setBackground(color_rgb(255, 255, 255))

  ptList = [] # Create a list for control points
  sampleCount = 10 # Number of points on the curve

  while True:
    bezierPtList = [] # Create a list for points on the curve
    mouseCoord = win.getMouse() # Get the coordinates when the mouse is clicked

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

      ptList.append(pt) # Add the point to the control points list
      controlPointsCount = len(ptList)
      n = controlPointsCount - 1

    if controlPointsCount > 1:
      drawLines(ptList, color_rgb(200, 200, 200), win, 1) # Draw periphery lines

      # Calculate points on the curve
      for k in range(sampleCount + 1):
        t = k / sampleCount
        
        # Use recursive de Casteljau to calculate the coordinates
        x = deCasteljauX(n, 0, t, ptList)
        y = deCasteljauY(n, 0, t, ptList)

        # Draw a point on the curve
        result = Point(x, y)
        result.setOutline(color_rgb(255, 0, 0))
        result.draw(win)
        bezierPtList.append(result)

      # Draw Beizer curve
      drawLines(bezierPtList, color_rgb(0, 0, 0), win, 1)


# Run the program
main()
