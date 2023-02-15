secret_number = 10
number_of_guesses = 0
guess_limit = 5
while number_of_guesses < guess_limit:
    guess = int(input("Guess : "))
    number_of_guesses += 1
    chance = guess_limit - number_of_guesses
    print(f"You have got {chance} chance left 😱😰😱")
    if guess == secret_number:
        print("Congratulation. You won !! 🎉🎉✨✨")
        break
else:
    print("You Failed !! 😢😢")

