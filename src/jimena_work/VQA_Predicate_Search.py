import operator
import json
import re
from collections import defaultdict
import random

with open('/export/a14/jgualla1/v2_OpenEnded_mscoco_train2014_questions.json') as f:
    total_dict = json.load(f)

#with open('/export/a14/jgualla1/v2_mscoco_train2014_annotations.json') as h:
#    total_annotation_dict = json.load(h)
with open('/export/a14/jgualla1/v2_mscoco_train2014_annotations.json') as h:
    total_annotation_dict = json.load(h)

ANNOTATIONS_DICT = defaultdict(list)
yn_annotation_counter = 0
annotation_counter = 0

for key in total_annotation_dict:
    dict = total_annotation_dict[key]
    annotation_dict = total_annotation_dict["annotations"]
    for annotation in annotation_dict:
        annotation_counter = annotation_counter + 1
        q_id = annotation["question_id"]
        ANNOTATIONS_DICT[q_id] = []
        ANNOTATIONS_DICT[q_id].append(annotation["answer_type"])
        #ANNOTATIONS_DICT[q_id].append(annotation["multiple_choice_answer"])
        #print(annotation["multiple_choice_answer"])
        answer_list = annotation["answers"]
        #print(answer_list)
        for answer in answer_list:
            ANNOTATIONS_DICT[q_id].append(answer["answer"])
            #print(answer["answer"])
            #annotation_counter = annotation_counter + 1 
        #y = re.search("(([^\w]|)+([yY]es)[^\w])|(([^\w]|)+([nN]o)[^\w])", annotation["multiple_choice_answer"])
        if annotation["answer_type"] == "yes/no":
            yn_annotation_counter = yn_annotation_counter + 1
        answer_list = None
        #if annotation_counter == 10:
            #break
    #if annotation_counter == 10:
        #break

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
        #"does":"(([^\w])+([dD]oes)[^\w])",
        "age":"(([^\w])+([aA]ge)[^\w])",
        "enough":"(([^\w])+([eE]nough)[^\w])",
        #"or":"(([^\w])+([oO]r)[^\w])",
        "nearly":"(([^\w])+([nN]early)[^\w])",
        "new":"(([^\w])+([nN]ew)[^\w])",
        "overcast":"(([^\w])+([oO]vercast)[^\w])"
        #"blue":"([iI]s)?([aA]n|[aA])?(([^\w])+([bB]lue)[^\w])",
        #"brown":"([iI]s)?([aA]n|[aA])?(([^\w])+([bB]rown)[^\w])", 
        #"green":"([iI]s)?([aA]n|[aA])?",
        #"orange":"([iI]s)?([aA]n|[aA])?(([^\w])+([oO]range)[^\w])",
        #"pink":"([iI]s)?([aA]n|[aA])?(([^\w])+([pP]ink)[^\w])",
        #"purple":"([iI]s)?([aA]n|[aA])?(([^\w])+([pP]urple)[^\w])",
        #"red":"([iI]s)?([aA]n|[aA])?(([^\w])+([rR]ed)[^\w])",
        #"white":"([iI]s)?([aA]n|[aA])?(([^\w])+([wW]hite)[^\w])",
        #"yellow":"([iI]s)?([aA]n|[aA])?(([^\w])+([yY]ellow)[^\w])"
        }

non_regex_dict = {
    "what sort of": "([Ww]hat sort of)",
    "what type of": "([Ww]hat type of)",
    "what color": "([wW]hat color)",
    "where is": "([wW]here is)",
    "why is": "([wW]hy is)",
    "what is": "([wW]hat is)"}

QUESTION_DICTIONARY = {}
question_counter = 0
predicate_counter = 0 
yn_predicate_counter = 0

for key in total_dict:
    dict = total_dict[key]
    #print(key)
    question_dict = total_dict["questions"]
    #question_counter = question_counter + 1
    for question in question_dict:
        question_counter = question_counter + 1
        q = question["question"]
        i_id = question["image_id"]
        q_id = question["question_id"]
        q_type = ANNOTATIONS_DICT[q_id][0]
        for regex in regex_dict:
            current_regex = regex_dict[regex]
            x = re.search(str(current_regex), q)
            #for non_regex in non_regex_dict:
    
            if x:
                break
                #print(q)
        for non_regex in non_regex_dict:
            current_non_regex = non_regex_dict[non_regex]
            y = re.search(str(current_non_regex), q)
            if y:
                x = None
                break
        if x:
            QUESTION_DICTIONARY[q_id] = {'question': q, 'question_id':q_id, 'question_type': q_type, 'imageId': i_id}
            #break
                #if q_type =="yes/no":
                    #yn_predicate_counter = yn_predicate_counter + 1 
                #predicate_counter = predicate_counter + 1
                #limit_counter = limit_counter + 1 
                #y = re.search("(([^\w]|)+([yY]es)[^\w])|(([^\w]|)+([nN]o)[^\w])", ANNOTATIONS_DICT[q_id])
            #if ANNOTATIONS_DICT[q_id][0] == "yes/no":
                #yn_predicate_counter = yn_predicate_counter + 1 
        x = None 
        #if limit_counter == limit:
            #break
    #if limit_counter == limit: 
       #break
for question in QUESTION_DICTIONARY:
    dict = QUESTION_DICTIONARY[question]
    if dict["question_type"] == "yes/no":
        yn_predicate_counter = yn_predicate_counter + 1 

#print(ANNOTATIONS_DICT)
#print(QUESTION_DICTIONARY)
print("Total number of answer groups (for each answer) for entire dataset: " + str(annotation_counter))
print("Total number of yes/no answer groups: " + str(yn_annotation_counter))
print("Total number of questions: " + str(question_counter/6))
#print(ANNOTATIONS_DICT)
print("Total number of predicate questions: " + str(len(QUESTION_DICTIONARY)))
print("Total number of yes/no answers for predicate set: " + str(yn_predicate_counter))

res = random.sample(range(1,8236), 100)

for num in res:
    current_id = list(QUESTION_DICTIONARY)[num]
    print(QUESTION_DICTIONARY[current_id])
    current_id = None 
