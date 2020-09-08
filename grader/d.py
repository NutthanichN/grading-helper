import csv

with open('comprog19-students.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    with open('eggs.csv', 'w', newline='', encoding='utf-8') as csvfile2:
        spamwriter = csv.writer(csvfile2)
        for row in spamreader:
            spamwriter.writerow(row)
