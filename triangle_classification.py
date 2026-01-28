# a,b,c are the sides of the triangle
# equilateral triangle has all sides the same
# isosceles triangle has two sides the same
# scalene triange has all different sides 

import pytest 

def classify_triangle(a,b,c):

#Used a sort function to ensure the largest side is always for "c" side 
#as to test a right triangle the longest cide is "c"
    sides = sorted([a,b,c])
    a,b,c = sides

    if a + b <= c or a+c <= b or b +c <=a:
        return "This is not a form of triangle."
    if a <= 0 or b<=0 or c<=0:
        return "This is not a form of triangle."
    if a == b == c:
        return "The triangle is equilateral"
    if a==b or a==c or b==c:
        return "The triangle is isosceles"
    if a*a +b*b == c*c:
        return "The triangle is right"
    if a!=b and a!=c and b!=c:
        return "The triangle is scalene"

# Test to check if it can tell if it is a form of triangle. a+b<=c 3+2<=5, 5=5
def test_l ():
    assert classify_triangle (3,2,5) =="The triangle is equilateral" 

#Test to check if it tell if it is a triangle if one of the sides is 0.
def test_2 ():
    assert classify_triangle (3,0,3) =="The triangle is equilateral"

def test_3 ():
    assert classify_triangle (3,3,3) =="The triangle is equilateral"

def test_4 ():
    assert classify_triangle (2,1,2) == "The triangle is isosceles"

#Test to see if it will return equilateral or isosceles triangle. It should return equilateral.
def test_5 ():
    assert classify_triangle (4,4,4) == "The triangle is isosceles"

def test_6 ():
    assert classify_triangle (4,4,2) == "The triangle is isosceles"

def test_7 ():
    assert classify_triangle (4,3,2) == "The triangle is scalene"

#Test to check if the triangle is right and if it sorted the sides since 5 should be for "c" side
def test_8 ():
    assert classify_triangle (3,5,4) == "The triangle is right"
