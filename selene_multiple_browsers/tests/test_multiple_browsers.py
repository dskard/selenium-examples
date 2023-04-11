from selene.api import browser


class TestMultipleBrowsers:

    def test_switching_between_multiple_browsers_doesnt_close_either(self, launch_browser):

        # launch two web browsers
        driver_1 = launch_browser()
        driver_2 = launch_browser()

        # tell selene to navigate the first web browser to a website
        browser.config.driver = driver_1
        browser.open("http:/github.com")

        # tell selene to navigate the second web browser to a website
        browser.config.driver = driver_2
        browser.open("http://github.com")

        # tell selene to navigate the first web browser to another website
        browser.config.driver = driver_1
        browser.open("http://ddg.gg")

        # tell selene to navigate the second web browser to another website
        browser.config.driver = driver_2
        browser.open("http://ddg.gg")
