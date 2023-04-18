import pytest as pt

@pt.fixture(scope="session", autouse=True)
def tc_setup():
    print("Launching browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close browser")