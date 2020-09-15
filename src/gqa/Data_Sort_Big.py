import json
import re

with open('/home/jgualla1/vagueness/src/GQA_Data/output_FINAL.json') as f:
    total_question_dict = json.load(f)

predicate = "overcast"

dictionary_list = []
count = 0
order_count = 0

for key in total_question_dict:
    question_dict = total_question_dict[str(order_count)]

    question = question_dict['question']

    x = re.search("([iI]s|[aA]n|[aA]])?(([^\w])+(" + predicate + ")[^\w])", question)

    if x:

        #answer_type = question_dict['answer_type']
        image_id = question_dict['image_id']
        question_id = question_dict['question_id']
        answer = question_dict['answer']
        full_answer = question_dict['full_answer']

        current_dict = {'image_id': image_id, "question": question, "question_id": question_id, "answer": answer, "full_answer": full_answer}
        dictionary_list.append(current_dict)

        count = count + 1 
    order_count = order_count + 1 

with open('output_' + predicate + '_yesno_big.json', 'w') as f1:
    json.dump(dictionary_list, f1)

