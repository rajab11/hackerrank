"""
For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.

The real and imaginary precision part should be correct up to two decimal places.

Input Format

One line of input: The real and imaginary part of a number separated by a space.

Output Format

For two complex numbers  and , the output should be in the following sequence on separate lines:


For complex numbers with non-zero real and complex part, the output should be in the following format:

Replace the plus symbol  with a minus symbol  when .

For complex numbers with a zero complex part i.e. real numbers, the output should be:

For complex numbers where the real part is zero and the complex part is non-zero, the output should be:

Sample Input

2 1
5 6
Sample Output

7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
Concept

Python is a fully object-oriented language like C++, Java, etc. For reading about classes, refer here.

Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality.

__add__-> Can be overloaded for + operation

__sub__ -> Can be overloaded for - operation

__mul__ -> Can be overloaded for * operation
"""
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