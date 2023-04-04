class student:
   
    def __init__(self, id, first_name, last_name, grade, l, f):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._grade = grade
        self._letter = l
        self.final = f

    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id
    
    def get_first_name(self):
        return self._first_name
    
    def set_first_name(self, first_name):
        self._first_name = first_name
    
    def get_last_name(self):
        return self._last_name
    
    def set_last_name(self, last_name):
        self._last_name = last_name
    
    def get_grade(self):
        return self._grade
    
    def set_grade(self, grade):
        self._grade = grade
    
    def get_letter(self):
        return self._letter

    def set_final(self, final):
        self.final = final

    def get_final(self):
        return self.final


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

Rec = res
n = len(Rec)

astart = 0
acut = (n // 3) - 1
bstart = acut + 1
bcut = (2 * (n // 3)) - 1
cdstart = bcut + 1
fcut = n - 1
if(n < 10):
    fstart = (n -1) - (n // 10)
else:
    fstart = (n) - (n // 10)

cdcut = fstart - 1

# print(astart)
# print(acut)
# print(bstart)
# print(bcut)
# print(cdstart)
# print(cdcut)
# print(fstart)
# print(fcut)

Students = list()

for x in Rec:
    s = x.split(" ")
    temp = student(int(s[0]), s[1], s[2], int(s[3]), s[4], 'f')
    Students.append(temp)

# print((Students[2]).get_id())
# print((Students[2].get_first_name()))
# print((Students[2].get_last_name()))
# print((Students[2].get_grade()))
# print((Students[2].get_letter()))

gradeSort = sorted(Students, key=lambda x: (-x.get_grade(), x.get_letter()))

# for x in gradeSort:
#     print(x.get_first_name())
#     print(x.get_grade())
#     print(x.get_letter())
    
alist = list()
blist = list()
clist = list()
dlist = list()
flist = list()

a = astart
b = bstart
c = cdstart
f = fstart

while(a <= (acut)):
    alist.append(gradeSort[a])
    a += 1

while(b <= (bcut)):
    blist.append(gradeSort[b])
    b += 1

while(c <= (cdcut)):
    if(gradeSort[c].get_letter() == 'E'):
        clist.append(gradeSort[c])
        c += 1
    else:
        dlist.append(gradeSort[c])
        c += 1

while(f <= (fcut)):
    flist.append(gradeSort[f])
    f += 1


for x in alist:
    x.set_final('A')
    # print(x.get_first_name())
    # print(x.get_grade())
    # print(x.get_final())

for x in blist:
    x.set_final('B')
    # print(x.get_first_name())
    # print(x.get_grade())
    # print(x.get_final())

for x in clist:
    x.set_final('C')
    # print(x.get_first_name())
    # print(x.get_grade())
    # print(x.get_final())

for x in dlist:
    x.set_final('D')
    # print(x.get_first_name())
    # print(x.get_grade())
    # print(x.get_final())

for x in flist:
    x.set_final('F')
    # print(x.get_first_name())
    # print(x.get_grade())
    # print(x.get_final())


# temp3 = temp1.extend(temp2)
# final = temp3.extend(flist)

# Create the HTML code for the table
table_html = """<html>
<head>
<title>Grades</title>
</head>
<body>
<h2>PPL 3323 Homework 6</h2><table>\n

<tr><th>ID</th><th>First</th><th>Last</th><th>Final</th></tr>\n"""
# Data rows
for student in alist:
    table_html += f"<tr><td>{student.get_id()}</td><td>{student.get_first_name()}</td><td>{student.get_last_name()}</td><td>{student.get_final()}</td></tr>\n"
for student in blist:
    table_html += f"<tr><td>{student.get_id()}</td><td>{student.get_first_name()}</td><td>{student.get_last_name()}</td><td>{student.get_final()}</td></tr>\n"
for student in clist:
    table_html += f"<tr><td>{student.get_id()}</td><td>{student.get_first_name()}</td><td>{student.get_last_name()}</td><td>{student.get_final()}</td></tr>\n"
for student in dlist:
    table_html += f"<tr><td>{student.get_id()}</td><td>{student.get_first_name()}</td><td>{student.get_last_name()}</td><td>{student.get_final()}</td></tr>\n"
for student in flist:
    table_html += f"<tr><td>{student.get_id()}</td><td>{student.get_first_name()}</td><td>{student.get_last_name()}</td><td>{student.get_final()}</td></tr>\n"

table_html += """</table> </body>\n
    </html>"""


# Print the HTML code to the console
print(table_html)

f = open('output.html', 'w')
  
# the html code which will go in the file GFG.html
html_template = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>Welcome To GFG</h2>

  
</body>
</html>
"""
  
# writing the code into the file
f.write(table_html)
  
# close the file
f.close()

