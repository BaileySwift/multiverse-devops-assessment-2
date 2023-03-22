from csvhelper import *

# Ticket 1
data = read_csv_file('results.csv')

# Ticket 2
data = remove_duplicates(data)

# Ticket 3
data = remove_empty_lines(data)

# Ticket 4
capitalize_names(data)

# Ticket 5
data = validate_answer_3(data)

# Ticket 6
write_clean_data(data, 'clean_results.csv')