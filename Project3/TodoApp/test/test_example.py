import pytest



def test_equal_or_not_equal():
    assert 3 == 3
    assert 3 != 2

def test_isinstance():
    assert isinstance('this is a string', str)
    assert not isinstance('10', int)

def test_boolean():
    validated = True
    assert validated is True
    assert ('hello' == 'world') is False

def test_type():
    assert type('hello' is str)
    assert type('word' is str)

def test_gt_and_lt():
    assert 7 > 3
    assert 4 < 10

def test_list():
    num_list= [1,2,3,4,5]
    any_list = [False,False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)


class Student:
    def __init__(self,first_name : str, last_name : str, major : str, years : int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years

# def test_person_initialization():
#     p = Student('John', 'Doe', 'Computer Science', 3)
#     assert p.first_name == 'John', "Fisrt Name should Be John"
#     assert p.last_name == 'Doe', "Fisrt Name should Be Doe"
#     assert p.major == 'Computer Science'
#     assert p.years == 3


@pytest.fixture
def default_employee():
    return Student('John', 'Doe', 'Computer Science', 3)
        
def test_person_initialization(default_employee):
    assert default_employee.first_name == 'John', "Fisrt Name should Be John"
    assert default_employee.last_name == 'Doe', "Fisrt Name should Be Doe"
    assert default_employee.major == 'Computer Science'
    assert default_employee.years == 3