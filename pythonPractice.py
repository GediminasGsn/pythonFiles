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
def hello():
    print("hello")
    return 1234
print (hello())



