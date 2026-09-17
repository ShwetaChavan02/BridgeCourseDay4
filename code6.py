#create a menu driven calculator

a=int(input("enter number1:"))
b=int(input("enter number2:"))

print("1:addition")
print("2:subtraction")
print("3:division")
print("4:multiplication")
print("5:exit")

choice=int(input("enter your choice:"))

if choice==1:
    def add(a,b):
        print("addition is :",a+b)
    add(a,b)

if choice==2:
    def sub(a,b):
        print("subtraction is :",a-b)
    sub(a,b)

if choice==3:
    def div(a,b):
        print("division is :",a/b)
    div(a,b)

if choice==4:
    def mul(a,b):
        print("multiplication is :",a*b)
    mul(a,b)

if choice==5:
    print("exiting calculator program")
   
