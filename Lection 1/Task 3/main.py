print ("Please, write your temperature and choose what do you want to translate this into? (°C or °F)")
b = int(input("Write your temperature: "))
a = int(input("Write what your temperature is measured in C(write 0) or F(write 1): "))
if a==0:
    sum = (b*9/5)+32
    print ("Here is your result in Celsius: ", sum )
if a==1:
    sum = (b-32)*5/9
    print ("Here is your result in Fahrenheit: ", sum )