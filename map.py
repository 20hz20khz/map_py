# How to use the map class...
# 1.) create a map instance: map = Map()
# 2.) draw/redraw the map: map.draw(rooms,roomitems,mylocation,100)
# Don't wanna show your roomitems? Comment out line 42

from turtle import *
import math

class Map(Turtle):
  def __init__(self):
    Turtle.__init__(self)
    self.speed(0)
    self.penup()
    self.screen = Screen()
    self.size = 400
    self.screen.setup(self.size,self.size)
    self.screen.tracer(0)
    self.screen.bgcolor("black")
    self.screen.register_shape("bigdiamond",((0,9),(3,3),(9,0),(3,-3),(0,-9),(-3,-3),(-9,0),(-3,3)))
    self.screen.register_shape("lildiamond",((0,3),(1,1),(3,0),(1,-1),(0,-3),(-1,-1),(-3,0),(-1,1)))

  # use the draw method to draw and redraw the map
  def draw(self,rooms,roomitems,mylocation,columnheight):
    rowwidth = int(math.ceil(len(rooms) / columnheight))
    self.penup()
    self.clear()
    for row in range(rowwidth):
      for column in range(columnheight):
        try:
          if rooms[column*columnheight+row]:
            self.color('white')
            self.shape("square")
            self.goto(-self.size/2+10+column*21,self.size/2-10-row*21)
            self.stamp()
        except:
          pass
        if mylocation == column*columnheight+row:
            self.color('red')
            self.shape("bigdiamond")
            self.stamp()
        try:
          if roomitems[column*columnheight+row]:
            self.color('gold')
            self.shape("lildiamond")
            self.goto(-self.size/2+10+column*21,self.size/2-10-row*21)
            self.stamp()
        except:
          pass
    self.screen.update()
