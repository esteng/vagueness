import json

used_predicates_list = ["old", "young", "sunny", "cloudy", "high", "adult", "new"]
image_id_list = []

for predicate in used_predicates_list:
    with open('/home/jgualla1/vagueness/src/GQA_Data/output_' + predicate + '_yesno_small.json') as f:
        question_dict = json.load(f)
    
    for question in question_dict:
        #image_id_list.append('/export/a14/jgualla1/images/' + str(question['image_id']) + '.jpg')
        print('/export/a14/jgualla1/images/' + question['image_id'] + '.jpg')

#with open('output_neededimages.json', 'w') as f1:
    #json.dump(image_id_list, f1)
