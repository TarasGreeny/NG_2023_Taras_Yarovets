print ("Please, write your temperature and choose what do you want to translate this into? (°C or °F)")
temper = int(input("Write your temperature: "))
degree = int(input("Write what your temperature is measured in C(write 0) or F(write 1): "))
if temper==0:
    sum = (degree*9/5)+32
    print ("Here is your result in Celsius: ", sum )
if temper==1:
    sum = (degree-32)*5/9
    print ("Here is your result in Fahrenheit: ", sum )