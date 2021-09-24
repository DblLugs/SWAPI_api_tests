import pytest
import requests


def pytest_addoption(parser):
    parser.addoption('--url', default='https://swapi.dev/api')

@pytest.fixture(scope='module')
def base_url(request):
    return request.config.getoption('--url')

@pytest.fixture(scope='module')
def session():
    return requests.Session()



