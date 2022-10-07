from vpython import vector
from QuadTree import *

#some predefined constants
G = 6.67408e-11
objectDensity = 600 #kg/m3
dt = 1000

class Space:
    def __init__(self, width, height, canvas, grid):
        self.width = width
        self.height = height
        self.canvas = canvas
        self.xBound = ( float("+inf"), float("-inf") )
        self.yBound = ( float("+inf"), float("-inf") )
        self.bodies = []
        self.collided = False
        self.tree = None
        self.grid = grid

    def advance(self):
        for body in self.bodies:
            xMin, xMax = self.xBound
            yMin, yMax = self.yBound
            self.xBound = min(body.position.x, xMin), max(body.position.x, xMax)
            self.yBound = min(body.position.y, yMin), max(body.position.y, yMax)
            body.updatePosition()

    def mergeBody(self, b1, b2):
        if b1.mass > b2.mass:
            b1.velocity.x = (b1.mass*b1.velocity.x + b2.mass*b2.velocity.x)/(b1.mass + b2.mass)
            b1.velocity.y = (b1.mass*b1.velocity.y + b2.mass*b2.velocity.y)/(b1.mass + b2.mass)
            b1.updateMass(b2.mass)
            self.bodies.remove(b2)
            self.tree.deleteLines()

            #reconstruct the tree
            del self.tree
            self.tree = QuadTree(self.canvas)
            xMin, xMax = self.xBound
            yMin, yMax = self.yBound
            self.tree.root.constructTree(self.bodies, xMin, xMax, yMin, yMax, self.width/5000e6, self.grid)
            self.canvas.delete(b2.obj)

    def convertToDisplayVal(self, val):
        val = val*self.width/5000e6
        return val

    def draw(self):
        for body in self.bodies:
            radius = self.convertToDisplayVal(body.radius)
            x = self.convertToDisplayVal(body.position.x)
            y = self.convertToDisplayVal(body.position.y)
            self.canvas.coords(body.obj, x - radius, y - radius, x + radius, y + radius)

class Body:
    def __init__(self, position, velocity, mass, space):
        self.position = position
        self.velocity =  velocity
        self.mass = mass
        self.radius = self.massToRadius(mass)
        self.space = space
        self.obj = space.canvas.create_oval(position.x-self.radius,
            position.y-self.radius,
            position.x+self.radius,
            position.y+self.radius,
            outline="",
            fill="blue")

    def massToRadius(self, mass):
        return (3 * mass / (4*pi*objectDensity))**(1/3)

    #quadtree method to calculate acceleration
    def aQuadTree(self, currNode, pos):
        theta = 1
        if isinstance(currNode, list):
            if currNode == [] or currNode[0] == self:
                return vector(0,0,0)
            else:
                body = currNode[0]
                self.checkCollision(body)
                r = body.position - pos
                return norm(r) * G * body.mass / (mag(r)**2)
        else:
            r = currNode.cg - pos
            if currNode.width/mag(r) < theta:
                return norm(r) * G * currNode.m / (mag(r)**2)
            else:
                return self.aQuadTree(currNode.quad1, pos) + self.aQuadTree(currNode.quad2, pos) + self.aQuadTree(currNode.quad3, pos) + self.aQuadTree(currNode.quad4, pos)

    def checkCollision(self, body):
        r = body.position - self.position
        if mag(r) < body.radius + self.radius:
            self.space.collided = True
            self.space.mergeBody(self, body)
            self.space.collided = False

    def updatePosition(self):
        position1 = self.position
        k1 = self.aQuadTree(self.space.tree.root, position1)
        position2 = self.position + self.velocity * dt * 0.5 + k1 * (dt/2)**2 * 0.5
        k2 = self.aQuadTree(self.space.tree.root, position2)
        position3 = self.position + self.velocity * dt * 0.5 + k2 * (dt/2)**2 * 0.5
        k3 = self.aQuadTree(self.space.tree.root, position3)
        position4 = self.position + self.velocity * dt + k3 * (dt)**2 * 0.5
        k4 = self.aQuadTree(self.space.tree.root, position4)

        a = (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        self.position += self.velocity * dt + a * dt**2 * 0.5
        self.velocity += a * dt

    def updateMass(self, addMass):
        self.mass += addMass
        self.radius = self.massToRadius(self.mass)
