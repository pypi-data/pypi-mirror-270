from src import test_function, sum_function, return_df


def test_test_function():
    test_function()
    assert 1==1

def test_sum_function():
    assert sum_function(1,1) == 2

def test_return_df():
    assert not return_df().empty