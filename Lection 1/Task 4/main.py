print ("Input your a and b number and choose what method do you want to solve it: ")
a = int(input("Write first number- "))
b = int(input("Write second number- "))
print ("Select transfer method: ")
c= input()
match c:
    case "+":
        print ("Your number is {}".format(a+b))
    case "-":
        print ("Your number is {}".format(a-b))
    case "*":
        print ("Your number is {}".format(a*b))
    case "/":
        print ("Your number is {}".format(a/b))
    case _:
        print ("Command doesn`t exist")