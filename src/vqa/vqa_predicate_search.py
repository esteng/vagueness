import operator
import json
import re
from collections import defaultdict
import random

# Training questions
with open('/export/b14/jgualla1/v2_OpenEnded_mscoco_train2014_questions.json') as f:
    total_dict = json.load(f)
# Validation questions
#with open('/export/b14/jgualla1/v2_OpenEnded_mscoco_val2014_questions.json') as f:
    #total_dict = json.load(f)

# Training annotations
with open('/export/b14/jgualla1/v2_mscoco_train2014_annotations.json') as h:
    total_annotation_dict = json.load(h)
# Validation annotations
#with open('/export/b14/jgualla1/v2_mscoco_val2014_annotations.json') as h:
    #total_annotation_dict = json.load(h)

#ith open('/home/jgualla1/vagueness/src/jimena_work/bad_preds.json',"w") as g:
    #son.dumps("data", g)
with open('/home/jgualla1/vagueness/data/vqa/json/bad_preds.json') as g:
    bad_preds_list = json.load(g)

with open('/home/jgualla1/vagueness/src/regex_dict.json') as k:
    regex_dict = json.load(k)

with open('/home/jgualla1/vagueness/src/non_regex_dict.json') as l:
    non_regex_dict = json.load(l)

# Dictionary of all annotations (answers)
ANNOTATIONS_DICT = defaultdict(list)
yn_annotation_counter = 0
annotation_counter = 0

# Getting all annotations
for key in total_annotation_dict:
    dict = total_annotation_dict[key]
    annotation_dict = total_annotation_dict["annotations"]
    for annotation in annotation_dict:
        annotation_counter = annotation_counter + 1
        q_id = annotation["question_id"]
        ANNOTATIONS_DICT[q_id] = []
        ANNOTATIONS_DICT[q_id].append(annotation["answer_type"])
        ANNOTATIONS_DICT[q_id].append(annotation["question_type"])
        #ANNOTATIONS_DICT[q_id].append(annotation["multiple_choice_answer"])
        #print(annotation["multiple_choice_answer"])
        answer_list = annotation["answers"]
        #print(answer_list)
        for answer in answer_list:
            ANNOTATIONS_DICT[q_id].append(answer["answer"])
            #print(answer["answer"])
            #annotation_counter = annotation_counter + 1 
        if annotation["answer_type"] == "yes/no":
            yn_annotation_counter = yn_annotation_counter + 1
        answer_list = None
        #print (ANNOTATIONS_DICT[q_id])
        #if annotation_counter == 10:
            #break
    #if annotation_counter == 10:
        #break

limit_counter = 0

QUESTION_DICTIONARY = {}
#bad_preds_list = bad_preds_dict["questionId"]
question_counter = 0
predicate_counter = 0 
yn_predicate_counter = 0
count = 0
limit = 5000

for key in total_dict:
    dict = total_dict[key]
    #print(key)
    question_dict = total_dict["questions"]
    #question_counter = question_counter + 1
    for question in question_dict:
        question_counter = question_counter + 1
        q = question["question"]
        #print (q)
        i_id = question["image_id"]
        q_id = question["question_id"]
        a_type = ANNOTATIONS_DICT[q_id][0]
        q_answers_list = ANNOTATIONS_DICT[q_id][2:]
        q_type = ANNOTATIONS_DICT[q_id][1]
        #f q_type == "yes/no":
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

        for bad_preds in bad_preds_list:
            if bad_preds == q_id:
                x = None
                break
        
        for item in QUESTION_DICTIONARY:
            dict = QUESTION_DICTIONARY[item]
            if q_id == dict["question_id"]:
                x = None

        if a_type != "yes/no":
            x = None

        if x:
            QUESTION_DICTIONARY[limit_counter] = {'question': q, 'question_id':q_id, 'question_type': q_type, 'answer_type': a_type, 'question_answers': q_answers_list, 'imageId': i_id}
            #print(limit_counter)
            #print(q)
            #print(q_id)
            #print("       ")
            x = None
            print(QUESTION_DICTIONARY[limit_counter])
            limit_counter = limit_counter + 1

        #print(QUESTION_DICTIONARY[limit_counter])
        #if limit_counter == limit:
            #break
    #if limit_counter == limit: 
       #break

#print(count)
#for question in QUESTION_DICTIONARY:
    #dict = QUESTION_DICTIONARY[question]
    #if dict["question_type"] == "yes/no":
        #yn_predicate_counter = yn_predicate_counter + 1 

#print(ANNOTATIONS_DICT)
#print(QUESTION_DICTIONARY)
#print("Total number of answer groups (for each answer) for entire dataset: " + str(annotation_counter))
#print("Total number of yes/no answer groups: " + str(yn_annotation_counter))
#print("Total number of questions: " + str(question_counter/6))
#print("Total number of predicate questions: " + str(len(QUESTION_DICTIONARY)))
#print("Total number of yes/no answers for predicate set: " + str(yn_predicate_counter))


#c = 0
#for question in QUESTION_DICTIONARY:
    #dict = QUESTION_DICTIONARY[question]
    #c = c + 1
    #print(str(c) + ": " + str(dict))


#res = random.sample(range(1,7907), 100)

#for num in res:
    #current_id = list(QUESTION_DICTIONARY)[num]
    #print(QUESTION_DICTIONARY[current_id])
    #current_id = None

with open("vague_questions.json","w") as f1:
    json.dump(QUESTION_DICTIONARY, f1)


