import pytest as pt

# @pt.fixture(params=["a", "b"])
# def demo_fixture(request):
#     print(request.param)

@pt.mark.parametrize("a, b, final", [(2, 6, 8), (5, 8, 15), (5, 10, 15)])
def test_add(a, b, final):
    assert a + b == final 
    # print("Login Succesful")

# def testLogoff():
#     print("Logoff Succesful")

# def testCalculation():
#     assert 2 + 2 == 4