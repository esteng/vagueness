import operator
import json
import re

with open('/export/a14/jgualla1/v2_OpenEnded_mscoco_train2014_questions.json') as f:
    total_dict = json.load(f)

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
        "child":"([iI]s)?([aA]n|[aA])?(([^\w])+([cC]hild)[^\w])",
        "adult":"([iI]s)?([aA]n|[aA])?(([^\w])+([aA]dult)[^\w])",
        "blue":"([iI]s)?([aA]n|[aA])?(([^\w])+([bB]lue)[^\w])",
        "brown":"([iI]s)?([aA]n|[aA])?(([^\w])+([bB]rown)[^\w])", 
        "green":"([iI]s)?([aA]n|[aA])?(([^\w])+([gG]reen)[^\w])",
        "orange":"([iI]s)?([aA]n|[aA])?(([^\w])+([oO]range)[^\w])",
        "pink":"([iI]s)?([aA]n|[aA])?(([^\w])+([pP]ink)[^\w])",
        "purple":"([iI]s)?([aA]n|[aA])?(([^\w])+([pP]urple)[^\w])",
        "red":"([iI]s)?([aA]n|[aA])?(([^\w])+([rR]ed)[^\w])",
        "white":"([iI]s)?([aA]n|[aA])?(([^\w])+([wW]hite)[^\w])",
        "yellow":"([iI]s)?([aA]n|[aA])?(([^\w])+([yY]ellow)[^\w])"
        }

QUESTIONS_DICT = {}

for key in total_dict:
    dict = total_dict[key]
    #print(key)
    question_dict = total_dict["questions"]
    for question in question_dict:
        q = question["question"]
        i_id = question["image_id"]
        q_id = question["question_id"] 
        #print(q)
        #Adjectives
        for regex in regex_dict:
            current_regex = regex_dict[regex]
            #print(current_regex)
            x = re.search(str(current_regex), q)
            if x: 
                #print(q)
                QUESTIONS_DICT[limit_counter] = {"image_id":i_id, "QApairs":{"question_id":q_id, "question": q}} 
                #print(current_regex)
        limit_counter = limit_counter + 1
        x = None
        #if limit_counter == limit:
            #break
    #if limit_counter == limit:
        #break

print(limit_counter)
print(QUESTIONS_DICT)
