from quiz_game_question_model import Question
from quiz_game_data import question_data 


question_bank = []

for items in question_data:
    question_bank.append(items)


question_obj = Question(items['text'], items['answer'])