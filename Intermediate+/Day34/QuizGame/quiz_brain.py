
class QuizBrain:
    def __init__(self, question_bank : list):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0
        self.q_ans=''

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.q_ans = current_question.answer
        self.question_number += 1
        return f'Q.{self.question_number}: {current_question.text}'

    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def evaluate_answer(self, user_answer):
        if user_answer.lower() == self.q_ans.lower():
            self.score += 1
            return True
        else:
            return False


