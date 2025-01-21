number = 5
count=0
guess = None
print("Guess the number!")
while guess != number:
    guess =int(input("Is it... "))
    count+=1
    if count ==10:
        print("“Sorry, you ran out of attempts :(")
        break

    if guess ==number:
        print("Wow! You guessed it right!")
    if guess ==number and count<=3:
        print("You are an amazing guesser!")
    elif guess < number:
        print("Opps, It's bigger...")
    elif guess > number:
        print("Opps, It's not so big.")