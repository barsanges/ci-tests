"""
Set of functions allowing to recreate Monthy Python's "Cheese shop".
"""

import numpy as np

def basicanswer(question=None):
    """
    Give the answer "No." to the question `question` (whatever it is).

    Example:
    --------
    >>> basicanswer("Do you have some cheddar?")
    'No.'
    """
    return "No."

def elaborateanswer(question):
    """
    Give an elaborate, realitisc and Michael-Palin-like answer to the
    question `question`.

    Examples:
    ---------
    >>> elaborateanswer("Do you have some cheddar?")
    'No.'
    >>> elaborateanswer("The camembert is indeed runny.")
    '<Nods.>'
    """
    if question.endswith('?'):
        return "No."
    else:
        return "<Nods.>"

def stochasticanswer(question, answers=None):
    """
    Give an answer chosen at random in `answers` to the question
    `question`.
    """
    # The main purpose of this function is to use numpy.
    if answers is None:
        answers = ["No."]
    randindex = np.random.randint(len(answers))
    return answers[randindex]

def dialog(questions, answerfunc):
    """
    Create a dialog made of:
    - questions asked by a so-called "customer",
    - and answers given by a so-called "owner".

    Parameters:
    -----------
    - questions: strings iterable
    - answerfunc: function
        Return an answer (i.e.: a string) for each element of
        `questions`.
    """
    text = []
    for question in questions:
        text.append("Customer: " + question)
        text.append("Owner: " + answerfunc(question))
    text.append("Customer: <Kill the owner.>")
    return '\n'.join(text)
