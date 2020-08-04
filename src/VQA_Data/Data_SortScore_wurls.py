import json 
import re

with open ('/home/jgualla1/vagueness/src/VQA_Data/output_FINAL.json') as f:
    total_question_dict = json.load(f)

with open ('/export/a14/jgualla1/annotations/captions_val2014.json') as g:
    total_annotations_dict = json.load(g)

dictionary_list = []
count = 0
order_count = 0

for key in total_question_dict:
    question_dict = total_question_dict[str(order_count)]

    question = question_dict['question']
    x = re.search("([iI]s|[aA]n|[aA])?(([^\w])+([oO]ld)[^\w])", question)
    
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
        answer_count = 0 

        image_url = "     "
        images_list = total_annotations_dict["images"]
        for image in images_list:
            if image["file_name"] == ( "COCO_val2014_" + str(needed_zeros) + str(image_id) + ".jpg" ):
                #print(str(needed_zeros) + str(image_id))
                image_url = image["flickr_url"]
                break
        
    
        for answer in answer_list:
            w = re.search("([oO]ld)", answer)

            v = re.search("([yY]es)", answer)
            if w or v:
                update_answer_list.append(1)
                answer_count = answer_count + 1 
            else:
                update_answer_list.append(0)

        w = None
        v = None

        current_dict = {"answer_type": answer_type, "img_id": image_file, "image_url": image_url, "label": {str(label): 1 }, "question_id": question_id, "question_type": question_type, "sent": sent, "answers":answer_list, "score": answer_count, "score_answers": update_answer_list}
        dictionary_list.append(current_dict)

        count = count + 1 

    order_count = order_count + 1 

with open("output_new_wurl.json","w") as f1:
    json.dump(dictionary_list, f1)
