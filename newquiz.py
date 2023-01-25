import random
from string import ascii_lowercase

num_questions_per_quiz = 5
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

# this function will handle the questions and the number of questions parametres


def prepare_quiz(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    # this will generate a random sample of questions in whatever order
    return random.sample(list(questions.items()), k=num_questions)

# printing the question, the alternatives, handling user errors

def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
    )
    for label,  alternative in labeled_alternatives.items():
        print(f" {label}) {alternative}")

     # int() because input returns a string
    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]
