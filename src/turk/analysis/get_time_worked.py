import csv 
import sys 

with open(sys.argv[1]) as f1:
    reader = csv.DictReader(f1)


    times = []
    for line in reader:
        time_worked = int(line["WorkTimeInSeconds"])
        times.append(time_worked)

avg_secs = sum(times)/len(times)
avg_mins = avg_secs / 60
avg_hrs = avg_mins / 60
print(f"average time: seconds: {avg_secs} S = {avg_mins} M = {avg_hrs} H") 
max_time = max(times)
min_time = min(times) 

print(f"max time {max_time} min_time {min_time}") 
print(sorted(times))

times = sorted(times)
times = times[0:-10]
avg_secs = sum(times)/len(times)
avg_mins = avg_secs / 60
avg_hrs = avg_mins / 60
print(f"average time: seconds: {avg_secs} S = {avg_mins} M = {avg_hrs} H") 
