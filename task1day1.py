import random
# List of words to choose from
word_list = ['python', 'javascript', 'hangman', 'programming', 'openai']
def choose_word():
    return random.choice(word_list)
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])
def hangman():
    word = choose_word()  # Select a random word
    guessed_letters = set()
    incorrect_guesses = set()
    max_incorrect = 6  # Maximum number of incorrect guesses allowed
    print("Welcome to Hangman!")
    while len(incorrect_guesses) < max_incorrect:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Incorrect guesses ({len(incorrect_guesses)}/{max_incorrect}):", ' '.join(incorrect_guesses))
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue
        if guess in guessed_letters or guess in incorrect_guesses:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            guessed_letters.add(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses.add(guess)
        # Check if the player has guessed the word
        if set(word) == guessed_letters:
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")
# Start the game
hangman()
