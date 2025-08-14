import pytest


@pytest.fixture(scope="session")
def preSetUpWork():
    print("Browser Instance Setup")