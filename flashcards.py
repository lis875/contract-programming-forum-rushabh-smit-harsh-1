import random
name = input("Hello, Enter your Name: ")
print("Hi", name, "Welcome to the FLASHCARD Game of python libraries!!!!!!")
print("")
print("Please make sure to enter your answers WITHOUT brackets -> ()")
print("Let's Beginnnnnnn")
print("")

flashcard = [
    ("What returns the length (the number of items) of an object:", "len"),
    ("What returns the type of an object:", "type"),
    ("What prints objects to the text stream file:", "print"),
    ("What return the largest item in an iteration:", "max"),
    ("What opens file and return a corresponding file object:", "open"),
    ("How to add values to the end of a list:", "append"),
    ("How to add an element to a list at a given position:", "insert"),
    ("How to remove an item using the index:", "del"),
    ("How to remove all the items in a dictionary:", "clear"),
    ("What is 22 % 8", "6"),
    ("What keyword is used to define a class?", "class"),
    ("What command is used to load a Python module?", "import"),
    ("What Return the smallest item in an iterable.", "min")
]

count_wrong = 0
count_right = 0
random.shuffle(flashcard)
asked_flashcard = set()

while (len(flashcard) > 0):
    for question in flashcard:
        if question not in asked_flashcard:        
            print(question[0])
            answer = input("What is the answer? ")
            if answer == question[1]:
                print("Correct!") 
                count_right += 1
            else:
                print("Incorrect! The answer is " + question[1])
                count_wrong += 1
            asked_flashcard.add(question)
    break

print("")
print("Right answer : " , count_right)
print("Wrong answer : " , count_wrong)    