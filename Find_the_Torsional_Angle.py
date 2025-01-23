import math

class Points(object):
    def __init__(self, x, y, z):

    def __sub__(self, no):

    def dot(self, no):

    def cross(self, no):
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)