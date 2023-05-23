from questiondata import question_data
from questionmodel import QuestionModel
from quizbrain import Brain

questionbank = []

for x in question_data:
    question = x["question"] 
    answer = x["correct_answer"]
    questionbank.append(QuestionModel(question,answer)) #Basically, question bank keeps all the objects with it. The objects have attributes of 'question' and 'answer'.

brain = Brain(questionbank)
while brain.arequestionsleft():
    brain.displayquestion()





