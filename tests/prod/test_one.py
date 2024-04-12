import allure
import pytest



class TestDemo:

    @allure.title("Успешный тест")
    @allure.feature("Simple test")
    @allure.story("1111")
    @allure.suite("ПЕРВЫЙ")
    def test_one(self):
       assert 1 == 1

    @allure.title("Пропущенный тест")
    @pytest.mark.skip
    def test_skipped(self):
        assert 1 == 1

    @allure.title("Тест с ошибкой в коде")
    @allure.feature("Simple test")
    @allure.story("2222222")
    @allure.suite("ВТОРОЙ")
    def test_failed(self):
       assert 1 == 2

    @allure.title("Тест с ошибкой в тесте")
    @allure.feature("Simple test")
    @allure.story("1111")
    @allure.suite("ВТОРОЙ")
    def test_broken(self):
        assert 1 == 1
        raise Exception("Ошибка в тесте")
