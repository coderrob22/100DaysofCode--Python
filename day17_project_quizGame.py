from quiz_game_question_model import Question
from quiz_game_data import question_data 
from quiz_game_quiz_brain import QuizBrain

question_bank = []

for items in question_data:
    
    question_obj = Question(items['text'], items['answer'])
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions:
    quiz.next_question()