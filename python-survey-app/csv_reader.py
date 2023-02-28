import csv

def read_csv_file(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row:
                row['first_name'] = row['first_name'].capitalize()  # capitalize first name
                row['last_name'] = row['last_name'].capitalize()  # capitalize last name
                try:
                    answer_3 = int(row['answer_3'])
                    if answer_3 < 1 or answer_3 > 10:
                        continue  # ignore invalid answer_3 values
                except ValueError:
                    continue  # ignore non-numeric answer_3 values
                row['answer_3'] = str(answer_3)
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
    
    # write clean data to new file
    with open('clean_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'])
        for row in data:
            writer.writerow([row['user_id'], row['first_name'], row['last_name'], row['answer_1'], row['answer_2'], row['answer_3']])