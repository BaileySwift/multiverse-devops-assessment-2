import csv

def read_csv_file(file_path):
    data = []
    user_ids = set()
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Check if the User ID has already been addedd to the set
            if row['user_id'] not in user_ids:
                data.append(row)
                user_ids.add(row['user_id'])
                
    return data