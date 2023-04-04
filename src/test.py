# parse the input file and create a list of student records
students = []
with open('src\input.txt', 'r') as f:
    lines = f.readlines()
    i = 0
    while i < len(lines):
        record = []
        while i < len(lines) and not lines[i].startswith('ID'):
            i += 1
        if i >= len(lines):
            break
        fields = lines[i].split()
        record.append(fields[1])  # first name
        record.append(fields[2])  # last name
        record.append(int(fields[0]))  # ID
        record.append(int(fields[3]))  # score
        record.append(fields[4])  # eagerness
        i += 1
        while i < len(lines) and not lines[i].startswith('ID'):
            fields = lines[i].split()
            if len(fields) == 2:  # city and state
                record.append(fields[0])  # city
                record.append(fields[1])  # state
            else:
                record.append(None)  # no city and state
            i += 1
        students.append(record)

# sort the list of students according to the rules
students.sort(key=lambda x: (-x[3], x[4]))
n = len(students)
a_cutoff = n / 3
b_cutoff = 2 * a_cutoff
f_cutoff = -(-n / 10)  # ceil(n/10)
for i in range(n):
    if i < a_cutoff:
        students[i].append('A')
    elif i < b_cutoff:
        students[i].append('B')
    elif i >= n - f_cutoff:
        students[i].append('F')
    else:
        students[i].append('C' if students[i][4] == 'E' else 'D')

# generate the HTML table in the output file
with open('output.html', 'w') as f:
    f.write('<table>\n')
    f.write('<tr><th>Last name</th><th>First name</th><th>ID</th><th>Grade</th></tr>\n')
    for s in sorted(students, key=lambda x: (x[1], x[0], x[2])):
        f.write('<tr><td>{}</td><td>{}</td><td>{:09d}</td><td>{}</td></tr>\n'.format(
            s[1], s[0], s[2], s[5]))
    f.write('</table>\n')
