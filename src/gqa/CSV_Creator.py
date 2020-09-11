import csv
import json

predicate = 'young'

with open ('/home/jgualla1/vagueness/src/gqa/output_' + predicate + '_yesno_small.json') as f:
    predicate_dict = json.load(f)

row_size = 8
row_counter = 0
count = 1
question_count = 0
question_limit = 10000
csv_format_list = []

for question in predicate_dict:

    current_dict = {}
    csv_format_list.append(current_dict)
    csv_format_list[row_counter]['question_' + str(count)] = question['question']
    csv_format_list[row_counter]['imageurl_' + str(count)] = ('ugrad.cs.jhu.edu/~jgualla1/images/' + str(question['image_id']) + '.jpg')
    csv_format_list[row_counter]['question_id_' + str(count)] = question['question_id']

    question_count = question_count + 1

    count = count + 1

    if count == row_size:
        count = 0
        row_counter = row_counter + 1

    if question_count == question_limit:
        break

csv_format_list_filtered = filter(None, csv_format_list)

with open('output_' + predicate + '_yesno.csv','w',newline='') as csvfile:
    fieldnames = ['question_0', 'imageurl_0','question_id_0', 'question_1', 'imageurl_1','question_id_1', 'question_2', 'imageurl_2','question_id_2', 'question_3', 'imageurl_3','question_id_3', 'question_4', 'imageurl_4','question_id_4', 'question_5', 'imageurl_5','question_id_5', 'question_6', 'imageurl_6','question_id_6', 'question_7', 'imageurl_7','question_id_7']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for item in csv_format_list_filtered:
        if len(item) == row_size * 3:
            writer.writerow(item)
