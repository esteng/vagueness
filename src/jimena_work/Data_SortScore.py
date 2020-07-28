import json 
import re

with open ('/home/jgualla1/vagueness/src/jimena_work/output_1000_yesno.json') as f:
    total_question_dict = json.load(f)

#print(total_question_dict)

dictionary_list = []
count = 0
order_count = 0

for key in total_question_dict:
    question_dict = total_question_dict[str(order_count)]

    question = question_dict['question']
    x = re.search("([iI]s|[aA]n|[aA])?(([^\w])+([sS]hort)[^\w])", question)







    #y = re.search("([iI]s|[aA]n|[aA])?(([^\w])+([cC]loudy)[^\w])", question)
    
    if x:

        answer_type = question_dict['answer_type']
        image_id = question_dict['imageId'] 
        image_length = len(str(image_id))
        needed_length = 12 - image_length
        needed_zeros = str(0)
        for t in range(0, needed_length - 1):
            needed_zeros = needed_zeros + str(0)
        image_file = ("COCO_val2014_" + str(needed_zeros) + str(image_id))
        label = question_dict["question_answers"][0]

        question_id = question_dict['question_id']
        question_type = question_dict['question_type']
        sent = question_dict['question']

        answer_list = question_dict['question_answers']
        update_answer_list = []
        #answer_list_count = 0
        answer_count = 0 
        
    
        for answer in answer_list:
            w = re.search("([sS]hort)", answer)

            v = re.search("([yY]es)", answer) 
            if w or v:
                update_answer_list.append(1)
                answer_count = answer_count + 1 
            else:
                update_answer_list.append(0)

                #y = None

        #if y:
            #for answer in answer_list:
                #w = re.search("((^\w)+([cC]loudy)[^\w])", answer)
                #v = re.search("([nN]o)", answer)
                #if v:
                    #update_answer_list.append(1)
                    #answer_count = answer_count + 1 
                #else:
                    #update_answer_list.append(0) 

        w = None
        v = None

        #print(sent)
        current_dict = {"answer_type": answer_type, "img_id": image_file, "label": {str(label): 1 }, "question_id": question_id, "question_type": question_type, "sent": sent, "answers":answer_list, "score": answer_count, "score_answers": update_answer_list}
        dictionary_list.append(current_dict)

        count = count + 1 
    
    #print(order_count)

    order_count = order_count + 1 
    
    #if count == 10:
        #break

#print(count
#print(dictionary_list)
with open("output_short_scored.json","w") as f1:

    json.dump(dictionary_list, f1)
