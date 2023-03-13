import csv


def read_csv_file(filename):
    data = []

    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) == 0:
                    continue
                data.append(row)
    except FileNotFoundError:
        raise AssertionError("The CSV file was not found.")
    except Exception as e:
        raise AssertionError(f"An error occurred while reading the CSV file: {e}")

    return data


def write_csv_file(filename, data):
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                writer.writerow(row)
    except Exception as e:
        raise AssertionError(f"An error occurred while writing to the CSV file: {e}")