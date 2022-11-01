from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_Bank = []
for question in question_data:
    question_Bank.append(Question(question["text"], question["answer"]))
print(question_Bank[0].text)

quiz = QuizBrain(question_Bank)
while quiz.still_has_question():
    quiz.next_question()
print("you've completed the quiz")
print(f"your final score was {quiz.correct}/{quiz.question_number}")
