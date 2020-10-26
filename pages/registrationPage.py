"""
This module contains the page object
for the registration page.
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import allure

class registrationPage:
    """
    Define all web element locators and test steps
    in this class for registration page
    """
    first_name = (By.XPATH, "//input[@id='first_name']")
    last_name = (By.XPATH, "//input[@id='last_name']")
    select_school = (By.XPATH, "//select[@id='combo']")
    select_cohort = (By.XPATH, "//select[@id='cohorts']")
    backdrop = (By.XPATH, "//div[contains(@class, 'modal-backdrop fade')]")
    calendar_icon = (By.XPATH, "//i[@class='icon-calendar']")
    calendar_next = (By.XPATH, "//div[@class='datepicker-months']//th[@class='next']")
    calendar_monthApr = (By.XPATH, "//span[@class='month' and text()='Apr']")
    address1 = (By.XPATH, "//input[@id='c_address_1']")
    address2 = (By.XPATH, "//input[@id='c_address_2']")
    select_state = (By.XPATH, "//select[@id='c_state']")
    select_city = (By.XPATH, "//select[@id='c_city']")
    zipcode = (By.XPATH, "//input[@id='c_zip']")
    phone = (By.XPATH, "//input[@id='uphone']")
    email = (By.XPATH, "//input[@id='email']")
    confirm_email = (By.XPATH, "//input[@id='email_confirm']")
    password = (By.XPATH, "//input[@id='password']")
    password_confirm = (By.XPATH, "//input[@id='password_confirm']")
    agreement_checkbox = (By.XPATH, "//input[@id='agreement_checkbox']")
    submit_button = (By.XPATH, "//input[@id='submit_button']")
    alert_title = (By.XPATH, "//div[@id='alert_modal']//h4[1]")
    alert_button_ok = (By.XPATH, "//div[@id='alert_modal']//button[text()='OK']")
    modal_fade = (By.XPATH, "//div[contains(@class, 'hide active fade in modal')]")
    modal_backdrop = (By.XPATH, "//div[contains(@class, 'modal-backdrop')]")
    creditcard_number = (By.XPATH, "//input[@id='card-number']")
    creditcard_expyr = (By.XPATH, "//select[@id='exp-year']")
    creditcard_ccv = (By.XPATH, "//input[@id='ccv']")
    creditcard_same_address = (By.XPATH, "//input[@id='same_mailing_address']")
    select_student_type = (By.XPATH, "//select[@id='student_type']")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Selecting the type of user for registration')
    def select_studentType(self, type):
        select = Select(self.browser.find_element(*self.select_student_type))
        select.select_by_visible_text(type)

    @allure.step('Enter the first name')
    def enter_firstName(self, firstName):
        self.browser.find_element(*self.first_name).send_keys(firstName)

    @allure.step('Enter the last name')
    def enter_lastName(self, lastName):
        self.browser.find_element(*self.last_name).send_keys(lastName)

    @allure.step('Select school')
    def selectSchoolCampusDiscipline(self, selectItem):
        select = Select(self.browser.find_element(*self.select_school))
        select.select_by_visible_text(selectItem)
        # WebDriverWait(self.browser, 10).until(
        #     EC.invisibility_of_element_located(self.backdrop))
        time.sleep(5)

    @allure.step('Select Cohort')
    def selectCohort(self, selectItem):
        select = Select(self.browser.find_element(*self.select_cohort))
        select.select_by_visible_text(selectItem)

    @allure.step('Enter graduation date')
    def enter_graduationDate(self):
        # WebDriverWait(self.browser, 10).until(
        #     EC.invisibility_of_element_located(self.modal_backdrop))
        self.browser.find_element(*self.calendar_icon).click()
        self.browser.find_element(*self.calendar_next).click()
        self.browser.find_element(*self.calendar_next).click()
        self.browser.find_element(*self.calendar_monthApr).click()

    @allure.step('Enter mailing address')
    def enter_address(self, address1, address2, state, city, zip):
        self.browser.find_element(*self.address1).send_keys(address1)
        self.browser.find_element(*self.address2).send_keys(address2)
        Select(self.browser.find_element(*self.select_state)).select_by_visible_text(state)
        Select(self.browser.find_element(*self.select_city)).select_by_visible_text(city)
        self.browser.find_element(*self.zipcode).click()
        self.browser.find_element(*self.zipcode).send_keys(zip)

    @allure.step('Enter phone number')
    def enter_phoneNumber(self, phone):
        self.browser.find_element(*self.phone).click()
        self.browser.find_element(*self.phone).send_keys(phone)

    @allure.step('Enter email address')
    def enter_email(self, email):
        self.browser.find_element(*self.email).send_keys(email)
        self.browser.find_element(*self.confirm_email).send_keys(email)

    @allure.step('Enter and confirm password')
    def enter_password(self, password):
        self.browser.find_element(*self.password).send_keys(password)
        self.browser.find_element(*self.password_confirm).send_keys(password)

    @allure.step('Enter credit card number')
    def enter_creditcard_number(self, cardnum):
        self.browser.find_element(*self.creditcard_number).send_keys(cardnum)

    @allure.step('Enter credit card expiry year')
    def enter_creditcard_expyr(self, expyr):
        select = Select(self.browser.find_element(*self.creditcard_expyr))
        select.select_by_visible_text(expyr)

    @allure.step('Enter credit card ccv')
    def enter_creditcard_ccv(self, ccv):
        self.browser.find_element(*self.creditcard_ccv).send_keys(ccv)

    @allure.step('Select checkbox for same mailing address')
    def select_checkbox_sameaddress(self):
        self.browser.find_element(*self.creditcard_same_address).click()

    @allure.step('Check license agreement')
    def select_agreementCheckbox(self):
        self.browser.find_element(*self.agreement_checkbox).click()

    @allure.step('Click Submit button')
    def click_submitButton(self):
        self.browser.find_element(*self.submit_button).click()

    @allure.step('Validate successful registration')
    def validate_successfulRegistration(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(self.alert_button_ok))
            title = self.browser.find_element(*self.alert_title).text
            time.sleep(5)
            self.browser.find_element(*self.alert_button_ok).send_keys(Keys.ENTER)
            if title.strip() == "Success":
                return True
            else:
                return False
        except TimeoutException:
            return False