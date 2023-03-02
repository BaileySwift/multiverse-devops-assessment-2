import csv


def test_csv_reader():
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

    # check if the length of the data array is greater than 0
    assert len(data) > 0, "No data was read from the CSV file."

    # check if the first row of the CSV file is equal to ['column1', 'column2', 'column3']
    assert data[0] == ['column1', 'column2', 'column3'], "The first row of the CSV file does not match the expected value."

    # check if the second row of the CSV file is equal to ['value1', 'value2', 'value3']
    assert data[1] == ['value1', 'value2', 'value3'], "The second row of the CSV file does not match the expected value."