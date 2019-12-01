import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # next() function ommits first row(with keys) in csv file like ['first_name', 'last_name', 'email']
    # next(csv_reader)
    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
            # to print out only first_name values we can use indexing [0]
            # print(line[0])
