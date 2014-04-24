import csv

row_data = [['salads','veggies','aerobic','sports',
             'healthy_diet','smoking']]

with open('csv_data/Health.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        r = []
        try:
            salads_count = int(row[3])
            if salads_count >= 5:
                r.append('lots_of_salads')
            else:
                r.append('few_salads')
        except:
            continue    

        try:
            veggies_count = int(row[4])
            if veggies_count >= 4:
                r.append('lots_of_veggies')
            else:
                r.append('few_veggies')
        except:
            continue

        try:
            aerobic_count = int(row[6])
            if aerobic_count >= 4:
                r.append('lots_of_aerobic')
            else:
                r.append('few_aerobic')
        except:
            continue

        try:
            sports_count = int(row[7])
            if sports_count >= 4:
                r.append('lots_of_sports')
            else:
                r.append('few_sports')
        except:
            continue

        if (row[5] == 'Below average' or
            row[5] == 'Very unhealthy' or
            row[5] == 'Unhealthy'):
            r.append('unhealthy')
        else:
            r.append('healthy')
    
        r.append(row[8])

        if len(row[8]) > 3:
            row_data.append(r)

with open('part2.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(row_data)
