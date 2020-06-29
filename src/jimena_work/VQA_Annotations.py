import operator
import json
import re

with open('/export/a14/jgualla1/v2_mscoco_train2014_annotations.json') as f:
    total_dict = json.load(f)

limit = 10
limit_counter = 0

for key in total_dict:
    dict = total_dict[key]
    print(key)
    annotations_dict = total_dict["annotations"] 
    for annotation in annotations_dict:
        print(annotation["question_id"])
        print(annotation["image_id"])
        print(annotation["multiple_choice_answer"])
        limit_counter = limit_counter + 1 
        if limit_counter == limit:
            break
    if limit_counter == limit:
        break

#print(limit_counter)
