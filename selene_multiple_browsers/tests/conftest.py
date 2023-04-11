import os
import pytest

from selene.api import browser
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

# set the default selene reports folder
# to the present working directory
browser.config.reports_folder = os.getcwd()

# tell selene not to close the web browser,
# let our launch_browser fixture or pytest-selenium
# close the web browser
browser.config.hold_driver_at_exit = True


@pytest.fixture
def launch_browser(request, driver_class, driver_kwargs):
    """Returns a function that can be used to launch a web browser

    Web browser is managed by this fixture. It will be closed when
    this fixture has completed, after the the test case completes.
    """

    def create_driver():
        """Create a driver and return it to the caller
        """

        # driver_class comes from pytest-selenium plugin
        driver = driver_class(**driver_kwargs)

        event_listener = request.config.getoption("event_listener")
        if event_listener is not None:
            # Import the specified event listener and wrap the driver instance
            mod_name, class_name = event_listener.rsplit(".", 1)
            mod = __import__(mod_name, fromlist=[class_name])
            event_listener = getattr(mod, class_name)
            if not isinstance(driver, EventFiringWebDriver):
                driver = EventFiringWebDriver(driver, event_listener())

        request.node._driver = driver

        driver.maximize_window()

        # add a finalizer to close the driver after the test case completes
        request.addfinalizer(driver.quit)

        # return the Selenium driver object to the caller
        return driver

    return create_driver
