# cities=("dadu","hyd","karachi","sukkar")
# op=list(cities)        # here we have converted a tuple into a list
# op.pop(3)              #to remove something
# op.append("nawabshah") # to add something
# op[2]="larkana"        # here we are going to add larkana at index 2
# cities=tuple(op)       # here again we have convarted list into a tuple 
# print(type(cities),cities)



# tup=(1,2,3,4,5,3,3,3,3)
# # res=tup.count(3)
# res=tup.index(3)# here it will show that on which index does 3 exists
# print(res)








# list1=["which is the capital city"]
# score=0
# print(list1[0])
# ans=str(input("Enter The answer "))
# if ans=='islamabad':
#     print("Thats correct Answer")
#     score=score+1
# else:
#     print("You are rong")
#     score=score-1







# score =0
# list1=['which is the capital city of pakistan','islamabad','who is the founder of pakistan','quaid']
# print(list1[0])
# ans=str(input("Answer : "))
# if ans==list1[1]:
#     print("Your anser is correct")
#     score=score+100
# elif ans==str(input("Answer :"))==list1[3]:
#     print("You are rong")
#     score=score-100
# print(list1[2])







 

score=0
totalCorrect=0
list1=[]

print(list1.append("Which is the capital city of pakistan"))
print("A : karachi ") 
print(" B :Lahore ") 
print(" c :Islamabad")
print("D : None")

ans =str(input("Enter your answer : "))

if ans=='a':
        print("Correct")
        score=score+100
        totalCorrect=totalCorrect+1
else:
        score=score-100
       

print(list1.append("Who is the founder of pakistan"))

print("A : Allama iqbal")
print("B : Quaid -e- Azam")
print("C : Liquat Ali khan")
print("D : Sir Syed Ahmed Khan")

ans =str(input("Enter your answer : "))

if ans=='a':
        score=score+100
        totalCorrect=totalCorrect+1
else:
        score=score-100
       

print(list1.append("Which the Hottest City of Pakistan"))

print("A : Larkana ")
print("B : Sibi ")
print("C : Dadau")
print("D : Karachi")

ans =str(input("Enter your answer : "))

if ans=='B':
        score=score+100
        totalCorrect=totalCorrect+1
else:
        score=score-100


print(list1.append("Who is the Current Prime minister of Pakistan"))

print("A : Nawaz Sharif")
print("B : Asif ZArdai")
print("C : Imran khan")
print("D : Shahbaz Shareef")

ans =str(input("Enter your answer : "))

if ans=='d':
        score=score+10000
        totalCorrect=totalCorrect+1
else:
        score=score-100


print("Your total score is " ,score)
print("Total correct Answers : ",totalCorrect)




























































