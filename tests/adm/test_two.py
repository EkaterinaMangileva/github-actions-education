import allure
import pytest
from qaseio.pytest import qase


@qase.title('Второй набор тестов')
@qase.description('Это фальшивые тесты')
class TestDemo2:

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
    @allure.suite("ТРЕТИЙ")
    def test_one(self):
        assert 1 == 1

    @allure.title("Пропущенный тест")
    @pytest.mark.skip
    def test_skipped(self):
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
    @allure.story("4444")
    @allure.suite("ЧЕТВЕРТЫЙ")
    def test_failed(self):
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
    @allure.suite("ПЯТЫЙ")
    def test_broken(self):
        assert 1 == 1
        raise Exception("Ошибка в тесте")
