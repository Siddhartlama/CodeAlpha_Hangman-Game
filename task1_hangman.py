"""
CodeAlpha Internship — Task 1: Hangman Game
"""

import random

WORDS = ["python", "hangman", "coding", "laptop", "rocket"]

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]

def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("\n🎮 Welcome to Hangman!")
    print("Guess the word one letter at a time. You have 6 incorrect guesses.\n")

    while incorrect_guesses < max_incorrect:
        # Display hangman
        print(HANGMAN_STAGES[incorrect_guesses])

        # Display word progress
        display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
        print(f"Word: {display}")
        print(f"Guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}\n")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"🎉 Congratulations! You guessed the word: '{word.upper()}'")
            return

        # Get input
        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try a different letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"✅ Nice! '{guess}' is in the word!\n")
        else:
            incorrect_guesses += 1
            print(f"❌ '{guess}' is not in the word.\n")

    # Game over
    print(HANGMAN_STAGES[max_incorrect])
    print(f"💀 Game Over! The word was: '{word.upper()}'")


def main():
    while True:
        play_hangman()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
