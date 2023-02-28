import pytest
from csv_reader import read_csv_file

@pytest.fixture
def sample_data():
    return [
        ['user_id','first_name','last_name','answer_1','answer_2','answer_3'],
        ['1','Charissa','Clark','yes','c','7'],
        ['richard','McKinney','yes','b','7'],
        ['','','','','',''],
        ['3','patience','reeves','yes','b','9'],
        ['4','Harding','Estrada','no','b','14'],
        ['5','India','Gentry','yes','c','7'],
        ['6','Abra','Sheppard','yes','b','6'],
        ['6','Abra','Sheppard','no','a','8'],
        ['7','Bryar','cooley','yes','a','11'],
        ['8','Diana','Cameron','yes','b','9'],
        ['9','Alexander','Herring','no','b','4'],
        ['10','Graiden','Cannon','no','b','13'],
        ['11','Uma','Glass','yes','a','2'],
        ['12','Brittany','Weeks','yes','b','8'],
        ['13','Roth','Stout','yes','c','10'],
        ['14','Amos','Daniel','yes','a','5'],
        ['','','','','',''],
        ['15','Caesar','Rivers','yes','b','7'],
        ['16','Eugenia','Nichols','yes','b','6'],
        ['17','dieter','alvarado','yes','b','6'],
        ['17','Dieter','Alvarado','no','c','7'],
        ['17','Dieter','Alvarado','yes','a','9'],
        ['18','Roary','Frank','yes','c','7'],
        ['19','Ulric','Hensley','no','b','9'],
        ['20','Felicia','Wilkins','yes','b','8'],
    ]
    
def test_read_csv_file(sample_data):
    file_path = 'results.csv'
    assert read_csv_file(file_path) == sample_data
    
def test_read_csv_file_with_nonexistent_file():
    file_path = 'nonexistent.csv'
    with pytest.raises(FileNotFoundError):
        read_csv_file(file_path)