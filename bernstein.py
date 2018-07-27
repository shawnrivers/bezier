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

# Linear interpolation
def linearInterpolation(p1, p2, t):
  x = p1.x + (p2.x - p1.x) * t
  y = p1.y + (p2.y - p1.y) * t
  return Point(x, y)

# Draw coordinate axis
def drawAxisBox(leftUpPt, rightUpPt, leftDownPt, rightDownPt, window):
  leftLine = Line(leftUpPt, leftDownPt)
  rightLine = Line(rightUpPt, rightDownPt)
  upLine = Line(leftUpPt, rightUpPt)
  downLine = Line(leftDownPt, rightDownPt)

  lineColor = color_rgb(200, 200, 200)
  lineWidth = 1

  leftLine.setOutline(lineColor)
  rightLine.setOutline(lineColor)
  upLine.setOutline(lineColor)
  downLine.setOutline(lineColor)

  leftLine.setWidth(lineWidth)
  rightLine.setWidth(lineWidth)
  upLine.setWidth(lineWidth)
  downLine.setWidth(lineWidth)

  leftLine.draw(window)
  rightLine.draw(window)
  upLine.draw(window)
  downLine.draw(window)

# Convert point in the axis box
def coordShiftPoint(point, origin, scale):
  shiftedX = point.x * scale + origin.x
  shiftedY = -(point.y * scale - origin.y)
  return Point(shiftedX, shiftedY)

# Calculate the result of Bernstein Polynomial
def bernstein(n, i, t):
  return (factorial(n) / (factorial(i) * factorial(n - i))) * (t ** i) * ((1 - t) ** (n - i))

# Draw the graph of Bernstein Polynomial
def drawBernstein(n, sampleCount, leftDownPt, axisBoxSize, window):
  for i in range(n + 1):

    drawnPtList = []

    for j in range(sampleCount + 1):
      x = j / sampleCount
      y = bernstein(n, i, x)
      pt = Point(x, y)
      drawnPt = coordShiftPoint(pt, leftDownPt, axisBoxSize)
      drawnPtList.append(drawnPt)

    drawLines(drawnPtList, color_rgb(0, 0, 0), window, 1)


def main():
  # Initialize window
  windowWidth = 512
  windowLength = 512
  win = GraphWin("Bernstein Polynomial", 512, 512)
  win.setBackground(color_rgb(255, 255, 255))

  axisBoxSize = 400 # Setting for Coordinates grid to draw the graph

  # Four vertices of the axis box drawn
  leftUpPt = Point((windowWidth - axisBoxSize) / 2, (windowLength - axisBoxSize) / 2)
  rightUpPt = Point((windowWidth + axisBoxSize) / 2, (windowLength - axisBoxSize) / 2)
  leftDownPt = Point((windowWidth - axisBoxSize) / 2, (windowLength + axisBoxSize) / 2)
  rightDownPt = Point((windowWidth + axisBoxSize) / 2, (windowLength + axisBoxSize) / 2)

  sampleCount = int((rightDownPt.x - leftDownPt.x) / 10)

  drawAxisBox(leftUpPt, rightUpPt, leftDownPt, rightDownPt, win) # Draw coordinate axis

  n = 3 # Default degree setting

  # Input box to change n
  inputBox = Entry(Point(windowWidth / 2, (windowLength - axisBoxSize) / 4), 20)
  inputBox.setText(3)
  inputBox.setTextColor(color_rgb(0, 0, 0))
  inputBox.setFace("courier")
  inputBox.draw(win)

  # Message text to display the current n
  messageText = "n = " + str(n)
  message = Text(Point((windowWidth - axisBoxSize) / 2, (windowLength - axisBoxSize) / 4), messageText)
  message.setTextColor(color_rgb(0, 0, 0))
  message.setFace("courier")
  message.draw(win)

  drawBernstein(n, sampleCount, leftDownPt, axisBoxSize, win) # Draw the graph of Bernstein Polynomial

  while True:
    # When ENTER is pressed, redraw graph with the new n
    if(str(win.getKey()) == 'Return'):
      n = int(inputBox.getText())
      print(n)

      # Draw a white rectangle to clear window
      windowClearer = Rectangle(Point(0, 0), Point(512, 512))
      windowClearer.setOutline(color_rgb(255, 255, 255))
      windowClearer.setFill(color_rgb(255, 255, 255))
      windowClearer.draw(win)

      drawAxisBox(leftUpPt, rightUpPt, leftDownPt, rightDownPt, win) # Redraw axis

      # Redraw message text
      messageText = "n = " + str(n)
      message = Text(Point((windowWidth - axisBoxSize) / 2, (windowLength - axisBoxSize) / 4), messageText)
      message.setTextColor(color_rgb(0, 0, 0))
      message.setFace("courier")
      message.draw(win)

      
      drawBernstein(n, sampleCount, leftDownPt, axisBoxSize, win) # Redraw the graph of Bernstein Polynomial


# Run the program
main()
