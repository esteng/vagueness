import operator
import json
import re
from collections import defaultdict

with open('/export/a14/jgualla1/v2_OpenEnded_mscoco_train2014_questions.json') as f:
    total_dict = json.load(f)
    
with open('/export/a14/jgualla1/v2_mscoco_train2014_annotations.json') as h:
    total_annotation_dict = json.load(h)

with open('/export/a14/jgualla1/v2_mscoco_train2014_annotations.json') as h:
    total_annotation_dict = json.load(h)

ANNOTATIONS_DICT = {}

for key in total_annotation_dict:
    dict = total_annotation_dict[key]
    annotation_dict = total_annotation_dict["annotations"]
    for annotation in annotation_dict:
        q_id = annotation["question_id"]
        ANNOTATIONS_DICT[q_id] = annotation["multiple_choice_answer"]

limit = 100
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
        #"child":"([iI]s)?([aA]n|[aA])?(([^\w])+([cC]hild)[^\w])",
        "adult":"([iI]s)?([aA]n|[aA])?(([^\w])+([aA]dult)[^\w])",
        "age":"(([^\w])+([aA]age)[^\w])",
        "enough":"(([^\w])+([eE]nough)[^\w])",
        "nearly":"(([^\w])+([nN]early)[^\w])",
        "new":"(([^\w])+([nN]ew)[^\w])",
        "overcast":"(([^\w])+([oO]overcast)[^\w])"
        #"blue":"([iI]s)?([aA]n|[aA])?(([^\w])+([bB]lue)[^\w])",
        #"brown":"([iI]s)?([aA]n|[aA])?(([^\w])+([bB]lue)[^\w])",
        #"green":"([iI]s)?([aA]n|[aA])?(([^\w])+([gG]reen)[^\w])",
        #"orange":"([iI]s)?([aA]n|[aA])?(([^\w])+([oO]range)[^\w])",
        #"pink":"([iI]s)?([aA]n|[aA])?(([^\w])+([pP]ink)[^\w])",
        #"purple":"([iI]s)?([aA]n|[aA])?(([^\w])+([pP]urple)[^\w])",
        #"red":"([iI]s)?([aA]n|[aA])?(([^\w])+([rR]ed)[^\w])",
        #"white":"([iI]s)?([aA]n|[aA])?(([^\w])+([wW]hite)[^\w])",
        #"yellow":"([iI]s)?([aA]n|[aA])?(([^\w])+([yY]ellow)[^\w])"
        }

QUESTION_DICT = defaultdict(list)
there = False

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
            x = re.search(current_regex, q)
            if x:
                if i_id in QUESTION_DICT:
                    for value in QUESTION_DICT[i_id]:
                        if value == {"question_id":q_id, "question":q, "answer":q_answer}:
                            there = True
                    if there == True:
                        pass
                    else:
                        QUESTION_DICT[i_id].append({"question_id":q_id, "question":q, "answer":q_answer})
                else:
                    QUESTION_DICT[i_id] = []
                    QUESTION_DICT[i_id].append({"question_id":q_id, "question":q, "answer":q_answer})
                limit_counter = limit_counter + 1
            there = False
        x = None
        #if limit_counter == limit: 
            #break
    #if limit_counter == limit:
        #break

with open("output.json","w" as f1:
        json.dump(QUESTION_DICT, f1)

#print(len(QUESTION_DICT))
#print(QUESTION_DICT)
