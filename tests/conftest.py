import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    capabilities = {
        "browserName": "chrome",
        "version": "latest",
        "enableVNC": True,
        "enableVideo": True
    }
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities
    )
    yield driver
    driver.quit()
