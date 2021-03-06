from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from utils.logger import log
from configs import UI_MAX_RESPONSE_TIME


class Waits:
    def __init__(self, driver):
        self.wait_element = WebDriverWait(
            driver,
            UI_MAX_RESPONSE_TIME,
            ignored_exceptions=WebDriverException
        )

    def until_elements_presence_by_xpath(self, element, message=None):
        """
        wait until web element/elements appears in DOM with delay of 0,5 second,
        in case if elements/element is present returns web element/elements else throws exception
        @param element: XPATH
        @param message: Assertion message
        @return: web element/elements
        """
        return self.wait_element.until(
            ec.presence_of_all_elements_located((By.XPATH, element)), message)

    def until_element_visible_by_id(self, element, message=None):
        """
        wait until web element/elements if visible with delay 0,5 second by default
        @param element: ID
        @param message: Assertion message
        @return: web element/elements else False
        """
        log.info(f"Looking for id: {element}")
        return self.wait_element.until(
            ec.visibility_of_element_located((By.ID, element)), message)

    def until_element_presence_by_xpath(self, element, message=None):
        """
        wait until web element appears in DOM with delay of 0,5 second,
        in case if element is present returns web element else throws exception
        @param element: XPATH
        @param message: Assertion message
        @return: web element
        """
        return self.wait_element.until(
            ec.presence_of_element_located((By.XPATH, element)), message)

    def until_element_visible_by_name(self, element, message=None):
        """
        wait until web element/elements if visible with delay 0,5 second by default
        @param element: NAME
        @param message: Assertion message
        @return: web element/elements else False
        """
        return self.wait_element.until(
            ec.visibility_of_element_located((By.NAME, element)), message)

    def until_element_visible_by_class_name(self, element, message=None):
        """
        wait until web element/elements if visible with delay 0,5 second by default
        @param element: CLASS_NAME
        @param message: Assertion message
        @return: web element/elements else False
        """
        log.info(f"Looking for class: {element}")
        return self.wait_element.until(
            ec.visibility_of_element_located((By.CLASS_NAME, element)), message)

    def until_element_visible_by_xpath(self, element, message=None):
        """
        wait until web element/elements is visible
        @param element: XPATH
        @param message: Assertion message
        @return: web element/elements else False
        """
        log.info(f"Looking for xpath: {element}")
        return self.wait_element.until(
            ec.visibility_of_element_located((By.XPATH, element)), message)

    def until_elements_visible_by_class_name(self, element, message=None):
        """
        wait until web element/elements appears in DOM with delay of 0,5 second,
        in case if elements/element is visible returns web element/elements else throws exception
        @param element: CLASS NAME
        @param message: Assertion message
        @return: web element/elements
        """
        return self.wait_element.until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, element)), message)

    def until_elements_visible_by_xpath(self, element, message=None):
        """
        wait until web element/elements appears in DOM with delay of 0,5 second,
        in case if elements/element is visible returns web element/elements else throws exception
        @param element: XPATH
        @param message: Assertion message
        @return: web element/elements
        """
        return self.wait_element.until(
            ec.visibility_of_any_elements_located((By.XPATH, element)), message)

    def until_element_not_visible_by_xpath(self, element, message=None):
        """
        wait until web element/elements is not visible
        @param element: XPATH
        @param message: Assertion message
        @return: web element/elements else False
        """
        log.info(f"Looking for xpath: {element}")
        return self.wait_element.until(
            ec.invisibility_of_element_located((By.XPATH, element)), message)
