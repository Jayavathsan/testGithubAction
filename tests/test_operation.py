from src.math_operations import add,sub

def test_add():
    assert add(2,5)==7
    assert add(-1,1)==0
    assert add(10,5)==15
    assert add(10,-10)==0

def test_sub():
    assert sub(5,3)==2
    assert sub(4,6)==-2
    assert sub(5,-5)==10
    assert sub(5,5)==0
