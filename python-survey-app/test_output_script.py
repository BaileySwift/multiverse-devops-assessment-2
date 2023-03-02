import csv
import pytest

@pytest.fixture(scope="output_script")
def get_data():
    with open('clean_results.csv') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        data = []
        for row in reader:
            data.append(row)
    return headers, data

def test_get_headers(get_data):
    headers, _ = get_data
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
    assert lengths[0] == 2
    assert lengths[1] == 10
    assert lengths[2] == 8
    assert lengths[3] == 3
    assert lengths[4] == 1
    assert lengths[5] == 2

def test_print_headers_and_divider(capsys, get_data):
    headers, _ = get_data
    lengths = [2, 10, 8, 3, 1, 2]
    for i in range(len(headers)):
        print(f'{headers[i]:{lengths[i]}}', end=' ')
    captured = capsys.readouterr()
    assert captured.out == 'user_id   first_name last_name answer_1 answer_2 answer_3 \n'
    for i in range(sum(lengths) + len(lengths) - 1):
        print('-', end='')
    captured = capsys.readouterr()
    assert captured.out == '---------------------------------------------------------------------\n'

def test_print_data(capsys, get_data):
    _, data = get_data
    lengths = [2, 10, 8, 3, 1, 2]
    expected_output = """1         Charissa   Clark     yes c  7
2         Richard    Mckinney  yes b  7
3         Patience   Reeves    yes b  9
5         India      Gentry    yes c  7
6         Abra       Sheppard  yes b  6
8         Diana      Cameron   yes b  9
9         Alexander Herring  no  b  4
11        Uma        Glass     yes a  2
12        Brittany  Weeks     yes b  8
13        Roth      Stout     yes c 10
14        Amos       Daniel    yes a  5
15        Caesar    Rivers    yes b  7
16        Eugenia   Nichols   yes b  6
17        Dieter    Alvarado  yes b  6
18        Roary     Frank     yes c  7
19        Ulric     Hensley  no  b  9
20        Felicia   Wilkins   yes b  8
"""
    csvfile.seek(0)
    next(data)
    for row in data:
        for i in range(len(row)):
            print(f'{row[i]:{lengths[i]}}', end=' ')
        print()
    captured = capsys.readouterr()
    assert captured.out == expected_output