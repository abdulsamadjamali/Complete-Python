# def average( *number):
#     sum=0
#     for i in number:
#         sum =sum+i
#     print("Average is ",sum/len(number))

# average(1,2,3,4,5,6)


# def avg(*numb)://here numb is used as a tuple 
#     sum =0
#     for i in numb:
#         sum=sum+i
#     return sum/len(numb)

# a=avg(1,2,3)
# print(a)


# def fun():
#     try:
#         b=[1,2,3,4,5]
#         a=int(input("Enter a number"))
#         print("Print the number",b[a])
#         return 1

#     except:
#         print('No any error')
#         return 0
#         # print("GGGG")
#     finally:
#         print("KUCH B HO MANA TO PRINT HONA E HA ")
    

# fun()









# cUSTOM errOR


a=input("Enter a number between 5 and 9")
if( a!="quit" or a>9 or a<5  ):
  raise ValueError("Invalid numb")
else:
  print('hello')

