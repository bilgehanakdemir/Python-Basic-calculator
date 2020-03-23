def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y
# User input
X = int(input("Enter your first number please: "))
select = input("Enter operator to use:")
Y = int(input("Enter your second number please: "))
if select == '+':
   print(X,"+",Y,"=", add(X,Y))
elif select == '-':
   print(X,"-",Y,"=", subtract(X,Y))
elif select == '*':
   print(X,"*",Y,"=", multiply(X,Y))
elif select == '/':
   print(X,"/",Y,"=", divide(X,Y))
else:
 print("invalid operator")