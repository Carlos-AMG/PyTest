import pytest as pt

@pt.mark.skip
def testLogin():
    print("Login Succesful")

@pt.mark.regression
def testLogoff():
    print("Logoff Succesful")

@pt.mark.xfail
def testCalculation():
    assert 2 + 2 == 6