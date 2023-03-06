import pytest
import os
import csv
import tempfile
from io import StringIO

from main_script import remove_duplicates, remove_empty_lines, capitalize_names, validate_answer_3, output_to_csv


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


# Test capitalize_names function
def test_capitalize_names():
    data = [
        ['1', 'john', 'doe', 'Yes', 'No', '5'],
        ['2', 'JANE', 'DOE', 'No', '', ''],
        ['3', 'john', 'smith', '', 'Yes', '8']
    ]
    expected_data = [
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'Doe', 'No', '', ''],
        ['3', 'John', 'Smith', '', 'Yes', '8']
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