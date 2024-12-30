# mark=[89,98,77,54,33,22,63]
# def result(mark):
#     if mark>85:
#         return "A+"
#     elif mark<85 and mark>70:
#         return "A"
#     elif mark>50 and mark<70:
#         return "B"
#     elif mark<50 and mark>33:
#         return "C"
#     else:
#         return "F"
    
# marks=list(map(result,mark))
# print("The result is : ",marks)


# marks=[55,77,89,98]
# def failing(score):
#     return score<60
# result=list(filter(failing,marks))
# print(result)

# numb=[11,22,34,65,56,88]
# def even(numb):
#     if numb%2==0:
#         return "Even"
#     else:
#         return "Odd"
# result=list(map(even,numb))
# print(result)

numb=[21,33,44,65,77,88,99]
def greater(numb):
    return numb>50
   
     
 
result=list(filter(greater,numb))
print(result)





































