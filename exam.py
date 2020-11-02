"""
This file contains the class Exam which encapsulates the functionality of the ChoiceQuestion and Question classes, creating a program capable of
creating exams.
"""
from choice_question import ChoiceQuestion
from question import Question

class Exam():
    def __init__(self):
        """ Initialize an empty instance of the Exam class, with lists to contain the instances of Question and ChoiceQuestion """
        self._question_list = []
        self._choice_question_list = []
        self.__point_count = 0
    
    def add_question(self, question_str, answer_str):
        """ Creates an instance of the Question class and appends it to a list of Question instances """
        q = Question()
        q.set_question(question_str)
        q.set_answer(answer_str) 
        self._question_list.append(q)

    def add_choice_question(self, question_str, answer_list):
        """ Creates an instance of the ChoiceQuestion class and appends it to a list of ChoiceQuestion instances """
        cq = ChoiceQuestion()
        cq.set_question(question_str)
        cq._choice_list = answer_list

        for element in answer_list:
            if element[1] == True:
                index = answer_list.index((element[0],element[1]))
                cq.set_answer(str(index + 1))

        self._choice_question_list.append(cq) 

    
    def get_num_questions(self):
        """ Returns the total number of questions within the Exam """
        return len(self._question_list) + len(self._choice_question_list)
    
    def get_points(self):
        """ Returns the total tally of points accumulated in the exam """
        return self.__point_count
    
    def present_exam(self):
        """ Prints a workable exam, first half devoted to singular questions and the second half devoted to multiple choice """
        for element in self._question_list:
            print(element)
            response = input("Your answer: ")
            print(element.check_answer(response))
            print()

            if element.check_answer(response):
                self.__point_count += 1
    

        for element in self._choice_question_list:
            print(element)
            response = input("Your answer: ") 
            print(element.check_answer(response))
            print()

            if element.check_answer(response) == True:
                self.__point_count += 1
