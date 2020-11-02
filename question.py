""" 
This file contains a python class meant to initialize a singular question and the answer to it, 
functions capable of determining a correct answer are implemented 
"""

class Question(object):
    def __init__(self):
        """ constructs an empty instance of the question """
        self._question = ""
        self._answer = ""
    
    def set_question(self, question_str):
        """ sets the value of the question string """
        self._question = question_str
    
    def set_answer(self, answer_str):
        """ sets the value of the answer string """
        self._answer = answer_str
    
    def check_answer(self, attempt_str):
        """ returns true if the input answer is the answer to the set question, false otherwise """
        return self._answer.lower() == attempt_str.lower()
    
    def __repr__(self):
        """ returns a representation of the current question instance """
        return "Q: {}".format(self._question) + " A: {}".format(self._answer)

    def __str__(self):
        """ returns a printable form of the question instance """
        return "{}".format(self._question)
