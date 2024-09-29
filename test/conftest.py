import json
import pytest

@pytest.fixture(scope='function', autouse='true')
def hook(request):
    #BEFORE TEST
    print("===== before test =====")

    yield

    #AFTER TEST
    print("===== After Test =====")

@pytest.fixture(scope='session', autouse='true')
def suite(request):
    # BEFORE SUITE
    print("***** BEFORE ALL *****")

    yield

    # AFTER SUITE
    print("***** AFTER ALL *****")