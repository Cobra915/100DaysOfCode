if __name__ == '__main__':
    
    from data import question_data
    import question_model
    from pprint import pprint
    from quiz_brain import QuizBrain
    import time
    import os

    # print(question_data)
    question_bank = []
    def create_question_bank():
        for question in range(0,len(question_data)):
            q = question_model.Question(question)
            question_bank.append(q)
        return question_bank

    

    question_bank = create_question_bank()

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()
        time.sleep(2)
        os.system('cls')

    print('You\'ve completed the quiz!')
    print(f'Your final score was {quiz.score}/{quiz.question_number}')