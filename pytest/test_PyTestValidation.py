import pytest


@pytest.fixture(scope="module")
def preWork():
    print("Browser Instance Setup Module")
    return "pass"

@pytest.fixture(scope="function")
def secondWork():
    print("I setup secondWork instance")
    yield
    print("tear down validation")

@pytest.mark.smoke
def test_initialCheck(preWork, secondWork):
    print("this is first test")
    assert preWork == "pass"

@pytest.mark.skip
def test_secondCheck(preSetUpWork, secondWork):
    print("this is second test")
