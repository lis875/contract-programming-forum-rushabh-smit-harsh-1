import random

def choose_level(user_input):
    levels = ['beginner', 'intermediate', 'advanced']
    if user_input in levels:
        return user_input
    elif user_input == 'exit':
        return 'exit'
    else:
        return 'invalid'

def get_vocabulary_words(level):
    if level == 'beginner':
        return [
            ("Arduous (adj.)", ["taxing", "difficult"]),
            ("Alacrity (noun)", ["lively", "zeal"]),
            ("Bolster (v.)", ["support", "strengthen"]),
            ("Pragmatic (adj.)", ["realistic", "practical"]),
            ("Waver", ["oscillate", "fluctuate"])
        ]
    elif level == 'intermediate':
        return [
            ("Banal (adj.)", ["boring", "cliche"]),
            ("Avarice (noun)", ["greed"]),
            ("Capricious (v.)", ["unpredictable"]),
            ("Credulous (adj.)", ["gullible", "naive"]),
            ("Ephemeral", ["short-lived", "fluctuate"])
        ]
    elif level == 'advanced':
        return [
            ("anodyne (adj.)", ["inoffensive"]),
            ("cow (v.)", ["to intimidate"]),
            ("encumber (v.)", ["hold back"]),
            ("penurious (adj.)", ["miserly"]),
            ("unstinting (adj.)", ["very generous"])
        ]

def check_answer(word, user_input, synonyms):
    return user_input in synonyms

def main():
    print("Welcome to the GRE Vocabulary Flashcards Program!")
    counter = 0
    while True:
        if counter == 0:
            level_input = input("\nChoose a level (Beginner/Intermediate/Advanced) or 'exit': ").lower()
        else:
            level_input = input("\nChoose a level to continue or 'exit': ").lower()

        level = choose_level(level_input)

        if level == 'exit':
            print("Exiting the program. Goodbye!")
            break
        elif level == 'invalid':
            print("Invalid level. Please choose a valid level or type 'exit' to exit.")
            continue

        vocabulary_words = get_vocabulary_words(level)
        random.shuffle(vocabulary_words)
        score = 0

        for word, synonyms in vocabulary_words:
            print(f"\nWord: {word}! Guess a synonym:")
            user_input = input().lower()
            if check_answer(word, user_input, synonyms):
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. Synonyms: {', '.join(synonyms)}")

        print(f"\nScore: {score}/{len(vocabulary_words)}")
        counter += 1

if __name__ == "__main__":
    main()

import pytest


def test_choose_level():
    assert choose_level('beginner') == 'beginner'
    assert choose_level('intermediate') == 'intermediate'
    assert choose_level('advanced') == 'advanced'
    assert choose_level('exit') == 'exit'
    assert choose_level('random') == 'invalid'

def test_get_vocabulary_words():
    assert isinstance(get_vocabulary_words('beginner'), list)
    assert isinstance(get_vocabulary_words('intermediate'), list)
    assert isinstance(get_vocabulary_words('advanced'), list)

def test_check_answer():
    synonyms = ["synonym1", "synonym2"]
    assert check_answer("word", "synonym1", synonyms) == True
    assert check_answer("word", "wrong", synonyms) == False


test_choose_level()
test_get_vocabulary_words()
test_check_answer()

# Additional tests can be written for other aspects of the program
