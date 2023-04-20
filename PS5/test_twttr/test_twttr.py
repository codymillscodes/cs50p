from twttr import shorten

def test_twttr():
    assert shorten('eat the rich') == 't th rch'
    assert shorten('ACAB') == 'CB'
    assert shorten('1312') == '1312'
    assert shorten('hello, world') == 'hll, wrld'