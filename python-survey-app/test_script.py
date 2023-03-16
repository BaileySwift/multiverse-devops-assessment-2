import pytest
import os
import csv
import tempfile
from io import StringIO
import script1
import script2

from script2 import remove_duplicates, remove_empty_lines, capitalize_names, validate_answer_3, output_to_csv, print_csv
from script1 import read_csv_file, write_csv_file

# testing csv reader

# Arrange
@pytest.fixture
def csv_data():
    return read_csv_file('results.csv')

# Assert

def test_csv_data_length(csv_data):
    assert len(csv_data) > 0, "No data was read from the CSV file."

def test_csv_data_first_row(csv_data):
    assert csv_data[0] == ['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'], "The first row of the CSV file does not match the expected value."

def test_csv_data_second_row(csv_data):
    assert csv_data[1] == ['1', 'Charissa', 'Clark', 'yes', 'c', '7'], "The second row of the CSV file does not match the expected value."

def test_csv_data_row_length(csv_data):
    for row in csv_data:
        assert len(row) == 6, "The number of columns in the row does not match the expected value."
        
# testing main script

# Test remove_duplicates function
def test_remove_duplicates():
    data = [
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'Doe', 'No', '', ''],
        ['3', 'John', 'Smith', '', 'Yes', '8'],
        ['1', 'John', 'Doe', '', '', '9']
    ]
    expected_data = [
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'Doe', 'No', '', ''],
        ['3', 'John', 'Smith', '', 'Yes', '8']
    ]
    assert remove_duplicates(data) == expected_data

    # Test when there are no duplicates in the data
    data = [
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'Doe', 'No', '', ''],
        ['3', 'John', 'Smith', '', 'Yes', '8'],
        ['4', 'Tom', 'Hanks', 'Yes', 'No', '9']
    ]
    expected_data = data
    assert remove_duplicates(data) == expected_data


# Test remove_empty_lines function
def test_remove_empty_lines():
    data = [
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'Doe', 'No', '', ''],
        ['3', 'John', 'Smith', '', 'Yes', '8'],
        ['', '', '', '', '', '']
    ]
    expected_data = [
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'Doe', 'No', '', ''],
        ['3', 'John', 'Smith', '', 'Yes', '8']
    ]
    assert remove_empty_lines(data) == expected_data

    # Test when all lines are empty
    data = [
        ['', '', '', '', '', ''],
        ['', '', '', '', '', ''],
        ['', '', '', '', '', '']
    ]
    expected_data = []
    assert remove_empty_lines(data) == expected_data


# Test capitalize_names function
def test_capitalize_names():
    # Test with all lowercase names
    data = [        
        ['1', 'john', 'doe', 'Yes', 'No', '5'],
        ['2', 'jane', 'doe', 'No', '', ''],
        ['3', 'john', 'smith', '', 'Yes', '8']
    ]
    expected_data = [        
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'Doe', 'No', '', ''],
        ['3', 'John', 'Smith', '', 'Yes', '8']
    ]
    capitalize_names(data)
    assert data == expected_data

    # Test with all uppercase names
    data = [        
        ['1', 'JOHN', 'DOE', 'Yes', 'No', '5'],
        ['2', 'JANE', 'DOE', 'No', '', ''],
        ['3', 'JOHN', 'SMITH', '', 'Yes', '8']
    ]
    expected_data = [        
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'Doe', 'No', '', ''],
        ['3', 'John', 'Smith', '', 'Yes', '8']
    ]
    capitalize_names(data)
    assert data == expected_data

    # Test with mixed case names
    data = [        
        ['1', 'jOhn', 'DoE', 'Yes', 'No', '5'],
        ['2', 'jAnE', 'DoE', 'No', '', ''],
        ['3', 'jOhN', 'sMiTh', '', 'Yes', '8']
    ]
    expected_data = [        
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'Doe', 'No', '', ''],
        ['3', 'John', 'Smith', '', 'Yes', '8']
    ]
    capitalize_names(data)
    assert data == expected_data

    # Test with non-alphabetic characters in name fields
    data = [        
        ['1', 'john123', 'doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'doe@#', 'No', '', ''],
        ['3', 'john', 'smith99', '', 'Yes', '8']
    ]
    expected_data = [        
        ['1', 'John123', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'Doe@#', 'No', '', ''],
        ['3', 'John', 'Smith99', '', 'Yes', '8']
    ]
    capitalize_names(data)
    assert data == expected_data

# Test validate_answer_3 function
def test_validate_answer_3():
    data = [
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'Doe', 'No', '', '11'],
        ['3', 'John', 'Smith', '', 'Yes', '8'],
        ['4', 'Tom', 'Hanks', 'Yes', 'No', 'abc']
    ]
    expected_data = [
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['3', 'John', 'Smith', '', 'Yes', '8']
    ]
    assert validate_answer_3(data) == expected_data
   
@pytest.fixture
def data():
    return [
        [1, 'John', 'Doe', 'Yes', 'No', 'Maybe'],
        [2, 'Jane', 'Doe', 'No', 'Yes', 'Maybe'],
        [3, 'Alice', 'Smith', 'Maybe', 'Maybe', 'No'],
    ]
    
# test output script

# Create a sample CSV file with the expected header row
sample_csv = '''user_id,first_name,last_name,answer_1,answer_2,answer_3
1,Charissa,Clark,yes,c,7
2,Richard,Mckinney,yes,b,7They are proper random name
3,Patience,Reeves,yes,b,9
5,India,Gentry,yes,c,7
6,Abra,Sheppard,yes,b,6
8,Diana,Cameron,yes,b,9
9,Alexander,Herring,no,b,4
11,Uma,Glass,yes,a,2
12,Brittany,Weeks,yes,b,8
13,Roth,Stout,yes,c,10
14,Amos,Daniel,yes,a,5
15,Caesar,Rivers,yes,b,7
16,Eugenia,Nichols,yes,b,6
17,Dieter,Alvarado,yes,b,6
18,Roary,Frank,yes,c,7
19,Ulric,Hensley,no,b,9
20,Felicia,Wilkins,yes,b,8
'''

@pytest.fixture(scope="session")
def get_data(tmp_path_factory):
    # Create a temporary file in the test directory and write the sample CSV data
    csv_path = tmp_path_factory.mktemp("data").joinpath("test.csv")
    with csv_path.open("w", newline="") as f:
        f.write(sample_csv)

    with csv_path.open() as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        data = []
        for row in reader:
            data.append(row)
    return headers, data

def test_get_headers(get_data):
    headers, _ = get_data
    print(headers)
    assert len(headers) == 6
    assert headers[0] == 'user_id'
    assert headers[1] == 'first_name'
    assert headers[2] == 'last_name'
    assert headers[3] == 'answer_1'
    assert headers[4] == 'answer_2'
    assert headers[5] == 'answer_3'

def test_get_max_lengths(get_data):
    _, data = get_data
    lengths = [0] * 6
    for row in data:
        for i in range(len(row)):
            lengths[i] = max(lengths[i], len(row[i]))
    print(lengths)  # add this line to print the lengths of each column
    assert lengths[0] == 2
    assert lengths[1] == 9
    assert lengths[2] == 8
    assert lengths[3] == 3
    assert lengths[4] == 1
    assert lengths[5] == 28  # update this assertion as necessary