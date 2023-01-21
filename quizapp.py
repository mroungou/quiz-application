
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
}


# looping through the list
for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label,  alternative in enumerate(sorted_alternatives):
        print(f" {label}) {alternative}")

    # int() because input returns a string
    answer_label = int(input(f"{question}? "))
    answer = sorted_alternatives[answer_label]
    if answer == correct_answer:
        print('Correct!')
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
