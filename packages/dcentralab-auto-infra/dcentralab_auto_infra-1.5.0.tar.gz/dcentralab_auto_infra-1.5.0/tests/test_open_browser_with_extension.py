import pytest

from src.dcentralab_auto_infra.utilities.allure_utils import AllureUtils

AllureUtils.setup_allure_logging()


@pytest.mark.usefixtures("allure_logger", "init_browser", "init_wallet_actions_and_import_wallet_manager")
class TestOpenBrowserWithExtension:
    # @pytest.mark.parametrize(argnames="url",
    #                          argvalues=["https://staging.tokensfarm.com", "https://preprod.chainport.io",
    #                                     "https://staging-app.hord.fi"])
    @pytest.mark.parametrize(argnames="url",
                             argvalues=["https://staging-app.hord.fi"])
    def test_open_browser_with_extension(self, url):
        self.driver.get(url)

        AllureUtils.allure_screenshot(driver=self.driver, message=f"Page with URL {url} is loading")



class TestWatever:

    def test_whatever(self):
        dcentralab_auto_infra.