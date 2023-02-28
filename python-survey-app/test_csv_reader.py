import csv

def read_csv_file(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row:
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

def test_read_csv_file():
    data = read_csv_file('results.csv')
    assert len(data) == 20
    assert data[0]['user_id'] == '1'
    assert data[0]['first_name'] == 'Charissa'
    assert data[0]['last_name'] == 'Clark'
    assert data[0]['answer_1'] == 'yes'
    assert data[0]['answer_2'] == 'c'
    assert data[0]['answer_3'] == '7'

def test_remove_duplicates():
    data = [
        {'user_id': '1', 'first_name': 'Charissa', 'last_name': 'Clark', 'answer_1': 'yes', 'answer_2': 'c', 'answer_3': '7'},
        {'user_id': '2', 'first_name': 'Richard', 'last_name': 'McKinney', 'answer_1': 'yes', 'answer_2': 'b', 'answer_3': '7'},
        {'user_id': '1', 'first_name': 'Charissa', 'last_name': 'Clark', 'answer_1': 'no', 'answer_2': 'a', 'answer_3': '5'}
    ]
    new_data = remove_duplicates(data)
    assert len(new_data) == 2
    assert new_data[0]['user_id'] == '1'
    assert new_data[0]['first_name'] == 'Charissa'
    assert new_data[0]['last_name'] == 'Clark'
    assert new_data[0]['answer_1'] == 'yes'
    assert new_data[0]['answer_2'] == 'c'
    assert new_data[0]['answer_3'] == '7'
    assert new_data[1]['user_id'] == '2'
    assert new_data[1]['first_name'] == 'Richard'
    assert new_data[1]['last_name'] == 'McKinney'
    assert new_data[1]['answer_1'] == 'yes'
    assert new_data[1]['answer_2'] == 'b'
    assert new_data[1]['answer_3'] == '7'
    
def test_read_csv_file_with_capitalized_names():
    # Arrange
    expected_data = [
        {'user_id': '1', 'first_name': 'Charissa', 'last_name': 'Clark', 'answer_1': 'yes', 'answer_2': 'c', 'answer_3': '7'},
        {'user_id': '2', 'first_name': 'Richard', 'last_name': 'Mckinney', 'answer_1': 'yes', 'answer_2': 'b', 'answer_3': '7'},
        {'user_id': '3', 'first_name': 'Patience', 'last_name': 'Reeves', 'answer_1': 'yes', 'answer_2': 'b', 'answer_3': '9'},
        {'user_id': '4', 'first_name': 'Harding', 'last_name': 'Estrada', 'answer_1': 'no', 'answer_2': 'b', 'answer_3': '14'},
        {'user_id': '5', 'first_name': 'India', 'last_name': 'Gentry', 'answer_1': 'yes', 'answer_2': 'c', 'answer_3': '7'},
        {'user_id': '6', 'first_name': 'Abra', 'last_name': 'Sheppard', 'answer_1': 'yes', 'answer_2': 'b', 'answer_3': '6'},
        {'user_id': '6', 'first_name': 'Abra', 'last_name': 'Sheppard', 'answer_1': 'no', 'answer_2': 'a', 'answer_3': '8'},
        {'user_id': '7', 'first_name': 'Bryar', 'last_name': 'Cooley', 'answer_1': 'yes', 'answer_2': 'a', 'answer_3': '11'},
        {'user_id': '8', 'first_name': 'Diana', 'last_name': 'Cameron', 'answer_1': 'yes', 'answer_2': 'b', 'answer_3': '9'},
        {'user_id': '9', 'first_name': 'Alexander', 'last_name': 'Herring', 'answer_1': 'no', 'answer_2': 'b', 'answer_3': '4'},
        {'user_id': '10', 'first_name': 'Graiden', 'last_name': 'Cannon', 'answer_1': 'yes', 'answer_2': 'a', 'answer_3': '10'}
    ]
    input_file = 'test_data.csv'
    
    # Act
    actual_data = read_csv_file(input_file)
    
    # Assert
    assert actual_data == expected_data
    
    # Check if first_name and last_name are capitalized in actual_data
    for row in actual_data:
        assert row['first_name'].isupper() == False  # make sure not all upper case
        assert row['last_name'].isupper() == False  # make sure not all upper case
        assert row['first_name'][0].isupper() == True  # check if first letter is capitalized
        assert row['last_name'][0].isupper() == True  # check if first letter is capitalized


if __name__ == '__main__':
    input_file = 'results.csv'
    data = read_csv_file(input_file)
    data = remove_duplicates(data)
    
    # print final data
    for row in data:
        print(row)