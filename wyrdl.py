#Unfinished
import pathlib
import random

def get_random_word():
    WORDLIST = pathlib.Path("text files/scramblewords.txt")
    words = list(WORDLIST.read_text(encoding="utf-8").strip().split("\n"))
    return random.choice(words)

def game_over(word):
    print(f"The word was {word}")

def show_guess(guess, word):
    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:".join(sorted(correct_letters)))
    print("\nMisplaced letters:".join(sorted(misplaced_letters)))
    print("\nWrong letters:".join(sorted(wrong_letters)))

def main():
    word = get_random_word()
    for guess_num in range(1, 7):
        guess = input(f"\nGuess {guess_num}: ").upper()
        show_guess(guess, word)
        if guess == word:
            break
    else:
        game_over(word)

if __name__ == "__main__":
    main()