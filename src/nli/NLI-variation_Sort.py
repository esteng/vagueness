import json
import statistics

with open("/export/a14/jgualla1/preprocessed-data.jsonl", 'r') as f1:
    lines = f1.readlines()
data = [json.loads(line) for line in lines]

count = 0
dict_unsorted = {}
list_sorted = []

for key in data:
    sd = statistics.pstdev(key["normed-labels"])
    id = key["id"]
    #print(sd)
    dict = {"standard-deviation": sd, "id": id}
    dict_unsorted[count] = dict
    count = count + 1

sort_order = sorted(dict_unsorted.items(), key=lambda x: x[1]["standard-deviation"], reverse=True)
#print(sort_order)

for item in sort_order:
    dict = item[1]
    id = dict["id"]
    sd = dict["standard-deviation"]
    for key in data:
        if id == key["id"]:
            premise = key["premise"]
            hypothesis = key["hypothesis"]
            task = key["task"]
            originaldatasetlabel = key["original-dataset-label"]
            labels = key["labels"]
            normedlabels = key["normed-labels"]
            break
    dict = {"premise": premise, "hypothesis": hypothesis, "task": task, "original-dataset-label": originaldatasetlabel, "labels": labels, "normed-lables": normedlabels, "standard-deviation": sd}
    list_sorted.append(dict)

with open("output_normed.json","w") as f2:
    json.dump(list_sorted, f2)

