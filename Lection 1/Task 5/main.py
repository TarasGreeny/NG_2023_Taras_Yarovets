print ("Formula quadratic equation: ax^2+bx=c\n Specify the numbers to substitute them into the formula and solve it: ")
a = int(input("Input first number(a)- "))
b = int(input("Input second number(b)- "))
c = int(input("Input third number(c)- "))
D = pow(b,2)-(4*a*c)
if D < 0:
    print ("There are two roots\n х1: {}".format (-(b-pow(D, 0.5))/(2*a)))
    print ("x2: {}".format (-(b-pow(D, 0.5))/(2*a)))
elif D == 0:
    print ("There is only one root: {}".format (-(b)/(2*a)))
elif D > 0:
    print ("There are two roots\n х1: {}".format (-(b-pow(D, 0.5))/(2*a)))
    print ("x2: {}".format (-(b+pow(D, 0.5))/(2*a)))