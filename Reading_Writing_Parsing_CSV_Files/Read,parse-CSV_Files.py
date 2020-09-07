import csv


def writing_csv():
    """
    General way of reading CSV Files:
    # if you wanna read with the new_files with the tab delimiter:
    with open('new_names.csv', 'r') as csv_file:
        csv_reader =csv.reader(csv_file, delimiter='\t')
        for line in csv_reader:
            print(line)

    Writing into CSV File, by creating a new file from the read-only file
        with open('names.csv', 'r') as csv_file: # read-only file
            csv_reader = csv.reader(csv_file) # reader module to read the csv_file

            with open('new_names_new.csv', 'w') as new_file: # write file, from the read-only file
                csv_writer = csv.writer(new_file, delimiter='*') # new file with '*' instead of ','

                for line in csv_reader:
                    csv_writer.writerow(line) # write each line using writerow

    Reading as dictionary:
    #Dictionary Reader:
    with open('names.csv', 'r') as csv_file:  # read-only file
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            print(line['email'])

    # Dict writer
    with open('names.csv', 'r') as csv_file:  # read-only file
        csv_reader = csv.DictReader(csv_file)

        with open('new_names.csv', 'w') as new_file:  # write file, from the read-only file
            field_names = ['first_name', 'last_name', 'email']

            csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter='\t')  # new file with '*' instead of ','

            csv_writer.writeheader()

            for line in csv_reader:
                csv_writer.writerow(line)  # write each line

    # If you want to remove something
    with open('names.csv', 'r') as csv_file:  # read-only file
    csv_reader = csv.DictReader(csv_file)

    with open('new_names1.csv', 'w') as new_file:  # write file, from the read-only file
        field_names = ['first_name', 'last_name', 'email'] # if you do not want the email

        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter='\t')  # new file with '*' instead of ','

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)  # write each line


    """
    pass


help(writing_csv)

# Dict writer
with open('names.csv', 'r') as csv_file:  # read-only file
    csv_reader = csv.DictReader(csv_file)  # when you would print it, field names become keys in the dictionary

    # you have to provide the fieldnames with the dictwriter
    with open('new_names1.csv', 'w') as new_file:  # write file, from the read-only file
        field_names = ['first_name', 'last_name']  # if you do not want the email

        csv_writer = csv.DictWriter(new_file, fieldnames=field_names,
                                    delimiter='\t')  # new file with 'tab' instead of ','

        csv_writer.writeheader()  # this will write out the fieldnames, which are the headers in the csv file

        for line in csv_reader:
            del line['email']  # asking to delete all the emails
            csv_writer.writerow(line)  # write each line
