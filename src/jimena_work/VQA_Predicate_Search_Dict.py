import operator
import json
import re

with open('/export/a14/jgualla1/v2_OpenEnded_mscoco_train2014_questions.json') as f:
    total_dict = json.load(f)

with open('/export/a14/jgualla1/v2_mscoco_train2014_annotations.json') as h:
    total_annotation_dict = json.load(h)

ANNOTATIONS_DICT = {}

for key in total_annotation_dict:
    dict = total_annotation_dict[key]
    annotation_dict = total_annotation_dict["annotations"]
    for annotation in annotation_dict:
        q_id = annotation["question_id"]
        ANNOTATIONS_DICT[q_id] = annotation["multiple_choice_answer"]

limit = 10
limit_counter = 0

regex_dict = {
        "old":"([iI]s|[aA]n|[aA])?(([^\w])+([oO]ld)[^\w])",
        "bald":"([iI]s|[aA]n|[aA])?(([^\w])+([bB]ald)[^\w])",    
        "tall":"([iI]s|[aA]n|[aA])?(([^\w])+([tT]all)[^\w])",
        "short":"([iI]s|[aA]n|[aA])?(([^\w])+([sS]ort)[^\w])",
        "young":"([iI]s|[aA]n|[aA])?(([^\w])+([yY]oung)[^\w])",
        "sunny":"([iI]s|[aA]n|[aA])?(([^\w])+([sS]unny)[^\w])",
        "cloudy":"([iI]s|[aA]n|[aA])?(([^\w])+([cC]loudy)[^\w])",
        "high":"([iI]s|[aA]n|[aA])?(([^\w])+([hH]igh)[^\w])",
        "low":"([iI]s|[aA]n|[aA])?(([^\w])+([lL]ow)[^\w])",
        "heap":"([iI]s)?([aA]n|[aA])?(([^\w])+([hH]eap)[^\w])",
        "child":"([iI]s)?([aA]n|[aA])?(([^\w])+([cC]hild)[^\w])",
        "adult":"([iI]s)?([aA]n|[aA])?(([^\w])+([aA]dult)[^\w])",
        "blue":"((iIs  
        }

QUESTION_DICT = {}

for key in total_dict:
    dict = total_dict[key]
    question_dict = total_dict["questions"]
    for question in question_dict:
        q = question["question"]
        i_id = question["image_id"]
        q_id = question["question_id"]
        q_answer = ANNOTATIONS_DICT[q_id]
        for regex in regex_dict:
            current_regex = regex_dict[regex]
            x = re.search(str(current_regex), q)
            if x:
                QUESTION_DICT[limit_counter] = {"image_id":i_id, "QApairs":{"question_id":q_id, "question":q, "answer":q_answer}}
                limit_counter = limit_counter + 1
        x = None
        #if limit_counter == limit: 
            #break
    #if limit_counter == limit:
        #break  

print(limit_counter)
print(QUESTION_DICT)
