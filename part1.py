import csv

ID_COUNT = 84
row_dict = {}

for i in range(1, ID_COUNT + 1):
    for j in range(i+1, ID_COUNT + 1):
        row_dict[str([i,j])] = [i,j]

with open('csv_data/RelationshipsFromSurveys.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            id_a = int(row[0])
        except:
            continue
        id_b = int(row[1])

        if id_a == id_b:
            continue
        elif id_a < id_b:
            key = str([id_a, id_b])
        else:
            key = str([id_b, id_a])

        if (row[2] == 'CloseFriend' or
            row[2] == 'SocializeTwicePerWeek'):
            if len(row_dict[key]) < 3:
                row_dict[key].append('friend')

    for k in row_dict.keys():
        if len(row_dict[k]) < 3:
            row_dict[k].append('not_friend')

with open('csv_data/Proximity.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            id_a = int(row[0])
        except:
            continue
        id_b = int(row[1])

        if id_a == id_b:
            continue
        elif id_a < id_b:
            key = str([id_a, id_b])
        else:
            key = str([id_b, id_a])
        
        if (row[3] != '' and float(row[3]) > 0):
            if len(row_dict[key]) < 4:
                row_dict[key].append('close')

    for k in row_dict.keys():
        if len(row_dict[k]) < 4:
            row_dict[k].append('not_close')

with open('csv_data/SMS.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            id_a = int(row[3])
        except:
            continue
        id_b = int(row[0])

        if id_a == id_b:
            continue
        elif id_a < id_b:
            key = str([id_a, id_b])
        else:
            key = str([id_b, id_a])

        if len(row_dict[key]) < 5:
            row_dict[key].append('texted')

    for k in row_dict.keys():
        if len(row_dict[k]) < 5:
            row_dict[k].append('not_texted')

with open('csv_data/Calls.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            id_a = int(row[3])
            id_b = int(row[0])
        except:
            continue        

        if id_a == id_b:
            continue
        elif id_a < id_b:
            key = str([id_a, id_b])
        else:
            key = str([id_b, id_a])
        
        if int(row[2]) > 0:
            if len(row_dict[key]) < 6:
                row_dict[key].append('called')

    for k in row_dict.keys():
        if len(row_dict[k]) < 6:
            row_dict[k].append('not_called')

csv_data = [['id_a','id_b','friendship','proximity','sms','calls']]
for k in row_dict.keys():
    csv_data.append(row_dict[k])

with open('part1.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)
