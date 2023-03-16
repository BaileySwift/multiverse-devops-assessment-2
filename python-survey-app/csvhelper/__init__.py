import csv


def read_csv_file(filename):
    """
    Reads data from a CSV file and processes it into an array.

    Each line of the file is read into a new array item.
    """
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader]


def remove_duplicates(data):
    """
    Ignores or removes any duplicate entries from the input data.

    Duplicates are placed on the User Id field.
    A final array is created with duplicate entries removed.
    Where duplicates are found, the first entry is retained.
    """
    seen_ids = set()
    output = []
    for row in data:
        if row[0] not in seen_ids:
            seen_ids.add(row[0])
            output.append(row)
    return output


def remove_empty_lines(data):
    """
    Ignores empty lines found when reading in the input data file.

    A final array is created with empty lines omitted.
    """
    return [row for row in data if any(row)]


def capitalize_names(data):
    """
    Capitalizes the first_name and last_name fields found in the input data.
    """
    for row in data:
        row[1] = row[1].capitalize()
        row[2] = row[2].capitalize()


def validate_answer_3(data):
    """
    Validates the responses to the answer_3 field.

    This answer must have a numeric value between 1 and 10.
    Any rows with an invalid value are ignored.
    A final array is created with the input data excluding any rows where the answer_3 field is invalid.
    """
    output = []
    for row in data:
        try:
            answer_3 = int(row[5])
            if 1 <= answer_3 <= 10:
                output.append(row)
        except ValueError:
            pass
    return output


def write_clean_data(data, filename):
    """
    Outputs the cleansed data to a new CSV file.

    The file needs to be recreated on each execution.
    No invalid or unformatted data is present in the new file.
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['User ID', 'First Name', 'Last Name', 'Answer 1', 'Answer 2', 'Answer 3'])
        writer.writerows(data)


def print_clean_data(filename):
    """
    Reads in the clean data file and prints the results to the console,
    row by row, with appropriate headers and fixed length strings.
    """
    data = read_csv_file(filename)
    header = ["User ID", "First Name", "Last Name", "Answer 1", "Answer 2", "Answer 3"]
    print(f"{header[0]:<10}{header[1]:<15}{header[2]:<15}{header[3]:<15}{header[4]:<15}{header[5]:<15}")
    for i, row in enumerate(data):
        if i == 0:
            continue # skip header row
        print(f"{row[0]:<10}{row[1]:<15}{row[2]:<15}{row[3]:<15}{row[4]:<15}{row[5]:<15}")
