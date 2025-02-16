# print("Wellcome to the simpe calculator")
# while True:
 
#  num1=int(input("Please enter first num1"))
#  num2=int(input("Please enter second num2"))

#  print("Choose operation (+,-,*,/)")
#  operator=input("operator")

#  match operator:
#     case "+":
#         print("The addition of both number is ",num1+num2)
    
#     case "-":
#         print("The subtraction of both number is ",num1-num2)
#     case "*":
#         print("The multiplication of both num",num1*num2)
#     case "/":
#        if num2!=0:
#           print("The division is ",num1/num2)
#        else:
#           print("Inavlid ")
#  condi=input("press Y to continue  and E to exit ").upper()
#  if condi=="E":
#     print("Exist Sucessfully")
    # break
# import random

# def Guess_numb():
#     print("You have to select a number between 0 and 10. Can you guess it?")
    
#     while True:
#         RandomNumb = random.randint(0, 10)
#         count = 0
        
#         while True:
#             count += 1
#             guess = int(input("Enter your guess: "))
            
#             if guess == RandomNumb:
#                 print(f"Correct! You guessed it in {count} attempts.")
#                 break
#             elif guess > RandomNumb:
#                 print("Too High")
#             else:
#                 print("Too Low")
        
#         conti = input("Do you want to continue? (Y/N): ").upper()
#         if conti == "Y":
#             continue
#         else:
#             print("Thanks for playing!")
#             break

# Guess_numb()

nested_tuple=((1,2,3),(3,4,5),"Abdul samad jamali")


# print(str(my_tuple))
# print(nested_tuple[2])

grades=("A","A+","A","B","B+",)
Agrades=grades.count("A")
index=(grades.index("A"))
print(Agrades)
print(index)






















 







