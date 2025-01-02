# numbers=[22,32,34,56,77,88]
# def even(numbers):
#   return numbers%2==0
# evens=list(filter(even,numbers))
# print(evens)  
        
# Same work like this 
# numbers=[22,32,34,56,77,88]
# evens=list(filter(lambda x:x%2==0,numbers))
# print(evens)

# numb=[1,2,3,4,5,6,7,8]
# even=list(filter(lambda x: x%2==0,numb))
# print("The list of even numbers ",even)

# numb=[1,2,3,4,5,6,7,8]
# odd=list(filter(lambda o:o%2!=0,numb))
# print("the list of odd numbers is ",odd)




# Q print the all cities according to their length
# city=["Dadu","Hydrabad","Karachi","Sukkar","Hyd","shikarpur"]
# def length(city):
#     return len(city)
# sort=sorted(city,key=length)
# print(sort)

# Same work like this 
# city=["Dadu","Hydrabad","Karachi","Sukkar","Hyd","shikarpur"]
# sort=sorted(city,key=lambda x:len(x),reverse=True)
# print(sort)



doller=83 
 
def cun():
    result=0
    pk=input("Enter rupees")
    print("in  us currancy ",result=pk*doller)
    print(result)
cun()



              
























