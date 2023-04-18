import pytest as pt

@pt.fixture
def setUp():
    print("Launching browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close browser")


def testAddItemToCart(setUp):
    print("Add Item Successful")

def testRemoveItemFromCart(setUp):
    print("Remove Item Succesful")
