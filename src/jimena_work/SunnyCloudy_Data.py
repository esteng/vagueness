import json 
import re

with open ('/home/jgualla1/vagueness/src/jimena_work/output_1000.json') as f:
    total_question_dict = json.load(f)

dictionary_list = []
count = 0
order_count = 0

for key in total_question_dict:
    question_dict = total_question_dict[str(order_count)]

    question = question_dict['question']
    x = re.search("([iI]s|[aA]n|[aA])?(([^\w])+([sS]unny)[^\w])", question)
    y = re.search("([iI]s|[aA]n|[aA])?(([^\w])+([cC]loudy)[^\w])", question)
    
    if x or y:

        answer_type = question_dict['answer_type']
        image_id = question_dict['imageId'] 
        image_length = len(str(image_id))
        needed_length = 12 - image_length
        needed_zeros = str(0)
        for w in range(0, needed_length - 1):
            needed_zeros = needed_zeros + str(0)
        image_file = ("COCO_val2014_" + str(needed_zeros) + str(image_id))
        label = question_dict["question_answers"][0]

        question_id = question_dict['question_id']
        question_type = question_dict['question_type']
        sent = question_dict['question']

        #print(sent)
        current_dict = {"answer_type": answer_type, "img_id": image_file, "label": {str(label): 1 }, "question_id": question_id, "question_type": question_type, "sent": sent}
        dictionary_list.append(current_dict)

        count = count + 1 
    
    #print(order_count)

    order_count = order_count + 1 
    
    if count == 2:
        break

with open("output_sunnycloudy.json","w") as f1:
        json.dump(dictionary_list, f1)
