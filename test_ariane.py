import pytest
from ariane_example import set_speed

def test_set_speed():
    with pytest.raises(AssertionError):
        set_speed(32768)

def test_set_speed2():
    with pytest.raises(AssertionError):
        set_speed(32.78) #type:ignore   