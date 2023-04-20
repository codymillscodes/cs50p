from fuel import convert, gauge
import pytest

def test_convert():
    assert convert('1/2') == 50.0
    with pytest.raises(ValueError):
        convert('three/4')
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
def test_gauge():
    assert gauge(99) == 'F'
    assert gauge(95) == '95%'
    assert gauge(1) == 'E'