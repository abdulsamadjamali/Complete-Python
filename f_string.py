# data="Hello my name is {} and i am from {}"
# name="abdul samad jamali"
# country="Pakistan"
# print(data.format(name,country))





# data="Hello my name is {0} and i am from {1}"
# name="abdul samad jamali"
# country="Pakistan"
# print(data.format(country,name))





# a="Hi {} where are you going i was waiting for {}"
# b=str(input("Who is going"))
# c=str(input("Waiting for whom"))
# print(a.format(b,c))


# price=20
# data=f"The real price of this toy is {price:.2f}$"
# print(data)


# price=89.4567777 
# data=f"ok so this is the real price of this toy {price :.2f}" here it will only the two letters after the decimal
# print(data)





# docstring ************************

def square (n):
    ''' this function will gives us the square of number which we will enter'''
    print(n**2)
print(square.__doc__)
square(44)

















