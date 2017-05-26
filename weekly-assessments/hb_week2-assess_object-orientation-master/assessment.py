"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Encapsulation:
    Hides the details that we don't necessarily need and keeps everything
    you should know about a class close to its declaration.

   Abstraction:
    Allows you to abstract the complexity of how something (a method) 
    works and use method without knowing what method specifically does.

   Polymorphism:
    Gives flexibility in inheritance and how attributes are assigned 
    to an object or class.


2. What is a class?
    A family of characteristics. These characteristics, or attributes, are passed
    onto objects when an object is created in that class. These are called class
    attributes.

3. What is an instance attribute?
    An instance attribute only applies attributes to that instance, or object,
    within a class that are not shared with all others in that class. A simple
    example is that we may have a class of Cats, where all cats are described as
    furry, but we know of cats who aren't. The class attribute of /hair/ can be 
    'furry', while we can define the instance attribute of /hair/ on a hairless cat 
    to be 'hairless'.

4. What is a method?
    A method is like a function that only applies to the class in which it's found.
    It also always takes the instance itself as the first parameter of the argument.

5. What is an instance in object orientation?
    A class instance, or object, is a single representation of a class. It inherits
    the attributes defined in that class (or found in superclasses) unless instance 
    attributes are found.

6. How is a class attribute different than an instance attribute?
    A class attribute is an attribute shared by most members of a class, but can
    be redefined upon instantiation.

    From #3:
    An instance attribute only applies attributes to that instance, or object,
    within a class that are not shared with all others in that class. A simple
    example is that we may have a class of Cats, where all cats are described as
    furry, but we know of cats who aren't. The class attribute of /hair/ can be 
    'furry', while we can define the instance attribute of /hair/ on a hairless cat 
    to be 'hairless'.

"""

class Students(object):
    def __init__(self, first_name, last_name, address):
        """What occurs when an object is initiated in this class."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init__(self, question, correct_answer, questions_list={}):
        """What occurs when an object is initiated in this class."""

        self.question = question
        self.correct_answer = correct_answer
        self.questions_list = questions_list
        questions_list[self.question] = [self.correct_answer]


    def ask_and_evaluate(self):
        """Prints question and allows user to input their answer.

        If the user's answer is correct, True is returned. Otherwise False is
        returned. """

        print self.question
        answer = raw_input("> ") #prompt for raw input

        if answer == self.correct_answer:
            return True
        else:
            return False


class Exam(Question):

    def __init__(self, name, questions_list={}):
        """What occurs when an object is initiated in this class."""

        self.name = name
        self.questions_list = questions_list
        
    def add_question(self, question, correct_answer):
        """Adds question to the list of exam questions.

        Also instantiates a question object when this method is called."""

        self.question = question
        self.correct_answer = correct_answer
        self.questions_list[self.question] = [self.correct_answer]
        return super(Exam, self).__init__(question, correct_answer) #instantiates a Question object

    def administer(self):
        """All exam questions are administered via ask_and_evaluate method.

        If the user's answers are correct, the score will incrementally increase by 1.
        The score prints at the end of the exam."""
        
        if self.questions_list:
            score = 0

            if super(Exam, self).ask_and_evaluate() == True:
                score += 1
            else:
                pass #i know this isn't working, but stuck at this point as i can't iterate through questions_list

        return score

##### PART 4 #####

def take_test(exam, student):
    """Function should take an exam and a student as params, administer exam,
    and give student a score, which will be stored as an instance attribute."""

    exam = Exam('Exam 1')
    student = Students('FN', 'LN', 'Address')
    student.score = exam.administer() #output of administered exam is score, that value is stored as attribute on student
    return student.score


def example():
    """Function should act as an example for how to administer an exam.

    Function should create an exam, add new questions to the questions_list,
    create a student, and administer the exam to that student."""

    exam_test = Exam('Example Exam', {'What is the color of the sky?': 'blue', 'What is the color of grass?': 'green',})
    new_student = Students('Jane', 'Donut', '123 Apple Road')
    return exam_test.administer()


##### PART 5 #####

# class Quiz(Exam):

#     def __init__(self, name)
#         return super(Exam, self).__init__()
        

