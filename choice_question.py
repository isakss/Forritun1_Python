"""
This file contains a class that inherits the Question class and expands upon its usage by adding multiple choice questions
"""
from question import Question

class ChoiceQuestion(Question):
    """ Initialize an empty instance of ChoiceQuestion, uses the constructor from the Question class"""
    def __init__(self):
        super().__init__()
        self._choice_list = []
    
    def add_choice(self, answer_option, boolean_object):
        """ Populates a list of multiple choice questions, sets the correct answer within in the list """
        self._choice_list.append((answer_option,boolean_object))
        
        if boolean_object == True:
            index = self._choice_list.index((answer_option, boolean_object))
            self.set_answer(str(index + 1))
        
    def __str__(self):
        """ Prints the current list of multiple choice options in addition to the question being asked """
        option_num = 1
        option_str = ""
        for element in self._choice_list:
            option_str += str(option_num) + ". {}".format(element[0]) + "\n"
            option_num += 1
        return super().__str__() + "\n" + option_str.strip()
        


    
