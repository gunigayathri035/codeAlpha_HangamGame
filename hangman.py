import random

# List of 5 predefined words
WORDS = ["python", "computer", "programming", "developer", "internship"]

# Maximum number of wrong guesses
MAX_WRONG_GUESSES = 6


def play_hangman():
    # Select a random word
    word = random.choice(WORDS)

    # Store letters guessed by the player
    guessed_letters = set()

    # Count wrong guesses
    wrong_guesses = 0

    print("================================")
    print("        HANGMAN GAME")
    print("================================")
    print("Guess the word one letter at a time.")
    print("You have 6 chances for wrong guesses.")

    while wrong_guesses < MAX_WRONG_GUESSES:

        # Display guessed letters and hide remaining letters
        display = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in word
        )

        print("\nWord:", display)

        # Check if the complete word has been guessed
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! 🎉")
            print("You guessed the word:", word)
            return

        # Get a letter from the player
        guess = input("Enter a letter: ").lower().strip()

        # Check whether input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        # Check whether the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Add the letter to guessed letters
        guessed_letters.add(guess)

        # Check whether the guess is correct
        if guess in word:
            print("Correct guess! ✅")
        else:
            wrong_guesses += 1
            remaining = MAX_WRONG_GUESSES - wrong_guesses
            print("Wrong guess! ❌")
            print("Remaining chances:", remaining)

    # Player has used all wrong guesses
    print("\nGame Over! 😔")
    print("The correct word was:", word)


# Start the game
if __name__ == "__main__":
    play_hangman()