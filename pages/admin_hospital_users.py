import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure

class adminHospitalUsersObj:
    tab_HospitalUsers = (By.XPATH, "//a[text()='Hospital']")
    hospitalUsers_create_option = (By.XPATH, "//a[text()='Hospital']/following-sibling::ul[1]//a[text()='Create Hospital User']")
    select_hospital = (By.XPATH, "//select[@id='hospital']")
    input_firstname = (By.XPATH, "//input[@id='first_name']")
    input_lastname = (By.XPATH, "//input[@id='last_name']")
    input_phone = (By.XPATH, "//input[@id='phone']")
    input_email = (By.XPATH, "//input[@id='email']")
    input_confirm_email = (By.XPATH, "//input[@id='email_confirm']")
    radio_receiveEmail_no = (By.XPATH, "//input[@id='receive_emails_no']")
    radio_cancelRotations_yes = (By.XPATH, "//input[@id='cancel_rotations_yes']")
    radio_editRotations_no = (By.XPATH, "//input[@id='edit_rotations_no']")
    input_password = (By.XPATH, "//input[@id='password']")
    input_confirm_password = (By.XPATH, "//input[@id='confirm_password']")
    button_submit = (By.XPATH, "//button[@id='submit']")
    label_login_username = (By.XPATH, "//h3[contains(text(),'Login: ')]/a")
    input_hospital = (By.XPATH, "//input[@id='hospital']")
    button_add_discipline = (By.XPATH, "//div[@class='row-fluid'][2]//a[@class='add']/img")
    button_add_school = (By.XPATH, "//div[@class='row-fluid'][4]//a[@class='add']/img")
    button_save_changes = (By.XPATH, "//button[text()='SAVE CHANGES']")
    label_managed_discipline = (By.XPATH, "//tr[@id='h_disciplines_id']//td[@id='managed']/p[1]")
    label_managed_school = (By.XPATH, "//tr[@id='discipline_id']//td[@id='managed']/p")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Verifying the managed school-campus-discipline by hosptial user')
    def verify_managed_school(self):
        return self.browser.find_element(*self.label_managed_school).text

    @allure.step('Verifying the managed hospital-discipline by hosptial user')
    def verify_managed_discipline(self):
        return self.browser.find_element(*self.label_managed_discipline).text

    @allure.step('Click Save Changes button')
    def click_save_changes(self):
        self.browser.find_element(*self.button_save_changes).click()

    @allure.step('Adding the school-campus-discipline to the hospital user')
    def add_school(self, school):
        sch = (By.XPATH, "//td[@id='available']/p[text()='" + school + "']")
        self.browser.find_element(*sch).click()
        self.browser.find_element(*self.button_add_school).click()

    @allure.step('Adding the hospital-discipline to the hospital user')
    def add_discipline(self, discipline):
        disc = (By.XPATH, "//td[@id='available']/p[text()='" + discipline + "']")
        self.browser.find_element(*disc).click()
        self.browser.find_element(*self.button_add_discipline).click()

    @allure.step('Verifying the radio button selected as NO for Edit Rotations')
    def verify_editRotations_no(self):
        return self.browser.find_element(*self.radio_editRotations_no).is_selected()

    @allure.step('Verifying the radio button selected as NO for Cancel Rotations')
    def verify_cancelRotations_yes(self):
        return self.browser.find_element(*self.radio_cancelRotations_yes).is_selected()

    @allure.step('Verifying the radio button selected as NO for Receive Emails')
    def verify_receiveEmails_no(self):
        return self.browser.find_element(*self.radio_receiveEmail_no).is_selected()

    @allure.step('Verifying the email')
    def verify_email(self):
        return self.browser.find_element(*self.input_email).get_attribute("value")

    @allure.step('Verifying the phone nuber')
    def verify_phone(self):
        phone =  self.browser.find_element(*self.input_phone).get_attribute("value")
        return phone.strip().replace('(', '').replace(')', '').replace('-', '').replace(' ', '').replace('x', '')

    @allure.step('Verifying the last name')
    def verify_lastname(self):
        return self.browser.find_element(*self.input_lastname).get_attribute("value")

    @allure.step('Verifying the first name')
    def verify_firstname(self):
        return self.browser.find_element(*self.input_firstname).get_attribute("value")

    @allure.step('Verifying the associated hospital name')
    def verify_hospital_name(self):
        return self.browser.find_element(*self.input_hospital).get_attribute("value")

    @allure.step('Verifying the login username')
    def verify_login_username(self):
        return self.browser.find_element(*self.label_login_username).text

    @allure.step('Click Submit button')
    def click_submit(self):
        self.browser.find_element(*self.button_submit).click()

    @allure.step('Entering the password and confirm password')
    def enter_password(self, password):
        self.browser.find_element(*self.input_password).send_keys(password)
        self.browser.find_element(*self.input_confirm_password).send_keys(password)

    @allure.step('Selecting NO for Edit Rotations')
    def select_editRotations_no(self):
        self.browser.find_element(*self.radio_editRotations_no).click()

    @allure.step('Selecting NO for Cancel Rotations')
    def select_cancelRotations_yes(self):
        self.browser.find_element(*self.radio_cancelRotations_yes).click()

    @allure.step('Selecting NO for Receive Emails')
    def select_receiveEmail_no(self):
        self.browser.find_element(*self.radio_receiveEmail_no).click()

    @allure.step('Entering the email and confirm email')
    def enter_email(self, email):
        self.browser.find_element(*self.input_email).send_keys(email)
        self.browser.find_element(*self.input_confirm_email).send_keys(email)

    @allure.step('Entering the phone number')
    def enter_phone(self, phone):
        time.sleep(2)
        self.browser.find_element(*self.input_phone).click()
        self.browser.find_element(*self.input_phone).send_keys(phone)

    @allure.step('Entering the last name')
    def enter_lastname(self, lname):
        self.browser.find_element(*self.input_lastname).send_keys(lname)

    @allure.step('Entering the first name')
    def enter_firstname(self, fname):
        self.browser.find_element(*self.input_firstname).send_keys(fname)

    @allure.step('Selecting the hospital')
    def hospital_select(self, hospital):
        select = Select(self.browser.find_element(*self.select_hospital))
        select.select_by_visible_text(hospital)

    @allure.step('Clicking option Hospital Users -> Create')
    def click_hospitalUsers_create(self):
        self.browser.find_element(*self.hospitalUsers_create_option).click()

    @allure.step('Clicking tab - Hospital Users')
    def click_tab_hospitalUsers(self):
        self.browser.find_element(*self.tab_HospitalUsers).click()