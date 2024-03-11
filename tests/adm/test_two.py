import allure
import pytest


@allure.feature("Don't simple test")
@allure.story("existsnce")
@allure.suite("test_one")
class TestDemo:

    @allure.title("Успешный тест")
    def test_one(self):
        assert 1 == 1

    @allure.title("Пропущенный тест")
    @pytest.mark.skip
    def test_skipped(self):
        assert 1 == 1

    @allure.title("Тест с ошибкой в коде")
    def test_failed(self):
        assert 1 == 2

    @allure.title("Тест с ошибкой в тесте")
    def test_broken(self):
        assert 1 == 1
        raise Exception("Ошибка в тесте")
