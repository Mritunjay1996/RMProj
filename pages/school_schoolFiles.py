from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui
import os
import allure

class school_schoolFilesPage:

    pyautogui.FAILSAFE = False
    tab_schoolFiles = (By.XPATH, "//a[text()[1]='School Files']")
    option_forStudents = (By.XPATH, "//a[text()='For Students']")
    option_forInstructors = (By.XPATH, "//a[text()='For Instructors']")
    select_studentMust = (By.XPATH, "//label[text()='Add a document that students must...']/following-sibling::select[1]")
    select_instructorMust = (By.XPATH, "//label[text()='Add a document that instructors must...']/following-sibling::select[1]")
    input_documentName = (By.XPATH, "//table[@id='req_files']//td[label[text()='Download']]/following-sibling::td[1]/input")
    attach_file = (By.XPATH, "(//a[contains(text(),'ATTACH')])[1]")
    input_choosefile = (By.XPATH, "//table[@id='req_files']//input[@id='upload_file']")
    # choose_file = (By.XPATH, "//input[@id='upload_file']")
    choose_file = (By.XPATH, "//a[@id='upload_file_btn']")
    choose_file_direct = (By.XPATH, "(//input[contains(@id,'upload_file_')])[1]")
    button_saveChanges = (By.XPATH, "//button[text()='SAVE CHANGES']")
    select_requirement = (By.XPATH), "//table[@id='req_files']//select[@id='glossary']"
    select_expirationDate = (By.XPATH, "//table[@id='req_files']//select[@name='exp_date_req[]']")
    label_readRequirementName = (By.XPATH, "//table[@id='req_files']//tr[1]//input[@name='name[]']")
    label_readRequirementMandatory = (By.XPATH, "//table[@id='req_files']//tr[1]//td[7]/b")
    label_provideRequirementName = (By.XPATH, "//table[@id='req_files']//tr[2]//input[@name='name[]']")
    label_provideRequirementMandatory = (By.XPATH, "//table[@id='req_files']//tr[2]//td[7]/b")
    label_provideRequirementExpiration = (By.XPATH, "//table[@id='req_files']//tr[2]//td[6]/b")
    button_agreement = (By.XPATH, "//a[text()='I AGREE']")
    save_change = (By.XPATH, "//button[contains(text(),'Save Changes')]")

    read_attachBtn = (By.XPATH, "//tbody[@class='ui-sortable']//td[input[@placeholder='Enter Document Name']]/following-sibling::td[1]/a")
    provide_attachBtn = (By.XPATH, "//tbody[@class='ui-sortable']//td[div[input[@placeholder='Document Name']]]/following-sibling::td[2]/a")
    input_provide = (By.XPATH, "//table[@id='req_files']//input[@placeholder='Document Name']")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Click Save Changes')
    def click_button_agreement(self):
        self.browser.find_element(*self.button_agreement).click()

    @allure.step('Verify the Expiration flag for Provide requirement')
    def verify_provideRequirementExpiration(self):
        msg = self.browser.find_element(*self.label_provideRequirementExpiration).text
        return msg

    @allure.step('Verify the Mandatory flag for Provide requirement')
    def verify_provideRequirementMandatory(self):
        msg = self.browser.find_element(*self.label_provideRequirementMandatory).text
        return msg

    @allure.step('Verify the requirement name for Provide requirement')
    def verify_provideRequirementName(self):
        msg = self.browser.find_element(*self.label_provideRequirementName).get_attribute('value')
        return msg

    @allure.step('Verify the Mandatory flag for Read requirement')
    def verify_readRequirementMandatory(self):
        msg = self.browser.find_element(*self.label_readRequirementMandatory).text
        return msg

    @allure.step('Verify the requirement name for Read requirement')
    def verify_readRequirementName(self):
        msg = self.browser.find_element(*self.label_readRequirementName).get_attribute('value')
        return msg

    @allure.step('Select the value for Doc with Expiration Date?')
    def select_option_expirationDate(self, value):
        element = self.browser.find_element(*self.select_expirationDate)
        ActionChains(self.browser).move_to_element(element).perform()
        time.sleep(2)
        select = Select(self.browser.find_element(*self.select_expirationDate))
        select.select_by_visible_text(value)

    @allure.step('Select the requirement')
    def select_option_requirement(self, value):
        select = Select(self.browser.find_element(*self.select_requirement))
        select.select_by_value(value)

    @allure.step('Enter the requirement')
    def enter_requirement_option(self, reqName):
        self.browser.find_element(*self.input_documentName).send_keys(reqName)

    @allure.step('Enter the requirement in Provide')
    def enter_requirement_provide(self, reqName):
        self.browser.find_element(*self.input_provide).send_keys(reqName)

    @allure.step('Click Save Changes')
    def click_saveChanges(self):
        self.browser.find_element(*self.button_saveChanges).click()

    def page_refresh(self):
        self.browser.refresh()

    @allure.step('Enter file path for Read requirement')
    def selectFileForUpload(self):
        # self.browser.find_element(*self.attach_file).click()
        # time.sleep(4)
        self.browser.find_element(*self.choose_file_direct).send_keys(os.getcwd()+"\\resources\\sample.pdf")
        # path = os.getcwd()+"\\resources\\sample.pdf"
        # self.browser.find_element(*self.choose_file).click()
        # time.sleep(4)  # waiting for window popup to open
        # pyautogui.write(path)  # path of File
        # pyautogui.press('enter')

    @allure.step('Click on save changes button to upload file')
    def click_savechanges_uploadfile(self):
        self.browser.find_element(*self.save_change).click()

    @allure.step('Enter document name for Read requirement')
    def enter_documentName(self, text):
        self.browser.find_element(*self.input_documentName).click()
        self.browser.find_element(*self.input_documentName).send_keys(text)

    @allure.step('Select an option from the dropdown Student Must...')
    def select_option_studentMust(self, value):
        select = Select(self.browser.find_element(*self.select_studentMust))
        select.select_by_value(value)

    @allure.step('Select an option from the dropdown Instructor Must...')
    def select_option_instructorMust(self, value):
        select = Select(self.browser.find_element(*self.select_instructorMust))
        select.select_by_value(value)

    @allure.step('Click dropdown option <For Students>')
    def click_option_forStudents(self):
        self.browser.find_element(*self.option_forStudents).click()

    @allure.step('Click dropdown option <For Instructors>')
    def click_option_forInstructors(self):
        self.browser.find_element(*self.option_forInstructors).click()

    @allure.step('Click tab for School files')
    def click_tab_schoolFiles(self):
        self.browser.find_element(*self.tab_schoolFiles).click()