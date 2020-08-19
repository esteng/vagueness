import json
import re
import random

with open('/home/jgualla1/vagueness/src/GQA_Data/output_FINAL.json') as f:
    total_question_dict = json.load(f)

predicate = "young"
slim_to = 75

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

        dictionary_list.append(current_dict)

        count = count + 1 
    order_count = order_count + 1 

dictionary_list_len = len(dictionary_list)

random_num_list = random.sample(range(dictionary_list_len), slim_to)

#for i in range(slim_to):
    #random_num_list.append(randint(0, dictionary_list_len - 1)

slimmed_dictionary_list = []

for ran_num in random_num_list:
    slimmed_dictionary_list.append(dictionary_list[ran_num])

with open('output_' + predicate + '_yesno_small.json', 'w') as f1:
    json.dump(slimmed_dictionary_list, f1)

