import FileParser
from Student import student

Rec = FileParser.res
n = len(Rec)

Students = list()

for x in Rec:
    s = x.split(" ")
    temp = student(s[0], s[1], s[2], s[3], s[4], 'f')
    Students.append(temp)

# print((Students[2]).get_id())
# print((Students[2].get_first_name()))
# print((Students[2].get_last_name()))
# print((Students[2].get_grade()))
# print((Students[2].get_letter()))

gradeSort = sorted(Students, key=lambda x: x.get_grade(), reverse=False)

for x in gradeSort:
    print(x.get_first_name())
    print(x.get_grade())
    print(x.get_final())
    

#print(Rec[0])
#print(n)