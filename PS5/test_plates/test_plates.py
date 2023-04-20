from plates import is_valid

def test_plates():
    assert is_valid('GAMBINO') == False
    assert is_valid('AAA111') == True

def test_plates_num():
    assert is_valid('42069') == False
    s1 = 'aa1234'
    s2 = '1234aa'
    assert is_valid(s1) == True
    assert is_valid(s2) == False
    assert is_valid('11') == False
    assert is_valid('10') == False
    assert is_valid('aaa01') == False
    assert is_valid('aaa200') == True
    assert is_valid('AaA2_1') == False
    assert is_valid('CS50') == True
    assert is_valid('aaaaa1') == True
    assert is_valid('aa1aaa') == False

def test_plates_length():
    assert is_valid('AA') == True
    assert is_valid('aa1234567789') == False
    assert is_valid('aa123') == True

def test_plates_punc():
    assert is_valid(',,,,') == False
    assert is_valid('!#%@') == False