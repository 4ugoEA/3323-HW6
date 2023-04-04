with open("src\input.txt") as f:
    contents = f.read();

d = "11"
for line in contents:
    s =  [d+e for e in contents.split(d) if e]

rest = []
for sub in s:
    rest.append(sub.replace("\n", "|"))

rest2 = []
for sub in rest:
    rest2.append(sub.replace("||", " "))

res = []
for sub in rest2:
    res.append(sub.replace("|", " "))



#print(contents)
#print(res[1])
# print(len(res))