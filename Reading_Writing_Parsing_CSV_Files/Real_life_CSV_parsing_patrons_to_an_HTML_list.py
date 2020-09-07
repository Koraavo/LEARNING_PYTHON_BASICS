import csv

html_output = ''
names = []

print("Method1")
with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    # we do not want headers or first line of data
    next(csv_data)
    next(csv_data)


    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f'{line[0]} {line[1]}')
    #print(names)

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!<p>'

html_output += '\n<ul>'
for name in names:
    html_output += f'\n\t<li>{name}<li>'

html_output += '\n</ul>'

print(html_output)

html_output1 = ''
names1 = []

print("Method 2 with dictionary")
with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    # first line of data
    next(csv_data)


    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names1.append(f'{line["FirstName"]} {line["LastName"]}')
    #print(names)

html_output1 += f'<p>There are currently {len(names1)} public contributors. Thank You!<p>'

html_output1 += '\n<ul>'
for name in names1:
    html_output1 += f'\n\t<li>{name}</li>'

html_output1 += '\n</ul>'

print(html_output1)
