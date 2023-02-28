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

if __name__ == '__main__':
    input_file = 'results.csv'
    data = read_csv_file(input_file)
    data = remove_duplicates(data)
    
    # print final data
    for row in data:
        print(row)