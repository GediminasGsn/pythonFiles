a = 0
while a < 10:
    a = a + 1
    print (a)

x = 10
while x != 0:
    print (x)
    x = x - 1
print ("We've counted x down,and it now equals",x)
print ("And the loop has now ended")

y = 1
if y == 1:
    print("y still equals 1, I was just checking")
    print("------------------------------------------")
    print("We are going to show you the even numbers up to 20")
    n = 1
    while n <= 20:
        if n % 2 == 0:
            print (n)
        n = n + 1
    print("done")
    print("------------------------------------------")
# 1 means loop. Anything else means dont loop.
loop = 1
#users choice
choice = 0

while loop == 1:
    #options for user to pick
    print("Welcome to calculator")
    print("Your options are:")
    print("")
    print("1)Addition")
    print("2)Subtraction")
    print("3)Multiplication")
    print("4)Division")
    print("5)Exit")
    print("")

    choice = int(input("Chose your option:"))
    
    if choice == 1:
        add1 = int(input ("Add this:"))
        add2 = int(input("to this:"))
        print (add1,"+", add2, "=", add1+add2)
    elif choice == 2:
        sub1 = int(input("Subtract this:"))
        sub2 = int(input("to this:"))
        print (sub1, "-", sub2, "=", sub1-sub2)
    elif choice == 3:
        mul1 = int(input("Multiply this:"))
        mul2 = int(input("to this:"))
        print (mul1,"x", mul2, "=", mul1*mul2)
    elif choice == 4:
        div1 = int(input("Divide this:"))
        div2 = int(input("to this:"))
        print (div1,"/", div2, "=", div1/div2)
    elif choice == 5:
        loop = 0
        print("See you next time!")



