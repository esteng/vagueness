import operator
import json

with open('/export/a14/jgualla1/v2_OpenEnded_mscoco_train2014_questions.json') as f:
    total_dict = json.load(f)

limit = 50
limit_counter = 0

for key in total_dict:
    dict = total_dict[key]
    #print(key)
    question_dict = total_dict["questions"]
    for question in question_dict:
        #print(question)
        print(question["question"])
        limit_counter = limit_counter + 1
        if limit_counter == limit:
            break
    if limit_counter == limit:
        break
