import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Testdata.test_dataDriven import TestData


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="type1", help="my option: type1 or type2"
    )


@pytest.fixture(scope="class")
def setup(request):
    name = request.config.getoption("--browser")
    if name.lower == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif name.lower == "firefox":
        driver = webdriver.Firefox()
    elif name.lower == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(TestData.url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()



