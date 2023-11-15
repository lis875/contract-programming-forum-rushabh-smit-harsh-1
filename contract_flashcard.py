import random

print("")
print("Welcome to the GRE Vocabulary Flashcards Program!")
print("This program is designed to help you enhance your English vocabulary skills for the GRE exam.")
print("Vocabulary words are categorized into three levels: Beginner, Intermediate, and Advanced.")
print("Each flashcard will present a word, and you can try to recall its meaning.")
print("Let's get started!\n")
counter = 0

while True:
    if (counter == 0):
        level = input("\nPlease choose the difficulty level to start with (Beginner / Intermediate / Advanced) or type 'exit' to exit the program: ").lower()
    else:
        level = input("\nTo continue practicing please choose Beginner, Intermediate, or Advanced. or type 'exit' to exit the program: ").lower()


    # Check if the user wants to exit
    if level == 'exit':
        print("\nExiting the program. Goodbye!")
        break

    elif level == 'beginner':
        print("Welcome to the beginner module")

        # List of vocabulary words and their synonyms by Smit
        vocabulary_words = [
            ("Abscond (adj.)", ["escape", "flee"]),
            ("Abstruse (noun)", ["difficult", "abstract"]),
            ("Benign (v.)", ["mild", "light"]),
            ("Pragmatic (adj.)", ["realistic", "practical"]),
            ("Castigate", ["chastise", "scold"])
        ]

    elif level == 'intermediate':
        print("Welcome to the Intermediate module")

        # List of vocabulary words and their synonyms by Rushabh
        vocabulary_words = [
            ("Banal (adj.)", ["boring", "Cliche"]),
            ("Avarice (noun)", ["greed"]),
            ("Capricious (v.)", ["unpredictable"]),
            ("Credulous (adj.)", ["gullible", "naive"]),
            ("Ephemeral", ["short-lived", "fluctuate"])
        ]

    elif level == 'advanced':
        print("Welcome to the Advanced module")

         # List of vocabulary words and their synonyms by Harsh
        vocabulary_words = [
            ("anodyne (adj.)", ["inoffensive"]),
            ("cow (v.)", ["to intimidate"]),
            ("encumber (v.)", ["hold back"]),
            ("penurious (adj.)", ["miserly"]),
            ("unstinting (adj.)", ["very generous"])
        ]

    else:
        print("\nInvalid level. Please choose Beginner, Intermediate, or Advanced  or type 'exit' to exit the program:")
        continue

    # Shuffle the order of words
    random.shuffle(vocabulary_words)

    # Initialize the score
    score = 0

    # Loop through each vocabulary word
    for word, synonyms in vocabulary_words:
        print(f"\nLet's tackle the word {word}! Can you think of a synonym?")
        user_input = input().lower()

        # Check if the user's input is correct
        if user_input in synonyms:
            print("Awesome! You nailed it!")
            score += 1
        else:
            print(f"Oops! The correct answer is {', '.join(synonyms)}")

    # Display the final score and a concluding message
    print(f"\nYour journey through {level} words has concluded!\nYour score is {score}/{len(vocabulary_words)}")
    print("Thank you for the test. Keep expanding your vocabulary!")
    counter = counter + 1 #to change the default message on running the loop once