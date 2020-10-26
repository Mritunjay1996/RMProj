from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime
import dateutil.relativedelta
import os
import allure
import time

class school_myStudentsPage:
    license_student = (By.XPATH, "//td[@data-order='License Student']/a")
    button_upload_multiple = (By.XPATH, "//td[b[a[contains(text(),'Multiple Automation')]]]/following-sibling::td[2]/a")
    input_upload_file = (By.XPATH, "//input[@id='upload_file']")
    radio_fulfill_yes = (By.XPATH, "//input[@id='fulfill_yes']")
    checkboxes_multiple_requirement = (By.XPATH, "//td[input[contains(@value,'Multiple Automation')]]/preceding-sibling::td[1]/input")
    button_confirm = (By.XPATH, "//button[text()='CONFIRM']")
    status_multiple_requirements = (By.XPATH, "//td[b[a[contains(text(),'Multiple Automation')]]]/following-sibling::td[4]//img")
    success_image1 = (By.XPATH, "//table[@class='requirements table table-bordered table-striped dataTable no-footer']/tbody/tr/td[5]/a/img")
    upload_button = (By.XPATH, "//a[contains(text(),'UPLOAD')]")
    chkBoxes_btn = (By.XPATH, "//input[@name='fulfill_requirements[]']")
    cross_button = (By.XPATH, "//button[contains(text(),'×')]")
    input_date = (By.XPATH, "//div[@class='exp_datePicker input-append date']/input")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Click on searched student name')
    def click_student_name(self):
        self.browser.find_element(*self.license_student).click()

    @allure.step('Click on upload file button')
    def click_upload_multiple(self):
        self.browser.find_element(*self.button_upload_multiple).click()

    @allure.step('Click on upload file button')
    def click_upload_button(self):
        self.browser.find_element(*self.upload_button).click()

    @allure.step('Upload requirement file')
    def upload_file(self):
        # WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(self.input_upload_file))
        time.sleep(8)
        path = os.getcwd() + "\\resources\\sample1.pdf"
        self.browser.find_element(*self.input_upload_file).send_keys(path)

    @allure.step('CLick on cross icon')
    def click_crossIcon(self):
        self.browser.find_element(*self.cross_button).click()

    @allure.step('Select option to fulfill multiple requirement')
    def select_fulfill_yes(self):
        self.browser.find_element(*self.radio_fulfill_yes).click()

    @allure.step('Select checkboxes for multiple requirements')
    def check_multiple_req(self):
        checks = self.browser.find_elements(*self.checkboxes_multiple_requirement)
        for check in checks:
            check.click()

    @allure.step('Enter Expiration Dates for multiple requirements')
    def enter_expirationDate_multiple_req(self):
        now = datetime.now()  # current date and time
        next = now + dateutil.relativedelta.relativedelta(months=+1)
        future_date = next.strftime("%m/%d/%Y")
        checks = self.browser.find_elements(*self.input_date)
        for check in checks:
            check.send_keys(future_date)

    @allure.step('Click confirm button')
    def click_confirm(self):
        self.browser.find_element(*self.button_confirm).click()

    @allure.step('Verify successful completion for multiple requirements')
    def verify_completed_multiple_req(self):
        success = True
        statuses = self.browser.find_elements(*self.success_image1)
        for status in statuses:
            if 'green' not in str(status.get_attribute('src')):
                success = False
        return success