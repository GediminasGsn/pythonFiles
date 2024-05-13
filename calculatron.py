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