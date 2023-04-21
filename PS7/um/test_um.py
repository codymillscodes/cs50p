from um import count

def test_words():
    assert count('UM UM UM YUM') == 3
    assert count('umbrella') == 0

def test_num():
    assert count('one') == 0

def test_misc():
    assert count('!@#$!%^um&*') == 1
    assert count('!@#$%') == 0