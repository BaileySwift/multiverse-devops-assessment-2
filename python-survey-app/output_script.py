import csv

def print_csv():
    # open the csv file
    with open('clean_results.csv') as csvfile:
        # read the csv file
        reader = csv.reader(csvfile)
       
        # get the headers
        headers = next(reader)
       
        # get the maximum length of each column
        lengths = [len(header) for header in headers]
        for row in reader:
            for i in range(len(row)):
                lengths[i] = max(lengths[i], len(row[i]))
       
        # print the headers
        for i in range(len(headers)):
            print(f'{headers[i]:{lengths[i]}}', end=' ')
        print()
       
        # print the divider
        for i in range(sum(lengths) + len(lengths) - 1):
            print('-', end='')
        print()
       
        # print the data
        csvfile.seek(0)
        next(reader)
        for row in reader:
            for i in range(len(row)):
                print(f'{row[i]:{lengths[i]}}', end=' ')
            print()

if __name__ == '__main__':
    print_csv()