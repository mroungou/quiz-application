from string import ascii_lowercase


# storing questions and answers
# each element of the list will have a two-tuple containing the question text and answer
QUESTIONS = {
    "When was the first known use of the word 'quiz'":  [
        "1781", "1771", "1871", "1881"
    ],
    "Which built-in function can get information from the user": [
        "input", "get", "print", "write"
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop"
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user"
    ],
    "How do you iterate over both indices and elements in an iterable": [
        "enumerate(iterable)",
        "enumerate(iterable, start=1)",
        "range(iterable)",
        "range(iterable, start=1)",
    ],

    "What's the offcicial name of the := operator": [
        "Assignment expression",
        "Named expression",
        "Walrus operator",
        "Colon equals operator",
    ],
}

# keeping track of amount of correct answers
correct_num = 0
# looping through the dictionary
for question_number, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {question_number}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label,  alternative in labeled_alternatives.items():
        print(f" {label}) {alternative}")

    # int() because input returns a string
    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        correct_num += 1
        print('⭐ Correct! ⭐')
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

# question_number variable already counts the number of questions in the quiz
# can be used to report the total number of questions that the user has answered
print(f"\nYou got {correct_num} correct out of {question_number} questions")
