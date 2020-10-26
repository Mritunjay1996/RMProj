import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure

class adminCRMObj:
    tab_CRM = (By.XPATH, "//a[contains(text(),'CRMs')]")
    CRM_create_option = (By.XPATH, "//a[contains(text(),'CRMs')]/following-sibling::ul[1]//a[text()='Create']")
    input_firstname = (By.XPATH, "//input[@id='first_name']")
    input_lastname = (By.XPATH, "//input[@id='last_name']")
    input_schoolname = (By.XPATH, "//input[@id='new_school']")
    input_campusname = (By.XPATH, "//input[@id='new_campus']")
    input_disciplinename = (By.XPATH, "//input[@id='new_discipline']")
    input_phone = (By.XPATH, "//input[@id='phone']")
    input_email = (By.XPATH, "//input[@id='email']")
    input_password = (By.XPATH, "//input[@id='password']")
    input_confirm_password = (By.XPATH, "//input[@id='confirm_password']")
    button_submit = (By.XPATH, "//button[text()='SUBMIT']")
    success_message = (By.XPATH, "//div[@id='error']")
    success_email = (By.XPATH, "//div[@class='span10']/h3/a")
    select_school = (By.XPATH, "//select[@id='school']")
    select_campus = (By.XPATH, "//select[@id='campus']")
    select_discipline = (By.XPATH, "//select[@id='discipline']")
    select_shadowing = (By.XPATH, "//select[@id='crm_shadow']")
    select_ccemail = (By.XPATH, "//select[@id='cc']")
    log_out = (By.XPATH, "//a[contains(text(),'Logout')]")
    button_save = (By.XPATH, "//button[@id='submit']")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Verifying the cc email option for CRM creation')
    def verify_crm_creation_ccemail(self):
        select = Select(self.browser.find_element(*self.select_ccemail))
        msg = select.first_selected_option
        msg = msg.text
        return msg.strip()

    @allure.step('Verifying the shadowing option for CRM creation')
    def verify_crm_creation_shadowing(self):
        select = Select(self.browser.find_element(*self.select_shadowing))
        msg = select.first_selected_option
        msg = msg.text
        return msg.strip()

    @allure.step('Verifying the email for CRM creation')
    def verify_crm_creation_email(self):
        msg = self.browser.find_element(*self.input_email).get_attribute("value")
        return msg.strip()

    @allure.step('Verifying the phone number for CRM creation')
    def verify_crm_creation_phone(self):
        msg = self.browser.find_element(*self.input_phone).get_attribute("value")
        return msg.strip().replace('(', '').replace(')', '').replace('-', '').replace(' ', '').replace('x', '')

    @allure.step('Verifying the discipline name for CRM creation')
    def verify_crm_creation_discipline(self):
        select = Select(self.browser.find_element(*self.select_discipline))
        msg = select.first_selected_option
        msg = msg.text
        return msg.strip()

    @allure.step('Verifying the campus name for CRM creation')
    def verify_crm_creation_campus(self):
        select = Select(self.browser.find_element(*self.select_campus))
        msg = select.first_selected_option
        msg = msg.text
        return msg.strip()

    @allure.step('Verifying the school name for CRM creation')
    def verify_crm_creation_school(self):
        select = Select(self.browser.find_element(*self.select_school))
        msg = select.first_selected_option
        msg = msg.text
        return msg.strip()

    @allure.step('Verifying the last name for CRM creation')
    def verify_crm_creation_lastname(self):
        msg = self.browser.find_element(*self.input_lastname).get_attribute("value")
        return msg.strip()

    @allure.step('Verifying the first name for CRM creation')
    def verify_crm_creation_firstname(self):
        msg = self.browser.find_element(*self.input_firstname).get_attribute("value")
        return msg.strip()

    @allure.step('Verifying the login email for CRM creation')
    def verify_crm_creation_email(self):
        msg = self.browser.find_element(*self.success_email).text
        return msg.strip()

    @allure.step('Verifying the success message for CRM creation')
    def verify_crm_creation_message(self):
        msg = self.browser.find_element(*self.success_message).text
        return msg.strip()

    @allure.step('Click Submit button')
    def click_submit(self):
        self.browser.find_element(*self.button_submit).click()

    @allure.step('Click Save button')
    def click_save(self):
        self.browser.find_element(*self.button_save).click()

    @allure.step('Enter password for CRM')
    def enter_password_crm(self, password):
        self.browser.find_element(*self.input_password).send_keys(password)
        self.browser.find_element(*self.input_confirm_password).send_keys(password)

    @allure.step('Enter email for CRM')
    def enter_email_crm(self, email):
        self.browser.find_element(*self.input_email).click()
        self.browser.find_element(*self.input_email).clear()
        self.browser.find_element(*self.input_email).send_keys(email)

    @allure.step('Enter phone number for CRM')
    def enter_phone_crm(self, phone):
        time.sleep(2)
        self.browser.find_element(*self.input_phone).click()
        self.browser.find_element(*self.input_phone).send_keys(phone)

    @allure.step('Enter new discipline name for CRM')
    def enter_disciplinename_crm(self, disciplinename):
        self.browser.find_element(*self.input_disciplinename).send_keys(disciplinename)

    @allure.step('Enter new campus name for CRM')
    def enter_campusname_crm(self, campusname):
        self.browser.find_element(*self.input_campusname).send_keys(campusname)

    @allure.step('Enter new school name for CRM')
    def enter_schoolname_crm(self, schoolname):
        self.browser.find_element(*self.input_schoolname).send_keys(schoolname)

    @allure.step('Enter last name for CRM')
    def enter_lastname_crm(self, lastname):
        self.browser.find_element(*self.input_lastname).send_keys(lastname)

    @allure.step('Enter first name for CRM')
    def enter_firstname_crm(self, firstname):
        self.browser.find_element(*self.input_firstname).send_keys(firstname)

    @allure.step('Clicking option CRMs -> Create')
    def click_crm_create(self):
        self.browser.find_element(*self.CRM_create_option).click()

    @allure.step('Clicking tab - CRMs')
    def click_tab_crm(self):
        self.browser.find_element(*self.tab_CRM).click()

    @allure.step('click logout button ')
    def click_logout_button(self):
        self.browser.find_element(*self.log_out).click()