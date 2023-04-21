from working import convert
import pytest

def test_exceptions():
    with pytest.raises(ValueError):
        convert('12am - 12pm')
    #with pytest.raises(ValueError):
    #   convert([1, 2])
    with pytest.raises(ValueError):
        convert('if you like pina coladas')
    with pytest.raises(ValueError):
        convert('!!!!!!!!!!!!')
    with pytest.raises(ValueError):
        convert('8:60 AM to 4:60 PM')
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
        convert('10:7 AM - 5:1 PM')
    with pytest.raises(ValueError):
        convert('to')

def test_conversions():
    assert convert('12:00 AM to 12:00 PM') == '00:00 to 12:00'
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'
    assert convert('2:14 PM to 11:59 AM') == '14:14 to 11:59'

def test_misc():
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'