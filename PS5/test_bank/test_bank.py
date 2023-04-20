from bank import value

def test_bank():
    assert value('hello') == 0
    assert value('hey') == 20
    assert value('WAKKA WAKKA') == 100

def test_bank_correct():
    assert value('HELLO') == 0

def test_bank_wacky():
    assert value('1231341345236') == 100