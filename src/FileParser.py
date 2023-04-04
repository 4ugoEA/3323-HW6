with open("src\input.txt") as f:
    contents = f.read();

d = "11"
for line in contents:
    s =  [d+e for e in contents.split(d) if e]

res = []
for sub in s:
    res.append(sub.replace("\n", " "))

#print(contents.split("11"))

print(res)
print(len(res))