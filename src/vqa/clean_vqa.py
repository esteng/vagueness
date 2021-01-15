import csv
import pathlib
import json
cwd = pathlib.Path.cwd()


results_path = cwd.joinpath("results")
lxmert_path = results_path.joinpath("lxmert", "vqa")

for filename in lxmert_path.glob("*.json"):
    with open(filename) as f1:
        data =json.load(f1)
    print(type(data)) 
    bad = []
    good = []
    for element in data:
        answer = element["answer"]
        if answer['yes'] + answer['no'] < 0.98:
            bad.append(element)
        else:
            good.append(element)
    print(f"filename {filename} has {len(bad)}") 
    new_file = lxmert_path.joinpath(f"{filename.stem}_clean.json")
    with open(new_file, "w") as f1:
        json.dump(good, f1) 
