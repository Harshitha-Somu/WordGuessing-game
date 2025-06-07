import itertools 
import random

user = 0
system = 0

def read_elements_from_file(file_path):
    with open(file_path, 'r') as file:
        elements = file.readlines()
    return [element.strip() for element in elements]

def permutate(word): 
    permutations = itertools.permutations(word)
    return [''.join(p) for p in permutations]

def game(words):
    answer = random.choice(words).strip()
    permutations = permutate(answer)
    shuffled_word = random.choice(permutations)
    
    print("\nYour word is 👉👉:", shuffled_word)
    guess = input("Your answer 🤔🤔: ").strip()

    check_points(guess, answer, words)

def check_points(guess, answer, words):
    global user, system
    if guess.lower() == answer.lower():
        user += 1
        print("Great job! You got 1 point 🥳")
    else:
        system += 1
        print(f"Oops! System got 1 point 🙂. The correct word was: {answer}")
    
    print("Your score:", user)
    print("System score:", system)
    
    choice = input("\nDo you want to play another round? (yes/no): ").strip().lower()
    if choice == "yes":
        game(words)
    else:
        print("\nFinal Result:")
        if user > system:
            print("You Won 🥳🥳🥳")
        elif user < system:
            print("System Won 🤗🤗")
        else:
            print("It's a Tie!")

# MAIN
input_file = "list_of_words.txt"
elements = read_elements_from_file(input_file)
game(elements)
