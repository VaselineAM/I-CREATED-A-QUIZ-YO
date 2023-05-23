class Brain:
    def __init__(self,question_list):
        self.questionlist = question_list #You are passing a list.
        self.score = 0
        self.question_number = 0

    def checkanswer(self, useranswer):
        correctanswer = self.questionlist[self.question_number]
        if useranswer.lower() == (correctanswer.answer).lower():
            print("You have answered correctly.")
            self.score = self.score + 1
        else:
            print("You have answered wrong.")
        self.question_number = self.question_number + 1

    def arequestionsleft(self):
        if self.question_number<len(self.questionlist):
            return True
        

    def displayquestion(self):
        current_question = self.questionlist[self.question_number] #Remember you are still passing a list to 'current_question' so you need to specify the index.
        useranswer = input(f"Q{self.question_number + 1}. {current_question.question} (True/False):  ").lower()
        self.checkanswer(useranswer)
        print(f"Your score is {self.score}/{self.question_number}")



