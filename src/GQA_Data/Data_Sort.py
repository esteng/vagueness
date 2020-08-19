import json
import re

with open('/home/jgualla1/vagueness/src/GQA_Data/output_FINAL_yesno.json') as f:
    total_question_dict = json.load(f)

prediate = "adult"

dictionary_list = []
count = 0
order_count = 0

for key in total_question_dict:
    question_dict = total_question_dict[str(order_count)]

    question = question_dict['question']

    x = re.search("([iI]s|[aA]n|[aA]])?(([^\w])+(" + predicate + ")[^\w])", question)

    if x:

        answer_type = question_dict['answer_type']
        image_id = question_dict['imageId']

