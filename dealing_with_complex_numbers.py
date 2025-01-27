import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self, no):
        real_part=self.real+no.real
        imaginary_part=self.imaginary+no.imaginary
        return Complex(real_part, imaginary_part)
        
    def __sub__(self, no):
        real_part=self.real-no.real
        imaginary_part=self.imaginary-no.imaginary
        return Complex(real_part, imaginary_part)
        
    def __mul__(self, no):
        real_part=self.real*no.real-self.imaginary*no.imaginary
        imaginary_part=self.real*no.imaginary+self.imaginary*no.real
        return Complex(real_part, imaginary_part)

    def __truediv__(self, no):
        real_part=(self.real*no.real+self.imaginary*no.imaginary)/(pow(no.real,2)+pow(no.imaginary,2))
        imaginary_part=(self.imaginary*no.real-self.real*no.imaginary)/(pow(no.real,2)+pow(no.imaginary,2))
        return Complex(real_part, imaginary_part)

    def mod(self):
        real_part=math.sqrt(pow(self.real,2)+pow(self.imaginary,2))
        return Complex(real_part,0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')