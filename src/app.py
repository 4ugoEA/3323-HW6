#author: Hugo E. Atayde
import re

#Student class to hold attributes for each student, such as id, first and last name, 
#eager or lazy, number grade and final grade
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

#The following line parses the text file as a string 
# and stores it in contents
with open("../input.txt") as f:
    contents = f.read();

#These lines separate each students record using the first 2 digits
#of their id, "11", then joins them in the list "s"
d = "11"
for line in contents:
    s =  [d+e for e in contents.split(d) if e]

#Alternate method to find matching records using regular expressions
#r"\b(\d{9})\b\s(.*?)(?=\b\d{9}\b|$)"

#r"[0-9]+\s[A-Za-z0-9]+\s[A-Za-z0-9]+\s[0-9]+ [A-Za-z]\s"

#pattern = re.compile(r"[0-9]+\s+[A-Za-z]+\s+[A-Za-z]+\s+\d\d\s+[A-Za-z]", re.IGNORECASE)
#pattern = re.compile(r"[0-9]+\s[A-Za-z0-9]+\s[A-Za-z0-9]+\s[0-9]+ [A-Za-z]\s", re.IGNORECASE)
pattern = r"\b(\d{9})\b\s(.*?)(?=\b\d{9}\b|$)"
#results = re.findall(pattern, contents)
results = re.findall(pattern, contents, flags=re.DOTALL)

id = []
stud = []

for tup in results:
    id.append(tup[0])

for tup in results:
    stud.append(tup[1])

#print(id)
#print(stud)


#These lines handle any new lines that might be scattered
#in our data and replaces them with temp character
rest = []

for x in stud:
    string = " ".join(x.split())
    rest.append(string)

#print(rest)

# for sub in stud:
#     rest.append(sub.replace("\n", "|"))

# #These lines find any of the temp characters and then replace 
# #them with spaces
# rest2 = []
# for sub in rest:
#     rest2.append(sub.replace("||", " "))

# #Additional string cleanup to make sure there are no 
# #temp characters left
# Rec = []
# for sub in rest2:
#     Rec.append(sub.replace("|", " "))



#n is the number of record entries, which is also the number of students
n = len(id)

#The following lines create specific ranges of indexes, in order to separate 
#students by their potential grades

#The top n/3 students are A's
#The following n/3 + 1 to 2n/3 are B's
#Anything between B's and F's are either C's or D's, that is determined later
#F's set as the bottom n/10 students
astart = 0
acut = (n // 3) - 1
bstart = acut + 1
bcut = (2 * (n // 3)) - 1
cdstart = bcut + 1
fcut = n - 1

#In the case that there are less than 10 students, the last student will be assigned F
#but the start of the F cutoff is altered slightly
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

#For each record stored in Rec, we create a new student using the first 5 values in 
#each record, which will be ID, First Name, Last Name, Number Grade, and Eager/Lazy
#We then add each student to the list "Students"
count = 0
for x in rest:
    s = x.split(" ")
    temp = student(int(id[count]), s[0], s[1], int(s[2]), s[3], 'f')
    Students.append(temp)
    count += 1

# print((Students[2]).get_id())
# print((Students[2].get_first_name()))
# print((Students[2].get_last_name()))
# print((Students[2].get_grade()))
# print((Students[2].get_letter()))

#This is probably the most important part:
#We take our list of Student objects and sort them by their grade, in descending order, then 
#by their Eager/Lazy value. This is done by having our key be a tuple, created
#by two functions, get_grade() and get_letter(). The grade comparison will be a 
#integer and the letter is a character. 
gradeSort = sorted(Students, key=lambda x: (-x.get_grade(), x.get_letter()))

# for x in gradeSort:
#     print(x.get_first_name())
#     print(x.get_grade())
#     print(x.get_letter())

#We create five lists, one for each letter grade, just for easier looping
#and for assigning final grades
alist = list()
blist = list()
clist = list()
dlist = list()
flist = list()

#These four variables are counters to keep track of each grade cutoff,
#while we are adding each student to their respective list
a = astart
b = bstart
c = cdstart
f = fstart

#These while loops are used to interate over specific indexes in our sorted list
#that correlate to our calculated cutoffs that were declared earlier
while(a <= (acut)):
    alist.append(gradeSort[a])
    a += 1

while(b <= (bcut)):
    blist.append(gradeSort[b])
    b += 1

#Since the C's and D's are any indexes not covered by the A's, B's or F's, we add
#an extra if else, that assigns the student to the C's or D's, based on their 
#Eager/Lazy value
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

#This for loops simply go through each letter grade list and sets each student's
#final grade to their respective list grade
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

#Creating a temp list to append all the students with their final grades
final0 = list()

for x in alist:
    final0.append(x)

for x in blist:
    final0.append(x)

for x in clist:
    final0.append(x)

for x in dlist:
    final0.append(x)

for x in flist:
    final0.append(x)

#Creating a new sorted list with all the students sorted according to Last Name, then First
#Name and finally ID
final = sorted(final0, key=lambda x: (x.get_last_name(),x.get_first_name(), x.get_id()), reverse=False)

# Create the HTML code for the table
#Basic HTML string for a HTML file that inclues a title and header, as well
#as a header for the table
table_html = """<html>
<head>
<title>Grades</title>
<style>
         table, th, td {
            border: 1px solid black;
            padding: 0; 
            border-spacing: none; 
         }
         table th, table td {
        padding: 5px;
      }
      th, td {
        text-align: center;
      }
      </style>
</head>
<body>
<h2>PPL 3323 Homework 6</h2><table>\n

<tr><th>ID</th><th>First</th><th>Last</th><th>Final</th></tr>\n"""
# Data rows
#Here we are iterating over each student and creating 
#a row, filled with that students information, ID, First Name, Last Name and Final Grade
#Every row is added on to our original HTML string
for student in final:
    table_html += f"<tr><td>{student.get_id()}</td><td>{student.get_first_name()}</td><td>{student.get_last_name()}</td><td>{student.get_final()}</td></tr>\n"

#This is the final bit of HTML code to make sure our HTML file is complete
table_html += """</table> </body>\n
    </html>"""


# Print the HTML code to the console
#Not that necessary, but its good to check that the string is formatted correctly
print(table_html)

#We create and open a new file called "output.html" and begin writing into it
f = open('output.html', 'w')
   
# Writing the code from the string we created above into the file
f.write(table_html)
  
#Close the file
f.close()

