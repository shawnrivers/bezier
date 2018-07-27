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

# Linear interpolation
def linearInterpolation(p1, p2, t):
  x = p1.x * (1 - t) + p2.x * t
  y = p1.y * (1 - t) + p2.y * t
  return Point(x, y)


def main():
  # Initialize window
  win = GraphWin("Bezier Curve (iteration)", 512, 512)
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

      for k in range(sampleCount + 1):
        t = float(k) / float(sampleCount)
        b = ptList
        
        # Calculate points on the curve using Linear Interpolation
        for r in range(1, n + 1):
          temp = []
          for i in range(n + 1 - r):
            temp.append(linearInterpolation(b[i], b[i + 1], t))
          b = temp
        
        # Draw a point on the curve
        result = b[0]
        result.setOutline(color_rgb(255, 0, 0))
        result.draw(win)
        bezierPtList.append(result)
        
      # Draw Beizer curve
      drawLines(bezierPtList, color_rgb(0, 0, 0), win, 1)

# Run the program
main()
