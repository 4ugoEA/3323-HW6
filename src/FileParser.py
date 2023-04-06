import re


with open("src\input.txt") as f:
    contents = f.read();

pattern = re.compile(r"[0-9]+\s+[A-Za-z]+\s+[A-Za-z]+\s+\d\d\s+[A-Za-z]", re.IGNORECASE)
results = re.findall(pattern, contents)

#print(results)



d = "11"
for line in contents:
    s =  [d+e for e in contents.split(d) if e]

rest = []
for sub in results:
    rest.append(sub.replace("\n", "|"))

rest2 = []
for sub in rest:
    rest2.append(sub.replace("||", " "))

res = []
for sub in rest2:
    res.append(sub.replace("|", " "))

#print([(i % 2) and (i * i) and (i + 3) and i for i in range(100)])
print(res)

#print(contents)
#print(res[1])
# print(len(res))