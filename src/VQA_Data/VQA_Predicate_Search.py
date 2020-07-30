import operator
import json
import re
from collections import defaultdict
import random

# Training questions
#with open('/export/a14/jgualla1/v2_OpenEnded_mscoco_train2014_questions.json') as f:
    #total_dict = json.load(f)
# Validation questions
with open('/export/a14/jgualla1/v2_OpenEnded_mscoco_val2014_questions.json') as f:
    total_dict = json.load(f)

# Training annotations
#with open('/export/a14/jgualla1/v2_mscoco_train2014_annotations.json') as h:
    #total_annotation_dict = json.load(h)
# Validation annotations
with open('/export/a14/jgualla1/v2_mscoco_val2014_annotations.json') as h:
    total_annotation_dict = json.load(h)

#ith open('/home/jgualla1/vagueness/src/jimena_work/bad_preds.json',"w") as g:
    #son.dumps("data", g)
with open('/home/jgualla1/vagueness/src/jimena_work/bad_preds.json') as g:
    bad_preds_list = json.load(g)

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
    "what is": "([wW]hat is)",
    "how many": "([hH]ow many)",
    "some sort of": "([sS]ome sort of)",
    "a sort of": "([aA] sort of)",
    #"sort": "([sS]ort)",
    "according to": "([aA]ccording to)",
    "likely": "([lL]ikely)",
    "does this belong": "([dD]oes this belong to)",
    "does this item belong": "([dD]oes this item belong)",
    "do these belong to": "([dD]o these belong to)",
    "do these items belong to": "([dD]o these items belong to)",
    "doing": "([dD]oing)",
    "what number of": "([iI]s it for)",
    "the same age": "([tT]he same age)",
    "are they at": "([aA]re they at)",
    "a new form": "([aA] new for of)",
    "seem to have": "([sS]eem to have)",
    "would anyone think": "([wW]ould anyone think)",
    "by choice": "([bB]y choice)",
    "based on their age": "([bB]ased on their age)",
    "holding anything": "([hH]olding anything)",
    "the same": "([tT]he same)",
    "what age group": "([wW]hat age group)",
    "is it easy to tell": "([iI]s it easy to tell)",
    "relatively same age": "([rR]elatively same age)",
    "is this person wearing": "([tT]hat of a child or an adult's)",
    "what are the": "([wW]hat are the)",
    "how old": "([hH]ow old)",
    "how tall": "([hH]ow tall)",
    "how high": "([hH]ow high)",
    "over the age of": "([oO]ver the age of)",
    "what age": "([wW]hat age)",
    "high speed train": "([hH]igh speed train)",
    "new york": "([nN]ew [yY]ork)",
    "which age": "([wW]hich age)",
    "what shows": "([wW]hat shows)",
    "old-fashioned": "([oO]ld-fashioned)",
    "old fashioned": "([oO]ld fashioned)",
    "adult's": "([aA]dult's)",
    "child's": "([cC]hild's)",
    "years old": "([yY]ears old)",
    "high-noon": "([hH]igh-noon)",
    "high noon": "([hH]igh noon)",
    "was this taken": "([wW]as this taken)",
    "what brand": "([wW]hat brand)",
    "how do you know": "([hH]ow do you know)",
    "high-quality": "([hH]igh-quality)",
    "high quality": "([hH]igh quality)",
    "how young": "([hH]ow young)",
    "high definition": "([hH]igh definition)",
    "off the ground": "([oO]ff the ground)",
    "low calorie": "([lL]ow calorie)",
    "new model": "([nN]ew model)",
    "naturally bald": "([nN]aturally bald)",
    "less than":"([lL]ess than)",
    "of any sort": "([oO]f any sort)",
    "adult beverage": "([aA]dult beverage)",
    "any sort of": "([aA]ny sort of)",
    "high class": "([hH]igh class)",
    "look happy": "([lL]ook happy)",
    "high in calories": "([hH]igh in calories)",
    "high in fiber": "([hH]igh in fiber)",
    "high in cholesterol": "([hH]igh in cholesterol)",
    "adult paty": "([aA]dult party)",
    "adult ride": "([aA]dult ride)",
    "high rise": "([hH]igh rise)",
    "high tech": "([hH]igh tech)",
    "high end": "([hH]igh end)",
    "low-carb": "([lL]ow-carb)",
    "as high as": "([aA]s high as)",
    "a high degree": "([aA] high degree)",
    "are there many": "([aA]re there many)",
    "high heel": "([hH]igh heel)",
    "high chair": "([hH]igh chair)",
    "to be over age": "([tT]o be over age)",
    "are all": "([aA]re all)",
    "low fat": "([lL]ow fat)",
    "or what": "([oO]r what)",
    "high calories": "([hH]igh calories)",
    "is everyone": "([iI]s everyone)",
    "high pressure": "([hH]igh pressure)",
    "low tide": "([lL]ow tide)",
    "are these all": "([aA]re these all)",
    "need": "([nN]eed)",
    "more easily": "([mM]ore easily)",
    "standing tall": "([sS]tanding tall)",
    "high school": "([hH]igh school)",
    "adult sized": "([aA]dult sized)",
    "want": "([wW]ant)",
    "high calorie": "([hH]igh calories)",
    "air pollution": "([aA]ir pollution)",
    "an appropriate age": "([aA]n appropriate age)",
    "mostly young": "([mM]ostly young)",
    "low carb": "([lL]ow carb)",
    "beta carotene": "([bB]eta carotene)",
    "high calorie": "([hH]igh calorie)",
    "brave": "([bB]rave)",
    "high tide": "([hH]igh tide)",
    "be able to": "([bB]e able to)",
    "dressed for": "([dD]ressed for)",
    "worried": "([wW]orried)",
    "learning": "([lL]earning)",
    "reached the age of": "([rR]eached the age of)",
    "standing": "([sS]tanding)",
    "smiling": "([sS]miling)",
    "at home": "([aA]t home)",
    "walking": "([wW]alking])",
    "busy": "([bB]usy)",
    "holding": "([hH]olding)",
    "more than": "([mM]ore than)",
    "high fiber": "([hH]igh fiber)",
    "of some sort": "([oO]f some sort)",
    "is one of": "([iI]s one of)",
    "can you tell me": "([cC]an yout tell me)",
    "monitoring": "([mM]onitoring)",
    "partly cloudy": "([pP]artly cloudy)",
    "sewing": "([sS]ewing)",
    "touching": "([tT]ouching)",
    "playing": "([pP]laying)",
    "all adult": "([aA]ll adult)",
    "all young": "([aA]ll young)",
    "too young": "([tT]oo young)",
    "to young": "([tT]o young)",
    "too old": "([tT]oo old)",
    "to old": "([tT]o old)",
    "how": "([hH]ow)",
    "what kind of epxression": "([wW]hat kind of expression)",
    "male or female": "([mM]ale or female)",
    "why does": "([wW]hy does)"
    }

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

        if x:
            QUESTION_DICTIONARY[limit_counter] = {'question': q, 'question_id':q_id, 'question_type': q_type, 'answer_type': a_type, 'question_answers': q_answers_list, 'imageId': i_id}
            #print(limit_counter)
            #print(q)
            #print(q_id)
            #print("       ")
            x = None
            limit_counter = limit_counter + 1 
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

with open("output_FINAL.json","w") as f1:
    json.dump(QUESTION_DICTIONARY, f1)

