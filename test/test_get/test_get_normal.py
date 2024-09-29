import pytest
import requests

from setting.endpoint import api_list_user


@pytest.fixture
def api_url():
    def _api_url(page):
        return api_list_user.format(page=page)
    return _api_url

def test_api_page_0(api_url):
    url = api_url(0)
    response = requests.get(url)
    assert response.status_code == 404 #expected 404 not found

def test_api_page_1(api_url):
    url = api_url(1)
    response = requests.get(url)
    assert response.status_code == 200

def test_api_page_2(api_url):
    url = api_url(2)
    response = requests.get(url)
    assert response.status_code == 200




