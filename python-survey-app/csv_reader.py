import csv

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

if __name__ == '__main__':
    input_file = 'results.csv'
    data = read_csv_file(input_file)
    data = remove_duplicates(data)
    
    # print final data
    for row in data:
        print(row)