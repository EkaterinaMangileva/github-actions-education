import allure
import pytest
from qaseio.pytest import qase


@qase.title('Первый набор тестов')
@qase.description('Это фальшивые тесты')
class TestDemo:

    @allure.title("Успешный тест")
    @qase.fields(
        ("severity", "critical"),
        ("priority", "high"),
        ("layer", "unit"),
        ("description", "Try to login to Qase TestOps using login and password"),
        ("description", "*Precondition 1*. Markdown is supported."),
    )
    @allure.feature("Simple test")
    @allure.story("1111")
    @allure.suite("ПЕРВЫЙ")
    def test_one(self):
        with qase.step("Make assert"):
            assert 1 == 1

    @allure.title("Пропущенный тест")
    @pytest.mark.skip
    def test_skipped(self):
        with qase.step("Make assert"):
            assert 1 == 1

    @allure.title("Тест с ошибкой в коде")
    @qase.fields(
        ("severity", "critical"),
        ("priority", "high"),
        ("layer", "unit"),
        ("description", "Try to login to Qase TestOps using login and password"),
        ("description", "*Precondition 1*. Markdown is supported."),
    )
    @allure.feature("Simple test")
    @allure.story("2222222")
    @allure.suite("ВТОРОЙ")
    def test_failed(self):
        with qase.step("Make assert"):
            assert 1 == 2

    @allure.title("Тест с ошибкой в тесте")
    @qase.fields(
        ("severity", "critical"),
        ("priority", "high"),
        ("layer", "unit"),
        ("description", "Try to login to Qase TestOps using login and password"),
        ("description", "*Precondition 1*. Markdown is supported."),
    )
    @allure.feature("Simple test")
    @allure.story("1111")
    @allure.suite("ВТОРОЙ")
    def test_broken(self):
        with qase.step("Make assert"):
            assert 1 == 1
            raise Exception("Ошибка в тесте")
