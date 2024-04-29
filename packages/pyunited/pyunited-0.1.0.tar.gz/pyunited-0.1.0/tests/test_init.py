import pytest

import pyunited as pu

@pytest.mark.unit
def test_base_units():
    # Test unit type
    a = pu.United(1)
    assert a == 1
    
@pytest.mark.unit
def test_conversion():
    a = 10 * pu.mm
    assert a.to(pu.m) == 0.01 * pu.m
    
@pytest.mark.unit
def test_parsing():
    a = pu("10 m")
    assert a == 10 * pu.m
    
@pytest.mark.unit
def test_callable():
    inputs = [
        "10 m",
        "5 inch",
        "20 mm",
    ]
    parsed = list(map(lambda x: pu.United(x), inputs))
    assert parsed == [10 * pu.m, 5 * pu.inch, 20 * pu.mm]
    
    united = list(map(pu.to(pu.m), parsed))
    assert united == [10 * pu.m, 0.127 * pu.m, 0.02 * pu.m]
    
    values = list(pu.values(united))
    assert values == [10, 0.127, 0.02]
    
    with pytest.raises(pu.UnityError):
        pu.values([
            1 * U.m,
            2 * U.mm,
        ])
