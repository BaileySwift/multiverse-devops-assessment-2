import pytest
import os
import io
import sys
from csvhelper import *

# Ticket 1 Tests

# Test 1: Check that the function returns an empty list when given an empty file.
def test_read_csv_file_empty_file():
    # Arrange
    filename = 'empty_file.csv'
    with open(filename, 'w') as csvfile:
        pass

    # Act
    result = read_csv_file(filename)

    # Assert
    assert result == []

    # Clean up
    os.remove(filename)

# Test 2: Check that the function raises a FileNotFoundError when given a non-existent file.
def test_read_csv_file_nonexistent_file():
    # Arrange
    filename = 'nonexistent_file.csv'
    if os.path.exists(filename):
        os.remove(filename)

    # Act and Assert
    with pytest.raises(FileNotFoundError):
        read_csv_file(filename)

# Ticket 2 Tests

# Test 1: checks that the function returns an empty list when given an empty list as input
def test_remove_duplicates_empty_input():
    # Arrange
    data = []

    # Act
    result = remove_duplicates(data)

    # Assert
    assert result == []

# Test 2: checks that the function returns the same list when given input with no duplicates.
def test_remove_duplicates_no_duplicates():
    # Arrange
    data = [
        ['1', 'John', 'Doe'],
        ['2', 'Jane', 'Doe'],
        ['3', 'Bob', 'Smith'],
    ]

    # Act
    result = remove_duplicates(data)

    # Assert
    assert result == data
    
# Test 3: checks that the function removes one duplicate when given input with one duplicate.
def test_remove_duplicates_one_duplicate():
    # Arrange
    data = [
        ['1', 'John', 'Doe'],
        ['2', 'Jane', 'Doe'],
        ['1', 'John', 'Doe'],
        ['3', 'Bob', 'Smith'],
    ]

    # Act
    result = remove_duplicates(data)

    # Assert
    assert result == [
        ['1', 'John', 'Doe'],
        ['2', 'Jane', 'Doe'],
        ['3', 'Bob', 'Smith'],
    ]
    
# Test 4: checks that the function removes multiple duplicates when given input with multiple duplicates.
def test_remove_duplicates_multiple_duplicates():
    # Arrange
    data = [
        ['1', 'John', 'Doe'],
        ['2', 'Jane', 'Doe'],
        ['1', 'John', 'Doe'],
        ['3', 'Bob', 'Smith'],
        ['2', 'Jane', 'Doe'],
    ]

    # Act
    result = remove_duplicates(data)

    # Assert
    assert result == [
        ['1', 'John', 'Doe'],
        ['2', 'Jane', 'Doe'],
        ['3', 'Bob', 'Smith'],
    ]

# Ticket 3 Tests

# Test 1: Check that the function returns an empty list when given an empty list.
def test_remove_empty_lines_empty_list():
    # Arrange
    data = []

    # Act
    result = remove_empty_lines(data)

    # Assert
    assert result == []


# Test 2: Check that the function returns the original data when there are no empty lines.
def test_remove_empty_lines_no_empty_lines():
    # Arrange
    data = [
        ['1', 'Name1', 'Email1'],
        ['2', 'Name2', 'Email2'],
        ['3', 'Name3', 'Email3'],
        ['4', 'Name4', 'Email4']
    ]

    # Act
    result = remove_empty_lines(data)

    # Assert
    assert result == data

# Ticket 4 Tests

# Test 1: tests whether the function can handle input data that is all in uppercase
def test_capitalize_names_all_caps():
    # Arrange
    input_data = [
        [1, "JOHN", "DOE"],
        [2, "JANE", "DOE"]
    ]
    expected_output = [
        [1, "John", "Doe"],
        [2, "Jane", "Doe"]
    ]

    # Act
    capitalize_names(input_data)

    # Assert
    assert input_data == expected_output

# Test 2: tests whether the function can handle input data that is in mixed case
def test_capitalize_names_mixed_case():
    # Arrange
    input_data = [
        [1, "jOhN", "dOe"],
        [2, "jAnE", "dOe"]
    ]
    expected_output = [
        [1, "John", "Doe"],
        [2, "Jane", "Doe"]
    ]

    # Act
    capitalize_names(input_data)

    # Assert
    assert input_data == expected_output

# Test 3: tests whether the function correctly leaves already capitalized names unchanged.
def test_capitalize_names_already_capitalized():
    # Arrange
    input_data = [
        [1, "John", "Doe"],
        [2, "Jane", "Doe"]
    ]
    expected_output = [
        [1, "John", "Doe"],
        [2, "Jane", "Doe"]
    ]

    # Act
    capitalize_names(input_data)

    # Assert
    assert input_data == expected_output

# Ticket 5 Tests

# Test 1: tests the scenario where all the rows in the input data have valid values for answer_3, 
def test_validate_answer_3_valid_values():
    # Arrange
    data = [
        ["1", "John", "Doe", "25", "M", "5"],
        ["2", "Jane", "Smith", "35", "F", "1"],
        ["3", "Bob", "Johnson", "42", "M", "10"]
    ]

    # Act
    result = validate_answer_3(data)

    # Assert
    assert len(result) == 3
    assert result == data

# Test 2: tests the scenario where some rows in the input data have invalid values for answer_3
def test_validate_answer_3_invalid_values():
    # Arrange
    data = [
        ["1", "John", "Doe", "25", "M", "15"],
        ["2", "Jane", "Smith", "35", "F", "0"],
        ["3", "Bob", "Johnson", "42", "M", "Invalid"]
    ]

    # Act
    result = validate_answer_3(data)

    # Assert
    assert len(result) == 0
    assert result == []
    
# Test 3: tests the scenario where some rows in the input data have non-integer values for answer_3
def test_validate_answer_3_mixed_values():
    # Arrange
    data = [
        ["1", "John", "Doe", "25", "M", "5"],
        ["2", "Jane", "Smith", "35", "F", "15"],
        ["3", "Bob", "Johnson", "42", "M", "Invalid"]
    ]

    # Act
    result = validate_answer_3(data)

    # Assert
    assert len(result) == 1
    assert result == [["1", "John", "Doe", "25", "M", "5"]]

 # Ticket 6 Tests

# Test 1: ensures that the output file is actually created
def test_output_file_created(tmp_path):
    data = [
        ['1', 'Alice', 'Jones', 'yes', 'no', '5'],
        ['2', 'Bob', 'Smith', 'no', 'yes', '7'],
        ['3', 'Charlie', 'Brown', 'yes', 'yes', '3']
    ]
    filename = os.path.join(tmp_path, 'test_output_file_created.csv')
    write_clean_data(data, filename)
    assert os.path.exists(filename)

# Test 2: ensures that the output file has the correct header and data rows.
def test_output_file_format(tmp_path):
    data = [
        ['1', 'Alice', 'Jones', 'yes', 'no', '5'],
        ['2', 'Bob', 'Smith', 'no', 'yes', '7'],
        ['3', 'Charlie', 'Brown', 'yes', 'yes', '3']
    ]
    filename = os.path.join(tmp_path, 'test_output_file_format.csv')
    write_clean_data(data, filename)
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header == ['User ID', 'First Name', 'Last Name', 'Answer 1', 'Answer 2', 'Answer 3']
        rows = list(reader)
        assert rows == data

# Test 3: ensures that an empty input file produces an empty output file
def test_output_file_empty(tmp_path):
    data = []
    filename = os.path.join(tmp_path, 'test_output_file_empty.csv')
    write_clean_data(data, filename)
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header == ['User ID', 'First Name', 'Last Name', 'Answer 1', 'Answer 2', 'Answer 3']
        assert len(list(reader)) == 0