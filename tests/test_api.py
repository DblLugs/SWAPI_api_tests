import pytest
import allure


@allure.title("Запрос всех доступных ресурсов")
@pytest.mark.xfail(reason="Как пример падающего теста", strict=True)
def test_get_all_resources(session, base_url):
    response = session.get(url=f'{base_url}')
    assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    assert len(response.json()) == 7, "Количество ресурсов != 7"


@allure.title("Запрос существующего в базе фильма")
@pytest.mark.parametrize("number", [1, 6])
def test_get_real_film(session, base_url, number):
    response = session.get(url=f"{base_url}/films/{number}")
    assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    assert response.json()["url"] == f"{base_url}/films/{number}/", "Неверный url"


@allure.title("Запрос персонажа Luke Skywalker")
@pytest.mark.skip(reason="Как пример пропуска теста")
def test_get_people(session, base_url):
    response = session.get(url=f"{base_url}/people/1")
    assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    assert response.json()["name"] == "Luke Skywalker", f'Неверный персонаж, получен {response.json()["name"]}'


@allure.title("Запрос несуществующего в базе фильма")
@pytest.mark.parametrize("number", [-1, 0, 7])
def test_get_no_real_film(session, base_url, number):
    response = session.get(url=f"{base_url}/films/{number}")
    assert response.status_code == 404, f"Неверный код ответа, получен {response.status_code}"
