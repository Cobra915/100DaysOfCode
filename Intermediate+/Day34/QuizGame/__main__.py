from quiz_brain import QuizBrain
import time
import os
import urllib3
import json
import html
from ui import QuizInterface

# print(question_data)

class Question:
    def __init__(self, question, data):
        self.text = html.unescape(data['results'][question]['question'])
        self.answer = data['results'][question]['correct_answer']

def create_question_bank(data):
    question_bank = []
    for question in range(0,len(data['results'])):
        q = Question(question, data)
        question_bank.append(q)
    return question_bank

def get_request_2():
    http = urllib3.PoolManager()
    req = http.request('GET',"https://opentdb.com/api.php?amount=10&type=boolean")
    print(f'Open Trivia API request status: {req.status}')
    response = req.data
    string = response.decode('utf8')
    data = json.loads(string)
    return data

if __name__ == '__main__':

    data = get_request_2()

    question_bank = create_question_bank(data)

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)

    # while quiz.still_has_questions():
    #     quiz.next_question()
    #     time.sleep(2)
    #     os.system('cls')

    print('You\'ve completed the quiz!')
    print(f'Your final score was {quiz.score}/{quiz.question_number}')