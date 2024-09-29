from setting.endpoint import api_hitung_jarak
from setting.resources import file_path
import json
import requests
from assertpy import assert_that
from jsonschema import validate

def test_positive_case_input():
    value_from = "CGK"
    value_to = "NRT"

    body_object = {
        "from": value_from,
        "to": value_to
    }

    with open(file_path, 'r') as schema_file:
        schema = json.load(schema_file)

    response = requests.post(
        api_hitung_jarak,
        headers={"Content-Type": "application/json"},
        data=json.dumps(body_object)
    )

    assert_that(response.status_code).is_equal_to(200)
    response_json = response.json()
    assert_that(response_json['data']['attributes']['from_airport']['iata']).is_equal_to(value_from)
    validate(instance=response_json, schema=schema)

def test_negative_case_input():
    value_from = "1234??"
    value_to = "NRT"

    body_object = {
        "from": value_from,
        "to": value_to
    }

    response = requests.post(
        api_hitung_jarak,
        headers={"Content-Type": "application/json"},
        data=json.dumps(body_object)
    )

    assert_that(response.status_code).is_equal_to(422) #expected return 422 for invalid input
    response_json = response.json()
    # Check if the error message is as expected
    (assert_that(response_json['errors'][0]['detail']).contains
     ("Please enter valid 'from' and 'to' airports."))

