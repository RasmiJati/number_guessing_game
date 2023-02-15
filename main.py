secret_number = 10
number_of_guesses = 0
guess_limit = 5
while number_of_guesses < guess_limit:
    guess = int(input("Guess : "))
    number_of_guesses += 1
    if guess == secret_number:
        print("You won !! 🎉🎉✨✨")
        break
else:
    print("You Failed !! 😢😢")

