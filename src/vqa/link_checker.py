import json
import numpy as np
#import cv2
import requests
from urllib.request import urlopen

predicate = "sunny"

with open ('/home/jgualla1/vagueness/data/vqa/json/outputs_json_yesno/output_' + predicate + '_wurl_yesno.json') as f:
    total_question_dict = json.load(f)

dictionary_list = []
removed_count = 0 
count = 0 

for key in total_question_dict:
    
    question_dict = key
    answer_type = question_dict["answer_type"]
    image_id = question_dict["img_id"]
    image_url = question_dict["image_url"]
    label = question_dict["label"]
    question_id = question_dict["question_id"]
    question_type = question_dict["question_type"]
    sent = question_dict["sent"]
    answer = question_dict["answers"]
    score = question_dict["score"]
    score_answers = question_dict["score_answers"]

    count = count + 1 
    
    #img = cv2.imread('/export/a14/jgualla1/val2014/' + str(image_id) + '.jpg')

    #if img is None:
    #def exists(path):
        
        #r = requests.head(path)
        #return r.status_code == requests.codes.ok

    #try:
        #f = urllib2.urlopen(urllib2.Request(image_url))
        #deadLinkFound = False
    #except:
        #deadLinkFound = True

    #if deadLinkFound == False:       d
        #removed_count = removed_count + 1 

    try:
        image_formats = ('image/png', 'image/jpeg', 'image/jpg')
        site = urlopen(image_url)
    #r = requests.head(image_url)
        meta = site.info()
        if meta["content-type"] in image_formats:
            dictionary_list.append({'answer_type': answer_type, 'image_id': image_id, 'image_url': image_url,'label': label, 'question_id': question_id, 'question_type': question_type, 'question': sent, 'answer': answer, 'score': score, 'score_answers': score_answers})
        else:
            removed_count = removed_count + 1 
    except:
        removed_count = removed_count + 1

#print(removed_count)
#print(count - removed_count)

with open('/home/jgualla1/vagueness/src/vqa/output_' + predicate + '_wurl_yesno_checked.json', 'w') as f1:
    json.dump(dictionary_list, f1)



