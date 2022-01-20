tri_ar = lambda b,h: 0.5*b*h
rect_ar = lambda ln, br: ln*br
sq_ar = lambda a : a*a

base = int(input("Enter the base of triangle"))
height = int(input("Enter the height of triangle"))

print(f"Area of triangle {tri_ar(base, height)}")

length = int(input("Enter the length of rectangle"))
breadth = int(input("Enter the breadth of rectangle"))

print(f"Area of rectangle {rect_ar(length, breadth)}")

side = int(input("Enter the length of square"))

print(f"Area of square {sq_ar(side)}")
