import tkinter
import pyautogui
from NbodySimulation import *
import random as rd
from vpython import vector
import time
from QuadTree import *


#some predefined constants
G = 6.67408e-11
objectDensity = 600 #kg/m3
initialLightestBodyMass = 1.0224e+22 #kg
initialHeaviestBodyMass = 2.1469e+24 #kg
initialMinBodySpeed = 241.02 #m/s
initialMaxBodySpeed = 4075.8 #m/s
width, height = pyautogui.size()
N = 0
dt = 0
addGrid = False

  

def create_animation_window():
  Window = tkinter.Tk()
  Window.title("N-body simulation")

  Window.geometry(f'{width}x{height}')
  return Window
 

def create_animation_canvas(Window):
  canvas = tkinter.Canvas(Window)
  canvas.configure(bg="White")
  canvas.pack(fill="both", expand=True)
  return canvas

def populateCanvas(canvas):
    mySpace = Space(width, height, canvas, addGrid)
    mySpace.tree = QuadTree(canvas)
    for i in range(N):
        velocity = vector.random().norm() * rd.uniform(initialMinBodySpeed, initialMaxBodySpeed)
        velocity.z = 0
        x = rd.uniform(0, 5000e6)
        y = rd.uniform(0, 5000e6*height/width)
        position = vector(x, y, 0)
        mass = rd.uniform(initialLightestBodyMass, initialHeaviestBodyMass)
        newBody = Body(position, velocity, mass, mySpace)
        mySpace.bodies.append(newBody)
    return mySpace

def display_time(seconds, granularity=3):
    result = []

    intervals = (
        ('weeks', 604800),  # 60 * 60 * 24 * 7
        ('days', 86400),    # 60 * 60 * 24
        ('hours', 3600),    # 60 * 60
        ('minutes', 60),
        ('seconds', 1),
    )

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])

def animate(canvas, Window, space, dt):
  t = 0
  while(True):
    while not space.collided:
        mySpace.tree = QuadTree(canvas)
        xMin, xMax = space.xBound
        yMin, yMax = space.yBound
        mySpace.tree.root.constructTree(space.bodies, xMin, xMax, yMin, yMax, width/5000e6, addGrid)
        space.advance()
        space.draw()
        timer = canvas.create_text(30, 30, text=f'elapsed time: {display_time(t)}', fill="black", font=('Arial'), anchor=tkinter.SW)
        time.sleep(0.01)
        Window.update()
        mySpace.tree.deleteLines()
        canvas.delete(timer)
        del mySpace.tree
        t += dt

if __name__ == "__main__":  
  print("-------------Nbody-Simulation--------------")
  print("Author: Minh Pham Dinh - Colby College     ")
  print()
  N = int(input("Number of particles (N): "))
  dt = int(input("Time step (s) (recommend 1000): "))
  addGrid = input("show quadtree grid lines? (y/n): ") == "y" if True else False
  print()
  print("-------------Nbody-Simulation--------------")

  Animation_Window = create_animation_window()
  Animation_canvas = create_animation_canvas(Animation_Window)
  mySpace = populateCanvas(Animation_canvas)
  animate(Animation_canvas, Animation_Window, mySpace, dt)