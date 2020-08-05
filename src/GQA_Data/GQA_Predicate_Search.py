import json

with open('/export/a14/jgualla1/val_all_questions.json') as f:
    total_question_dict = json.load(f)

with open('/home/a14/jgualla1/regex_dict.json') as h:
    regex_dict = json.load(h)

with open('/home/jgualla1/vagueness/src/non_regex_dict.json') as g:
    non_regex_dict = json.load(g)

limit_counter = 0

QUESTION_DICTIONARY = {}
    
for key in total_question_dict:
    question_dict = total_questions_dict[key]
    
    question_id = key
    question = question_dict["question"]
    answer = question_dict["answer"]
    full_answer = question_dict["fullAnswer"]
    image_id = question_dict["imageId"]
    
    
    for regex in regex_dict:
        current_regex = regex_dict[regex]
        x = re.search(str(current_regex), question)

        if x:
            break

    for non_regex in non_regex_dict:
        current_non_regex = non_regex_dict[non_regex]
        y = re.search(str(current_non_regex), question)
        
        if y:
            x = None
            break
    
    #for bad_pred in bad_preds_list: HAVE TO CREATE BAD PREDS LIST
        #if bad_pred == 

    if x:
        QUESTION_DICTIONARY[limit_counter] = {'question_id': question_id, 'question': question, 'answer': answer, 'full_answer': full_answer, 'image_id': image_id} 

    limit_counter = limit_counter + 1 
    if limit_counter == 10:
        break

with open('output_test.json','w') as f1:
    json.dump(QUESTION_DICTIONARY, f1)
