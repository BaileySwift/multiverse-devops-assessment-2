import csv

def test_csv_reader():
    # create an empty array to store the data
    data = []

    try:
        # open the csv file
        with open('results.csv', newline='') as csvfile:
            # read the csv file
            reader = csv.reader(csvfile)
            # loop through each row of the csv file
            for row in reader:
                # skip empty rows
                if len(row) == 0:
                    continue
                # add the row to the data array
                data.append(row)
    except FileNotFoundError:
        raise AssertionError("The CSV file was not found.")
    except Exception as e:
        raise AssertionError(f"An error occurred while reading the CSV file: {e}")

    # check if the length of the data array is greater than 0
    assert len(data) > 0, "No data was read from the CSV file."

    # check if the first row of the CSV file is equal to ['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3']
    assert data[0] == ['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'], "The first row of the CSV file does not match the expected value."

    # check if the second row of the CSV file is equal to ['1', 'Charissa', 'Clark', 'yes', 'c', '7']
    assert data[1] == ['1', 'Charissa', 'Clark', 'yes', 'c', '7'], "The second row of the CSV file does not match the expected value."
   
    # check if the number of rows in the CSV file matches the number of rows in the data array
    assert len(data) == 26, "The number of rows in the CSV file does not match the expected value."
   
    # check if the last row of the CSV file is equal to ['10', 'Felicia', 'Wilkins', 'yes', 'b', '8']
    assert data[-1] == ['20', 'Felicia', 'Wilkins', 'yes', 'b', '8'], "The last row of the CSV file does not match the expected value."
   
    # check if the number of columns in each row is equal to 6
    for row in data:
        assert len(row) == 6, "The number of columns in the row does not match the expected value."