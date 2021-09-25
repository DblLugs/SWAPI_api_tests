import json
import jsonschema
import allure
import os


def assert_valid_schema(data, schema_file):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(current_dir, schema_file)) as file:
        schema = json.load(file)
    return jsonschema.validate(instance=data, schema=schema)


@allure.title("Валидация jsonschema ресурса planets")
def test_valid_schema_planets(session, base_url):
    response = session.get(url=f"{base_url}/planets/1")
    assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    assert_valid_schema(response.json(), "../schemas/planets_schema.json")


@allure.title("Валидация jsonschema ресурса starships")
def test_valid_schema_starships(session, base_url):
    response = session.get(url=f"{base_url}/starships/10")
    assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    assert_valid_schema(response.json(), "../schemas/starships_schema.json")


