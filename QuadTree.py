from importlib.abc import Traversable
from numpy import true_divide
from NbodySimulation import *;
import pprint

from vpython import *
class QuadTree:
    def __init__(self, canvas):
        self.root = Node(self)
        self.lines = []
        self.canvas = canvas
        
    def __str__(self):
        dict = {"root": self.traverseToDict(self.root)}
        return pprint.pformat(dict)
    
    def toDict(self, payload,):
        if not isinstance(payload, Node):
            return payload
        else:
            return {
                "quad1": self.traverseToDict(payload.quad1),
                "quad2": self.traverseToDict(payload.quad2),
                "quad3": self.traverseToDict(payload.quad3),
                "quad4": self.traverseToDict(payload.quad4)
            }
            
    def deleteLines(self):
        for line in self.lines:
            self.canvas.delete(line)

class Node(QuadTree):
    def __init__(self, tree):
        self.tree = tree
        self.width = 0
        self.quad1 = []
        self.quad2 = []
        self.quad3 = []
        self.quad4 = []
        self.m = 0
        self.cg = vector(0,0,0)
        
    def constructTree(self, bodies, xMin, xMax, yMin, yMax, conversionRatio, addGrid):
        if len(bodies) <= 1:
            return bodies
        else:
            xMid = (xMin + xMax)/2
            yMid = (yMin + yMax)/2
            
            self.width = xMax - xMin
            #uncomment this if you don't want to show quadtree lines
            if (addGrid):
                self.draw(xMin, xMax, yMin, yMax, xMid, yMid, conversionRatio)
            
            for body in bodies:
                pos = body.position
                self.m += body.mass
                self.cg += pos*body.mass
                if pos.x < xMid and pos.y < yMid:
                    self.quad1.append(body)
                elif pos.x >= xMid and pos.y < yMid:
                    self.quad2.append(body)
                elif pos.x < xMid and pos.y >= yMid:
                    self.quad4.append(body)
                elif pos.x >= xMid and pos.y >= yMid:
                    self.quad3.append(body)
            
            self.cg /= self.m
            self.quad1 = Node(self.tree).constructTree(self.quad1, xMin, xMid, yMin, yMid, conversionRatio, addGrid)
            self.quad2 = Node(self.tree).constructTree(self.quad2, xMid, xMax, yMin, yMid, conversionRatio, addGrid)
            self.quad3 = Node(self.tree).constructTree(self.quad3, xMid, xMax, yMid, yMax, conversionRatio, addGrid)
            self.quad4 = Node(self.tree).constructTree(self.quad4, xMin, xMid, yMid, yMax, conversionRatio, addGrid)
            return self
        
    def draw(self, xMin, xMax, yMin, yMax, xMid, yMid, conversionRatio):
        xMin *= conversionRatio
        xMax *= conversionRatio
        yMin *= conversionRatio
        yMax *= conversionRatio
        xMid *= conversionRatio
        yMid *= conversionRatio
        
        self.tree.lines.append(self.tree.canvas.create_line(xMid, yMin, xMid, yMax, fill = "Black", width = 1))
        self.tree.lines.append(self.tree.canvas.create_line(xMin, yMid, xMax, yMid, fill = "Black", width = 1))
        