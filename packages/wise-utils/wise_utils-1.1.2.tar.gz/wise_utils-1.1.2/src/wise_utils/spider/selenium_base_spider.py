import os
import sys
import time
import string
import zipfile
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from wise_utils.spider.basespider import BaseSpider

from seleniumbase import Driver

class SeleniumBaseSpider(BaseSpider):
    PAGE_LOAD_TIMEOUT = 180

    def __init__(self, task_name, log_level=logging.DEBUG, log_file_path=None):
        super(SeleniumBaseSpider, self).__init__(task_name=task_name, log_level=log_level, log_file_path=log_file_path)
        self.__browser_model = "local"  # 默认为本地启动

    def create_local_browser(self,
                             headless: bool = True,
                             incognito: bool = True,
                             no_picture: bool = False,
                             proxy_string: str = "",  # Use proxy. Format: "SERVER:PORT" or "USER:PASS@SERVER:PORT".
                             userdata_file_path: str = "",
                             browser = None
                             ):

        if browser:
            try:
                print(browser.get_title())
                return browser
            except:
                pass

        browser = Driver(headless=headless,
                         incognito=incognito,
                         block_images=no_picture,
                         user_data_dir=userdata_file_path,
                         proxy=proxy_string,
                         uc=True)
        browser.maximize_window()
        return browser

    @staticmethod
    def get_browser_cookies(browser):
        """获取当前浏览器cookie，返回str"""
        cookie_dict = browser.get_cookies()
        cookies = ""
        for cookie in cookie_dict:
            if not cookie["name"].startswith("_"):
                cookies += cookie["name"] + "=" + cookie["value"] + ";"
        return cookies.strip(";")

    def clear_and_send_keys(self, browser, by: str, value: str, msg):
        """
        点击并发送
        每次都获取是因为有时旧的元素定位不到会报错，所以每次都重新获取元素并完成相应操作
        :param browser: 浏览器对象
        :param by: 通过什么方式定位，如： id，xpath，css_selector
        :param value: 定位的规则
        :param msg: 需要输入的值
        :return:
        """
        by = by.lower()
        self.__get_element(browser, by, value).clear()
        time.sleep(0.1)
        self.__get_element(browser, by, value).send_keys(msg)
        time.sleep(0.3)
        return True

    def find_element(self, browser, by, value):
        """获取元素"""
        return self.__get_element(browser, by, value)

    def find_element_by_xpath(self, browser, value: str):
        """通过xpath获取元素"""
        return self.__get_element(browser, "xpath", value)

    def find_element_by_id(self, browser, value: str):
        """通过id获取元素"""
        return self.__get_element(browser, "id", value)

    def find_elements(self, browser, by, value):
        """获取元素"""
        return self.__get_elements(browser, by, value)

    def find_elements_by_xpath(self, browser, value: str):
        """通过xpath获取元素"""
        return self.__get_elements(browser, "xpath", value)

    def find_elements_by_id(self, browser, value: str):
        """通过id获取元素"""
        return self.__get_elements(browser, "id", value)

    def wait_clickable_element(self, browser, by, value: str, wait=10):
        """等待可点击的元素"""
        if by == 'id':
            return self.wait_clickable_element_by_id(browser, value, wait)
        elif by == 'xpath':
            return self.wait_clickable_element_by_xpath(browser, value, wait)
        return None

    @staticmethod
    def wait_clickable_element_by_xpath(browser, value: str, wait=10):
        """等待可点击的元素"""
        return WebDriverWait(browser, wait, 0.5).until(EC.element_to_be_clickable((By.XPATH, value)))

    @staticmethod
    def wait_clickable_element_by_id(browser, value: str, wait=10):
        """等待可点击的元素"""
        return WebDriverWait(browser, wait, 0.5).until(EC.element_to_be_clickable((By.ID, value)))

    def wait_located_element(self, browser, by, value: str, wait=10):
        """等待元素"""
        if by == 'id':
            return self.wait_located_element_by_id(browser, value, wait)
        elif by == 'xpath':
            return self.wait_located_element_by_xpath(browser, value, wait)
        return None

    @staticmethod
    def wait_located_element_by_xpath(browser, value: str, wait=10):
        """等待元素"""
        return WebDriverWait(browser, wait, 0.5).until(EC.presence_of_element_located((By.XPATH, value)))

    @staticmethod
    def wait_located_element_by_id(browser, value: str, wait=10):
        """等待元素"""
        return WebDriverWait(browser, wait, 0.5).until(EC.presence_of_element_located((By.ID, value)))

    def wait_text_to_be_present(self, browser, by, value: str, text, wait=10):
        """等待元素"""
        if by == 'id':
            return self.wait_text_to_be_present_by_id(browser, value, text, wait)
        elif by == 'xpath':
            return self.wait_text_to_be_present_by_xpath(browser, value, text, wait)
        return None

    @staticmethod
    def wait_text_to_be_present_by_xpath(browser, value: str, text: str, wait=10):
        """等待文字"""
        return WebDriverWait(browser, wait, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, value), text_=text))

    @staticmethod
    def wait_text_to_be_present_by_id(browser, value: str, text: str, wait=10):
        """等待文字"""
        return WebDriverWait(browser, wait, 0.5).until(EC.text_to_be_present_in_element((By.ID, value), text_=text))

    def wait_ele_to_be_selected(self, browser, by, value: str, wait=10):
        """等待选择框"""
        if by == 'id':
            return self.wait_ele_to_be_selected_by_id(browser, value, wait)
        elif by == 'xpath':
            return self.wait_ele_to_be_selected_by_xpath(browser, value, wait)
        return None

    def wait_ele_to_be_selected_by_id(self, browser, value: str, wait=10):
        """等待选择框"""
        return Select(self.wait_clickable_element_by_id(browser, value, wait))

    def wait_ele_to_be_selected_by_xpath(self, browser, value: str, wait=10):
        """等待选择框"""
        return Select(self.wait_clickable_element_by_xpath(browser, value, wait))

    @staticmethod
    def wait_alert_element(browser, wait=10):
        """等待弹窗"""
        return WebDriverWait(browser, wait, 0.5).until(EC.alert_is_present())

    def click_by_js(self, browser, by, value):
        """通过js点击"""
        by = by.lower()
        ele = self.__get_element(browser, by, value)
        browser.execute_script("arguments[0].click();", ele)
        time.sleep(0.5)
        return True

    def __get_element(self, browser, by, value):
        """通过不同的方式查找界面元素"""
        element = None
        by = by.lower()
        if by == "id":
            element = browser.find_element(by=By.ID, value=value)
        elif by == "name":
            element = browser.find_element(by=By.NAME, value=value)
        elif by == "xpath":
            element = browser.find_element(by=By.XPATH, value=value)
        elif by == "classname":
            element = browser.find_element(by=By.CLASS_NAME, value=value)
        elif by == "css":
            element = browser.find_element(by=By.CSS_SELECTOR, value=value)
        elif by == "link_text":
            element = browser.find_element(by=By.LINK_TEXT, value=value)
        else:
            self.logger.error("无对应方法，请检查")
        return element

    def __get_elements(self, browser, by, value):
        """通过不同的方式查找所有界面元素"""
        elements = []
        by = by.lower()
        if by == "id":
            elements = browser.find_elements(by=By.ID, value=value)
        elif by == "name":
            elements = browser.find_elements(by=By.NAME, value=value)
        elif by == "xpath":
            elements = browser.find_elements(by=By.XPATH, value=value)
        elif by == "classname":
            elements = browser.find_elements(by=By.CLASS_NAME, value=value)
        elif by == "css":
            elements = browser.find_elements(by=By.CSS_SELECTOR, value=value)
        elif by == "link_text":
            elements = browser.find_elements(by=By.LINK_TEXT, value=value)
        else:
            self.logger.error("无对应方法，请检查")
        return elements

    def scroll_to_ele(self, browser, by, value):
        """滚动到某个元素的位置"""
        ele = self.__get_element(browser, by, value)
        js4 = "arguments[0].scrollIntoView();"
        browser.execute_script(js4, ele)
        return True

mytest_demo = SeleniumBaseSpider(task_name="demo", log_file_path="")

if __name__ == "__main__":
    browser = mytest_demo.create_local_browser(headless=False, proxy_string="127.0.0.1:42019")
    browser.open("https://www.baidu.com")
    mytest_demo.clear_and_send_keys(browser, "xpath", "//input[@id='kw']", "secret_sauce")
    browser.type("//input[@id='kw']", "secret_sauce")
    browser.quit()


#
# self.open(url)  # Navigate the browser window to the URL.
# self.type(selector, text)  # Update the field with the text.
# self.click(selector)  # Click the element with the selector.
# self.click_link(link_text)  # Click the link containing text.
# self.go_back()  # Navigate back to the previous URL.
# self.select_option_by_text(dropdown_selector, option)
# self.hover_and_click(hover_selector, click_selector)
# self.drag_and_drop(drag_selector, drop_selector)
# self.get_text(selector)  # Get the text from the element.
# self.get_current_url()  # Get the URL of the current page.
# self.get_page_source()  # Get the HTML of the current page.
# self.get_attribute(selector, attribute)  # Get element attribute.
# self.get_title()  # Get the title of the current page.
# self.switch_to_frame(frame)  # Switch into the iframe container.
# self.switch_to_default_content()  # Leave the iframe container.
# self.open_new_window()  # Open a new window in the same browser.
# self.switch_to_window(window)  # Switch to the browser window.
# self.switch_to_default_window()  # Switch to the original window.
# self.get_new_driver(OPTIONS)  # Open a new driver with OPTIONS.
# self.switch_to_driver(driver)  # Switch to the browser driver.
# self.switch_to_default_driver()  # Switch to the original driver.
# self.wait_for_element(selector)  # Wait until element is visible.
# self.is_element_visible(selector)  # Return element visibility.
# self.is_text_visible(text, selector)  # Return text visibility.
# self.sleep(seconds)  # Do nothing for the given amount of time.
# self.save_screenshot(name)  # Save a screenshot in .png format.
# self.assert_element(selector)  # Verify the element is visible.
# self.assert_text(text, selector)  # Verify text in the element.
# self.assert_exact_text(text, selector)  # Verify text is exact.
# self.assert_title(title)  # Verify the title of the web page.
# self.assert_downloaded_file(file)  # Verify file was downloaded.
# self.assert_no_404_errors()  # Verify there are no broken links.
# self.assert_no_js_errors()  # Verify there are no JS errors.