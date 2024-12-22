# # when we call function inside the same functio 

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return(n* factorial(n-1))

# print(factorial(6))


def facbonic(n):
    if n==0:
        return 0
    else:
        return (    (n-1))+(facbonic(n-2))
    


print(facbonic(6))