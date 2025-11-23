import random
words = ["python", "developer", "hangman", "codealpha", "internship"]

word = random.choice(words)

guessed_letters = []
attempts = 6

while attempts > 0:
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display.strip())

    if "_" not in display:
        print("🎉 Congratulations! You guessed the word correctly.")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print(f"Incorrect! You have {attempts} attempts left.")
    else:
        print("Good guess!")

if attempts == 0:
    print(f"😞 You ran out of attempts. The word was '{word}'.")
