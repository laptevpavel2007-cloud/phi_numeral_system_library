import pytest
from PhiBase import PhiBase
from PhiNumber import _PhiNumber

TEST_DATA = {
    1: "1",
    2: "10.01",
    3: "100.01",
    4: "101.01",
    42: "10100010.00100001",
    451: "1010000001010.000100000101"
}

def test_creation():

    for i in ["0", "1", "10.01", "101.01", "1000.1001"]:
        x = PhiBase(i)
        assert x.x == i
        
    for i in ["2", "11", "1.1.1", "abc", "0.11"]:
        with pytest.raises(TypeError):
            PhiBase(i)

def test_transfer_to_num():

    for n, s in TEST_DATA.items():
        x = PhiBase(s)
        y = PhiBase.transfer_to_number(x)
        assert y == _PhiNumber(n, 0)
    
    x = PhiBase("0.1")
    y = PhiBase.transfer_to_number(x)

    phi = _PhiNumber.phi()
    res = phi - _PhiNumber(1, 0) 
    assert y == res

def test_transfer_to_phi():

    for n, s in TEST_DATA.items():
        x = PhiBase.transfer_to_Phi(n)
        assert x.x == s
        assert "11" not in x.x.replace('.', '')

def test_sum():

    a = PhiBase.transfer_to_Phi(1)   
    b = PhiBase.transfer_to_Phi(2)   
    c = a + b                      
    assert c.x == TEST_DATA[3]
    
    n = PhiBase.transfer_to_number(c)
    assert n == _PhiNumber(3, 0)

def test_sub():

    a = PhiBase.transfer_to_Phi(3)
    b = PhiBase.transfer_to_Phi(2)
    c = a - b
    assert c.x == TEST_DATA[1]

    s = PhiBase.transfer_to_number(c)
    assert s == _PhiNumber(1, 0)

def test_mul():

    a = PhiBase.transfer_to_Phi(2)
    b = PhiBase.transfer_to_Phi(3)
    c = a * b   

    s = PhiBase.transfer_to_number(c)
    assert s == _PhiNumber(6, 0)

    assert "11" not in c.x.replace('.', '')

def test_norm():

    data = [
        ("011", "100"),
        ("0110", "1000"),
        ("0.11", "1.00"),
        ("01.1", "10.0"),
        ("01.10", "10.00"),
        ("11.01", "100.01"),
    ]

    for raw, exp in data:
        res = PhiBase.normalization(raw)

        assert res == exp

        assert "11" not in res.replace('.', '')

if __name__ == "__main__":
    pytest.main()