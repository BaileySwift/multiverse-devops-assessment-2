import csv
import os

def read_csv_file(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row:
                row['first_name'] = row['first_name'].capitalize()  # capitalize first name
                row['last_name'] = row['last_name'].capitalize()  # capitalize last name
                data.append(row)
    return data

def remove_duplicates(data):
    seen_ids = set()
    new_data = []
    for row in data:
        if row['user_id'] not in seen_ids:
            seen_ids.add(row['user_id'])
            new_data.append(row)
    return new_data

def validate_answer_3(data):
    valid_data = []
    for row in data:
        if 'answer_3' in row and row['answer_3'].isdigit():
            answer_3 = int(row['answer_3'])
            if 1 <= answer_3 <= 10:
                valid_data.append(row)
    return valid_data

def test_validate_answer_3():
    data = [
        {'user_id': '1', 'first_name': 'John', 'last_name': 'Doe', 'answer_3': '5'},
        {'user_id': '2', 'first_name': 'Jane', 'last_name': 'Doe', 'answer_3': '10'},
        {'user_id': '3', 'first_name': 'Bob', 'last_name': 'Smith', 'answer_3': '3'},
        {'user_id': '4', 'first_name': 'Alice', 'last_name': 'Johnson', 'answer_3': '0'},
        {'user_id': '5', 'first_name': 'Eve', 'last_name': 'Davis', 'answer_3': '11'},
        {'user_id': '6', 'first_name': 'Mike', 'last_name': 'Taylor', 'answer_2': 'b'},
        {'user_id': '7', 'first_name': 'Lisa', 'last_name': 'Brown'},
        {'user_id': '8', 'first_name': 'Tom', 'last_name': 'Wilson', 'answer_3': '7.5'},
        {'user_id': '9', 'first_name': 'Jerry', 'last_name': 'Lee', 'answer_3': '7.0'},
    ]
    expected_valid_data = [
        {'user_id': '1', 'first_name': 'John', 'last_name': 'Doe', 'answer_3': '5'},
        {'user_id': '2', 'first_name': 'Jane', 'last_name': 'Doe', 'answer_3': '10'},
        {'user_id': '3', 'first_name': 'Bob', 'last_name': 'Smith', 'answer_3': '3'},
        {'user_id': '9', 'first_name': 'Jerry', 'last_name': 'Lee', 'answer_3': '7.0'},
    ]
    assert validate_answer_3(data) == expected_valid_data

def test_clean_csv_file_creation():
    # Arrange
    input_file = 'test_data.csv'
    expected_data = [
        {'user_id': '1', 'first_name': 'Charissa', 'last_name': 'Clark', 'answer_1': 'yes', 'answer_2': 'c', 'answer_3': '7'},
        {'user_id': '2', 'first_name': 'Richard', 'last_name': 'Mckinney', 'answer_1': 'yes', 'answer_2': 'b', 'answer_3': '7'},
        {'user_id': '3', 'first_name': 'Patience', 'last_name': 'Reeves', 'answer_1': 'yes', 'answer_2': 'b', 'answer_3': '9'},
        {'user_id': '5', 'first_name': 'India', 'last_name': 'Gentry', 'answer_1': 'yes', 'answer_2': 'c', 'answer_3': '7'},
        {'user_id': '6', 'first_name': 'Abra', 'last_name': 'Sheppard', 'answer_1': 'yes', 'answer_2': 'b', 'answer_3': '6'},
        {'user_id': '7', 'first_name': 'Bryar', 'last_name': 'Cooley', 'answer_1': 'yes', 'answer_2': 'a', 'answer_3': '11'},
        {'user_id': '8', 'first_name': 'Diana', 'last_name': 'Cameron', 'answer_1': 'yes', 'answer_2': 'b', 'answer_3': '9'},
        {'user_id': '9', 'first_name': 'Alexander', 'last_name': 'Herring', 'answer_1': 'no', 'answer_2': 'b', 'answer_3': '4'},
    ]

    # Act
    clean_file = 'clean_results.csv'
    data = read_csv_file(input_file)
    data = remove_duplicates(data)

    with open(clean_file, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    # Assert
    assert os.path.exists(clean_file)  # check if file was created
    with open(clean_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        actual_data = [row for row in reader]

    assert actual_data == expected_data  # check if content of file matches expected data
    os.remove(clean_file)  # remove test file after test

if __name__ == '__main__':
    input_file = 'results.csv'
    data = read_csv_file(input_file)
    data = remove_duplicates(data)
    data = validate_answer_3(data)

    # print final data
    for row in data:
        print(row)
