import csv

print("hi")

with open("git.csv","w") as file:
    obj = csv.writer(file)
    obj.writerows([["sl","name"],["01","hus"]])
