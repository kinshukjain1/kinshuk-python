import shapes 

print("Choose Shapes:")
print("1. Circle")
print("2. Rectangle")           
print("3. Triangle")
choice = int(input("Enter your choice (1-3): "))    

if choice == 1:
    r = float(input("Enter the radius of the circle: "))
    area_circle = shapes.circle_area(r)
    print("The area of the circle is: ", area_circle)   

elif choice ==2:
    l = float(input("Enter the length of the rectangle:"))
    w = float(input("Enter the width of the rectangle:"))
    area_rectangle = shapes.rectangle_area(l,w)
    print("The area of the rectangle is:", area_rectangle)

elif choice == 3:
    b = float(input("Enter the base of triangle:"))
    h = float(input("Enter the height of triangle:"))
    area_triangle = shapes.triangle_area(b,h)
    print("The area of the triangle is:", area_triangle)

else:
    print("Invalid choice")
    
    
