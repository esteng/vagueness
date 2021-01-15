import json
import os 
import numpy as np
import requests
from urllib.request import urlopen
from glob import glob 

#predicate = "sunny"

#with open ("data/gqa/json/outputs_json_yesno/output_' + predicate + '_wurl_yesno.json') as f:

def clean_links(in_filepath, out_filepath): 
    with open(in_filepath) as f:
        total_question_dict = json.load(f)

    dictionary_list = []
    removed_count = 0 
    count = 0 

    for key in total_question_dict:
        
        question_dict = key
        #answer_type = question_dict["answer_type"]
        image_id = question_dict["image_id"]
        #image_url = question_dict["image_url"]
        image_url = f"https://ugrad.cs.jhu.edu/~jgualla1/images/{image_id}.jpg" 
        question_id = question_dict["question_id"]
        sent = question_dict["question"]

        count = count + 1 
        
        try:
            image_formats = ('image/png', 'image/jpeg', 'image/jpg')
            site = urlopen(image_url)
            meta = site.info()
            if meta["content-type"] in image_formats:
                dictionary_list.append({'image_id': image_id, 'image_url': image_url, 'question_id': question_id, 'question': sent})
            else:
                removed_count = removed_count + 1 
        except:
            removed_count = removed_count + 1

    print(f"{in_filepath}: removed {removed_count} of {count}")
    #print(count - removed_count)

    #with open('data/gqa/json/output_' + predicate + '_wurl_yesno_checked.json', 'w') as f1:
    with open(out_filepath, "w") as f1:
        json.dump(dictionary_list, f1)


if __name__ == "__main__":
    output_path = "data/gqa/json/outputs_json_wurl_small"
    for json_file in glob("data/gqa/json/outputs_json_small/*.json"):
        out_filepath = os.path.join(output_path, os.path.basename(json_file))
        clean_links(json_file, out_filepath) 



