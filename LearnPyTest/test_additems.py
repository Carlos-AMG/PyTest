import pytest as pt

@pt.mark.sanity
def testLogin():
    print("Login Succesful")

def testLogoff():
    print("Logoff Succesful")

def testCalculation():
    assert 2 + 2 == 4