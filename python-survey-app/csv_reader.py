import csv

# create an empty array to store the data
data = []

# open the csv file
with open('results.csv') as csvfile:
    # read the csv file
    reader = csv.reader(csvfile)
    # loop through each row of the csv file
    for row in reader:
        # add the row to the data array
        data.append(row)

# print the data
print(data)