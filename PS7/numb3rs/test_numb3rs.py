from numb3rs import validate

def test_alpha():
    assert validate('a.a.a.a') == False
    assert validate('a!') == False

def test_range():
    assert validate('-1.-1.23.1') == False
    assert validate('192.168.1.1') == True
    assert validate('420.420.420.420') == False
    assert validate('1') == False
    assert validate('129.666.666.666') == False