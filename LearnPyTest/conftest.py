import pytest as pt

@pt.fixture(scope="session", autouse=True)
def tc_setup(browser):
    if browser == "chrome":
        print("Launching chrome")
    elif browser == "ff":
        print("Launching firefox")
    else:
        print("Please provide a valid browser")
    print("Launching browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close browser")

def pytest_addoption(parser):
    print("Adding options...")
    parser.addoption("--browser")


@pt.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")