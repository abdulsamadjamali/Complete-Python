import random

def Guess_numb():
    print("You have to select a number between 0 and 10. Can you guess it?")
    
    while True:
        RandomNumb = random.randint(0, 10)
        count = 0
        
        while True:
            count += 1
            guess = int(input("Enter your guess: "))
            
            if guess == RandomNumb:
                print(f"Correct! You guessed it in {count} attempts.")
                break
            elif guess > RandomNumb:
                print("Too High")
            else:
                print("Too Low")
        
        conti = input("Do you want to continue? (Y/N): ").upper()
        if conti == "Y":
            continue
        else:
            print("Thanks for playing!")
            break

Guess_numb()
