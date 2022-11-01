class QuizBrain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.correct = 0

    def still_has_question(self):
        if self.question_number + 1 > len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        cur = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}: {cur.text} (True/False): ")
        self.question_number += 1
        self.check_answer(user_answer.lower(), cur.answer.lower())

    def check_answer(self, user_answer, answer):
        if user_answer == answer:
            print("you got it right.")
            self.correct += 1
        else:
            print("sorry, that's wrong")
        print(f"the correct answer was {answer}")
        print(f"your current score is : {self.correct}/{self.question_number}")
