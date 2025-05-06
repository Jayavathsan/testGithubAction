from src.math_operations import add,sub

def test_add():
    assert add(2,5)==5
    assert add(-1,1)==0
    assert add(10,5)==15

def test_sub():
    assert sub(5,3)==2
    assert sub(4,6)==-1
    assert sub(5-5)==0