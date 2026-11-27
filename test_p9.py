from p9 import  check_eligible

def test_check_eligible():
    assert check_eligible(2)== "eligible"
    assert check_eligible(9)== "not eligible"
    assert check_eligible(-2)== "not eligible"
