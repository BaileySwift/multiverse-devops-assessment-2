import csv

def remove_duplicates(data):
   
    # Removes duplicates from the data based on the user_id field
   
    seen = set()
    new_data = []
    for row in data:
        if row[0] not in seen:
            seen.add(row[0])
            new_data.append(row)
    return new_data

def remove_empty_lines(data):
   
   # Removes empty lines from the data
   
    return [row for row in data if any(row)]

def capitalize_names(data):
   
    # Capitalises the first_name and last_name fields
   
    for row in data:
        row[1] = row[1].capitalize()
        row[2] = row[2].capitalize()

def validate_answer_3(data):
   
    # Validates the responses in the answer_3 field. The answer must be a numeric value between 1 and 10
   
    valid_data = []
    for row in data:
        try:
            answer_3 = int(row[5])
            if 1 <= answer_3 <= 10:
                valid_data.append(row)
        except ValueError:
            pass
    return valid_data

def output_to_csv(data):
   
   # Outputs the cleansed data to a new csv file called clean_results.csv
   
    with open('clean_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'])
        writer.writerows(data)

# read the original data from the csv file
with open('results.csv') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# remove duplicates
data = remove_duplicates(data)

# remove empty lines
data = remove_empty_lines(data)

# capitalize names
capitalize_names(data)

# validate answer_3
data = validate_answer_3(data)

# output to csv
output_to_csv(data)

print("Cleaned data written to clean_results.csv")