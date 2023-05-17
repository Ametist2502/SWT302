def func2(x,y):
     if((1 > x > 0) and (y < 0)):
          return x + y
     elif(x > 1):
          return x*y
     else:
          return x-y

x = float(input("Enter x: "))
y = float(input("Enter y: "))
     
print(func2(x,y))