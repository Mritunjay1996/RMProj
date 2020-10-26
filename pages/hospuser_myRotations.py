from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import os
import allure
import time

class hosp_myRotationsPage:

    tab_myRotations = (By.XPATH, "//li/a[contains(text(),'My Rotations')]")
    option_viewRotations = (By.XPATH, "//li/a[contains(text(),'View Rotations')]")
    filter_pendingApproval = (By.XPATH, "//a[text()='Pending Approval']")
    filter_active = (By.XPATH, "//a[text()='Active']")
    filter_declined = (By.XPATH, "//a[text()='Declined']")
    hosp_rotation_process = (By.XPATH, "//table[@id='my_rotations_view']/tbody/tr[5]/td[9]/a[text()='Process']")
    hosp_rotation_process1 = (By.XPATH, "//a[text()='Process']")
    button_acceptRequest = (By.XPATH,"//button[text()='Accept Request']")
    button_OK = (By.XPATH, "//button[text()='OK']")
    button_confirm = (By.XPATH, "//button[text()='CONFIRM']")
    fitNo_overlapYes_process = (By.XPATH, "//table[@id='my_rotations_view']/tbody/tr[2]/td[9]/a[text()='Process']")
    fitNo_overlapNo_process = (By.XPATH, "//table[@id='my_rotations_view']/tbody/tr[1]/td[9]/a[text()='Process']")
    fitYes_overlapNo_process = (By.XPATH, "//table[@id='my_rotations_view']/tbody/tr[3]/td[9]/a[text()='Process']")
    fitYes_overlapYes_process = (By.XPATH, "//table[@id='my_rotations_view']/tbody/tr[4]/td[9]/a[text()='Process']")
    process_button = (By.XPATH, "//a[text()='Process']")
    message_process_rotation = (By.XPATH, "//div[@class='bootbox-body']/h4[1]")
    message_process_rotation2 = (By.XPATH, "//div[@class='bootbox-body']/b")
    confirmation_text = (By.XPATH, "//span[@class='noty_text']/center")
    first_rotation_number = (By.XPATH, "//table[@id='my_rotations_view']/tbody/tr[1]/td[2]")
    all_rotation_number = (By.XPATH, "//table[@id='my_rotations_view']/tbody/tr/td[2]")
    dropdown_cancel_overlap = (By.XPATH, "//select[@id='cancel_overlap']")
    cancelled_button = (By.XPATH, "//a[contains(text(),'Cancelled')]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Select Yes for cancel overlap option')
    def select_cancel_overlap(self, opt):
        select = Select(self.browser.find_element(*self.dropdown_cancel_overlap))
        select.select_by_visible_text(opt)

    @allure.step('Verifying the message for rotation processing')
    def verify_message_process(self):
        msg = self.browser.find_element(*self.message_process_rotation).text
        return msg.replace('\n','')

    @allure.step('Verifying the message for rotation processing')
    def verify_message_process2(self):
        msg = self.browser.find_element(*self.message_process_rotation2).text
        return msg.replace('\n', '')

    @allure.step('Verifying the first rotation number')
    def verify_first_rotation(self):
        msg = self.browser.find_element(*self.first_rotation_number).text
        return msg.strip()

    @allure.step('Verifying from all rotation number')
    def verify_all_rotation(self, rot):
        rotations = self.browser.find_elements(*self.all_rotation_number)
        flag = False
        for rotation in rotations:
            if rot in rotation.text:
                flag = True
        return flag

    @allure.step('Clicking tab My Rotations')
    def click_myRotations(self):
        self.browser.find_element(*self.tab_myRotations).click()

    @allure.step('Clicking option View Rotations')
    def click_viewRotations(self):
        self.browser.find_element(*self.option_viewRotations).click()

    @allure.step('Clicking filter Pending Approvals')
    def click_pendingApprovals(self):
        self.browser.find_element(*self.filter_pendingApproval).click()

    @allure.step('Clicking filter Active')
    def click_Active(self):
        self.browser.find_element(*self.filter_active).click()

    @allure.step('Clicking filter Declined')
    def click_Declined(self):
        self.browser.find_element(*self.filter_declined).click()

    @allure.step('Clicking Process button for pending rotation from hospital user')
    def click_process_hospitalRotation(self):
        self.browser.find_element(*self.hosp_rotation_process).click()

    @allure.step('Clicking Process button for rotation which not fits the schedule but overlaps other rotation')
    def click_process_fitNo_overlapYes(self):
        self.browser.find_element(*self.fitNo_overlapYes_process).click()

    @allure.step('Clicking Process button for rotation which not fits the schedule and not overlaps other rotation')
    def click_process_fitNo_overlapNo(self):
        self.browser.find_element(*self.fitNo_overlapNo_process).click()

    @allure.step('Clicking Process button for rotation which fits the schedule and not overlaps other rotation')
    def click_process_fitYes_overlapNo(self):
        self.browser.find_element(*self.fitYes_overlapNo_process).click()

    @allure.step('Clicking Process button for rotation which fits the schedule and overlaps other rotation')
    def click_process_fitYes_overlapYes(self):
        self.browser.find_element(*self.fitYes_overlapYes_process).click()

    @allure.step('Clicking button for Accept Request')
    def click_acceptRequest(self):
        # self.browser.find_element(*self.button_acceptRequest).click()
        display = self.browser.find_element(*self.button_acceptRequest).is_displayed()
        print(display)
        time.sleep(2)
        element = self.browser.find_element(*self.button_acceptRequest)
        self.browser.execute_script("arguments[0].click();", element)

    @allure.step('Clicking button OK')
    def click_ok(self):
        self.browser.find_element(*self.button_OK).click()

    @allure.step('Clicking button Confirm')
    def click_confirm(self):
        # self.browser.find_element(*self.button_confirm).click()
        display = self.browser.find_element(*self.button_confirm).is_displayed()
        print(display)
        time.sleep(2)
        element = self.browser.find_element(*self.button_confirm)
        self.browser.execute_script("arguments[0].click();", element)

    @allure.step('Reading rotation number')
    def get_rotationNumber(self):
        msg = self.browser.find_element(*self.confirmation_text).text
        msg = msg.split('#')[1].strip()
        msg = msg.split('has')[0].strip()
        return msg

    @allure.step('CLicking on cancelled button')
    def click_cancelledBtn(self):
        self.browser.find_element(*self.cancelled_button).click()