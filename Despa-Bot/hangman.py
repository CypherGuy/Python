# from nltk.corpus import words
# import nltk
# import random

# nltk.download('words')


# def generate_proper_word():
#     word_list = words.words()
#     return random.choice(word_list)


# # Generate a list of 200 proper words
# words = list(filter(lambda word: len(word) > 3 and len(word) < 10,
#                     [generate_proper_word() for _ in range(200)]))

# print("Start guessing...")
# word = random.choice(words)
# print(word)
# guesses = ''
# turns = 10

# while turns > 0:
#     failed = 0
#     for char in word:
#         if char in guesses:
#             print(char, end=" "),
#         else:
#             print("_", end=" "),
#             failed += 1
#     if failed == 0:
#         print("You won!")
#         break
#     guess = input("Guess a character:")
#     guesses += guess
#     if guess not in word:
#         turns -= 1
#         print("Wrong")
#         print("You have", + turns, 'more guesses')
#     if turns == 0:
#         print("You Lose")
