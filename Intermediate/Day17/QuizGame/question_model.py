from data import question_data

class Question:
    def __init__(self, question):
        self.text = question_data[question]['question']
        self.answer = question_data[question]['correct_answer']