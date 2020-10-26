"""
This module contains the page object
for the My Account page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import allure
import requests
import re
import time

class myAccountPage:

    #edit_email_button = (By.XPATH, "//span[@id='editEmail']")
    edit_email_textbox = (By.XPATH, "//td[b[text()='Username / Email']]/following-sibling::td[1]/input")
    #save_email_button = (By.XPATH, "//span[@id='saveEmail']")
    #edit_phone_button = (By.XPATH, "//span[@id='editPhone']")
    edit_phone_textbox = (By.XPATH, "//input[@id='phone']")
    #save_phone_button = (By.XPATH, "//span[@id='savePhone']")
    #edit_address1_button = (By.XPATH, "//span[@id='editAddress_1']")
    edit_address1_textbox = (By.XPATH, "//td[b[text()='Address']]/following-sibling::td[1]/input")
    #save_address1_button = (By.XPATH, "//span[@id='saveAddress_1']")
    #edit_address2_button = (By.XPATH, "//span[@id='editAddress_2']")
    edit_address2_textbox = (By.XPATH, "//td[b[text()='Address2']]/following-sibling::td[1]/input")
    #save_address2_button = (By.XPATH, "//span[@id='saveAddress_2']")
    select_state = (By.XPATH, "//select[@id='state']")
    #save_state_button = (By.XPATH, "//span[@id='saveState']")
    select_city = (By.XPATH, "//select[@id='city']")
    #save_city_button = (By.XPATH, "//span[@id='saveCity']")
    #edit_zip_button = (By.XPATH, "//span[@id='editZip']")
    edit_zip_textbox = (By.XPATH, "//td[b[text()='Zip Code']]/following-sibling::td[1]/input")
    #save_zip_button = (By.XPATH, "//span[@id='saveZip']")
    #user_email = (By.XPATH, "//span[@id='editEmail']/preceding-sibling::span[1]")
    user_email =(By.XPATH, "//tr[1]//td[2]//input[1]")
    user_phone = (By.XPATH, "//input[@id='phone']")
    user_address1 = (By.XPATH, "//tr[8]//td[2]//input[1]")
    user_address2 = (By.XPATH, "//tr[9]//td[2]//input[1]")
    user_zip = (By.XPATH, "//tr[12]//td[2]//input[1]")
    change_password_button = (By.XPATH, "//span[@id='resetPassword']")
    current_password = (By.XPATH, "//input[@name='current_password']")
    new_password = (By.XPATH, "//input[@name='new_password']")
    confirm_new_password = (By.XPATH, "//input[@name='confirm_new_password']")
    submit_password_button = (By.XPATH, "//button[text()='Submit']")
    alert_message = (By.XPATH, "//div[contains(@class,'clearfix alert')]")

    save_account = (By.XPATH, "//span[contains(text(),'Save')]")
    page_source = ""


    def __init__(self, browser):
        self.browser = browser

    def get_page_source(self):
        global page_source
        page_source = self.browser.page_source

    @allure.step("Edit user's email")
    def edit_email(self, newEmail):
        #self.browser.find_element(*self.edit_email_button).click()
        self.browser.find_element(*self.edit_email_textbox).clear()
        self.browser.find_element(*self.edit_email_textbox).send_keys(newEmail)
        #self.browser.find_element(*self.save_email_button).click()

    @allure.step("Edit user's phone")
    def edit_phone(self, newPhone):
        #self.browser.find_element(*self.edit_phone_button).click()
        self.browser.find_element(*self.edit_phone_textbox).clear()
        self.browser.find_element(*self.edit_phone_textbox).click()
        self.browser.find_element(*self.edit_phone_textbox).send_keys(Keys.CONTROL+ "A")
        self.browser.find_element(*self.edit_phone_textbox).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.edit_phone_textbox).send_keys(newPhone)
        #self.browser.find_element(*self.save_phone_button).click()

    @allure.step("Edit user's address 1")
    def edit_address1(self, newAddress1):
        #self.browser.find_element(*self.edit_address1_button).click()
        self.browser.find_element(*self.edit_address1_textbox).clear()
        self.browser.find_element(*self.edit_address1_textbox).send_keys(newAddress1)
        #self.browser.find_element(*self.save_address1_button).click()

    @allure.step("Edit user's address 2")
    def edit_address2(self, newAddress2):
        #self.browser.find_element(*self.edit_address2_button).click()
        self.browser.find_element(*self.edit_address2_textbox).clear()
        self.browser.find_element(*self.edit_address2_textbox).send_keys(newAddress2)
        #self.browser.find_element(*self.save_address2_button).click()

    @allure.step("Edit user's state")
    def edit_state(self, newState):
        select = Select(self.browser.find_element(*self.select_state))
        select.select_by_visible_text(newState)
        #self.browser.find_element(*self.save_state_button).click()

    @allure.step("Edit user's city")
    def edit_city(self, newCity):
        select = Select(self.browser.find_element(*self.select_city))
        select.select_by_visible_text(newCity)
        #self.browser.find_element(*self.save_city_button).click()

    @allure.step("Edit user's zip code")
    def edit_zip(self, newZip):
        #self.browser.find_element(*self.edit_zip_button).click()
        self.browser.find_element(*self.edit_zip_textbox).clear()
        self.browser.find_element(*self.edit_zip_textbox).click()
        self.browser.find_element(*self.edit_zip_textbox).send_keys(Keys.CONTROL + "A")
        self.browser.find_element(*self.edit_zip_textbox).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.edit_zip_textbox).send_keys(newZip)
        #self.browser.find_element(*self.save_zip_button).click()

    @allure.step("Verify user's email address")
    def verify_email(self):
        page_source = self.browser.page_source
        match = re.findall("user\\.email = '(.*?)';", str(page_source))
        return str(match[0])

    @allure.step("Verify user's phone number")
    def verify_phone(self):
        page_source = self.browser.page_source
        match = re.findall("user\\.phone = '(.*?)';", str(page_source))
        return str(match[0])

    @allure.step("Verify user's address 1")
    def verify_address1(self):
        page_source = self.browser.page_source
        match = re.findall("user\\.address_1 = '(.*?)';", str(page_source))
        return str(match[0])

    @allure.step("Verify user's address 2")
    def verify_address2(self):
        page_source = self.browser.page_source
        match = re.findall("user\\.address_2 = '(.*?)';", str(page_source))
        return str(match[0])

    @allure.step("Verify user's state")
    def verify_state(self):
        page_source = self.browser.page_source
        match = re.findall("user\\.state = '(.*?)';", str(page_source))
        return str(match[0])

    @allure.step("Verify user's city")
    def verify_city(self):
        page_source = self.browser.page_source
        match = re.findall("user\\.city = '(.*?)';", str(page_source))
        return str(match[0])

    @allure.step("Verify user's zip code")
    def verify_zip(self):
        page_source = self.browser.page_source
        match = re.findall("user\\.zip = '(.*?)';", str(page_source))
        return str(match[0])

    @allure.step("Click change password button")
    def click_change_password(self):
        self.browser.find_element(*self.change_password_button).click()

    @allure.step("Enter current password")
    def enter_cuurent_password(self, currentPassword):
        self.browser.find_element(*self.current_password).send_keys(currentPassword)

    @allure.step("Enter new password and confirm password")
    def enter_new_password(self, newPassword):
        self.browser.find_element(*self.new_password).send_keys(newPassword)
        time.sleep(2)
        self.browser.find_element(*self.confirm_new_password).send_keys(newPassword)

    @allure.step("Submit new password")
    def click_submit_password(self):
        self.browser.find_element(*self.submit_password_button).click()

    @allure.step("Verify the successful password change message")
    def verify_alert_message(self):
        message = self.browser.find_element(*self.alert_message).text
        return str(message).strip()

    @allure.step("Clicking on button -> Save Account")
    def click_save_account(self):
        self.browser.find_element(*self.save_account).click()

