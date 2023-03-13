import pytest
import csv_reader

# Arrange
@pytest.fixture
def csv_data():
    return csv_reader.read_csv_file('results.csv')

# Assert

def test_csv_data_length(csv_data):
    assert len(csv_data) > 0, "No data was read from the CSV file."

def test_csv_data_first_row(csv_data):
    assert csv_data[0] == ['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'], "The first row of the CSV file does not match the expected value."

def test_csv_data_second_row(csv_data):
    assert csv_data[1] == ['1', 'Charissa', 'Clark', 'yes', 'c', '7'], "The second row of the CSV file does not match the expected value."

def test_csv_data_last_row(csv_data):
    assert csv_data[-1] == ['20', 'Felicia', 'Wilkins', 'yes', 'b', '8'], "The last row of the CSV file does not match the expected value."

def test_csv_data_row_length(csv_data):
    for row in csv_data:
        assert len(row) == 6, "The number of columns in the row does not match the expected value."