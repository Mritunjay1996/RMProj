"""
This module contains the page object
for the School files page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import os
import time
import allure

class schoolFilesPage:

    #uploadResume_button = (By.XPATH, "//a[text()='UPLOAD']")
    uploadFile_input = (By.XPATH, "//input[@id='upload_file']")
    upload_button1 = (By.XPATH, "//table[@class='requirements table table-bordered table-striped']/tbody/tr[2]/td[3]/a")
    upload_button2 = (By.XPATH, "//table[@class='requirements table table-bordered table-striped']/tbody/tr[3]/td[3]/a")
    upload_button3 = (By.XPATH, "//table[@class='requirements table table-bordered table-striped']/tbody/tr[4]/td[3]/a")
    upload_type = (By.XPATH, "//select[@id='upload_type']")
    radio_button = (By.XPATH, "//*[@id='my_documents']/table/tbody/tr[3]/td[1]/input[1]")
    select_button = (By.XPATH, "//button[text()='Select']")
    success_image = (By.XPATH, "//td[b[a[contains(text(),'Requirement Automation')]]]/following-sibling::td[4]/a/img")
    success_image1 = (By.XPATH, "//table[@class='requirements table table-bordered table-striped']/tbody/tr[2]/td[5]/a/img")
    success_image2 = (By.XPATH, "//table[@class='requirements table table-bordered table-striped']/tbody/tr[3]/td[5]/a/img")
    success_image3 = (By.XPATH, "//table[@class='requirements table table-bordered table-striped']/tbody/tr[4]/td[5]/a/img")
    resume_link = (By.XPATH, "//td/b/a[contains(text(),'Requirement Automation')]")
    file_content = (By.XPATH, "//body/pre")
    input_expDate = (By.XPATH, "//input[@id='exp_date']")
    sample_file = (By.XPATH, "//a[contains(text(),'sample.pdf')]")
    document_select_button = (By.XPATH, "//button[contains(@class,'modal_callback')]")
    choose_file = (By.XPATH, "//input[@id='upload_file']")
    # choose_file = (By.XPATH, "//a[@id='upload_file_btn']")


    def __init__(self, browser):
        self.browser = browser

    @allure.step('Enter expiration date')
    def enter_ExpDate(self, date):
        self.browser.find_element_by_xpath("//input[@id='exp_date']").send_keys(date)

    @allure.step('Click 1st Upload button')
    def clickUploadResume(self):
        WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located(self.upload_button1)) #uploadResume_button
        self.browser.find_element(*self.upload_button1).click() #uploadResume_button

    @allure.step('Click 2nd Upload button')
    def clickUploadResume2(self):
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(self.upload_button2))
        self.browser.find_element(*self.upload_button2).click()

    @allure.step('Click 3rd Upload button')
    def clickUploadResume3(self):
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(self.upload_button3))
        self.browser.find_element(*self.upload_button3).click()

    def do_refresh(self):
        self.browser.refresh()

    @allure.step('Click radio button ')
    def click_radio_button(self):
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(self.radio_button))
        self.browser.find_element(*self.radio_button).click()


    @allure.step('Select Upload Type')
    def select_upload_type(self, type):
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(self.upload_type))
        sel = Select(self.browser.find_element(*self.upload_type))
        sel.select_by_value(type)

    @allure.step('Clicking on button -> Select')
    def click_document_select_button(self):
        self.browser.find_element_by_xpath("//button[contains(@class,'modal_callback')]").click()


    @allure.step('Add file path to upload input')
    def addFileToUpload(self):
        # WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(self.uploadFile_input))
        time.sleep(8)
        # path = os.getcwd() + "\\resources\\sample1.pdf"
        self.browser.find_element(*self.choose_file).send_keys(os.getcwd() + "\\resources\\sample1.pdf")
        # self.browser.find_element(*self.choose_file).click()
        # time.sleep(4)  # waiting for window popup to open
        # pyautogui.write(path)  # path of File
        # pyautogui.press('enter')

    @allure.step('Click Select button on Upload modal')
    def clickSelectButton(self):
        self.browser.find_element(*self.select_button).click()

    @allure.step('Validate successful upload')
    def validateSuccessfulUpload(self):
        img = self.browser.find_element(*self.success_image)
        return img.get_attribute("src")

    @allure.step('Validate successful upload 1')
    def validateSuccessfulUpload1(self):
        img = self.browser.find_element(*self.success_image1)
        return img.get_attribute("src")

    @allure.step('Validate successful upload 2')
    def validateSuccessfulUpload2(self):
        img = self.browser.find_element(*self.success_image2)
        return img.get_attribute("src")

    @allure.step('Validate successful upload 3')
    def validateSuccessfulUpload3(self):
        img = self.browser.find_element(*self.success_image3)
        return img.get_attribute("src")

    @allure.step('Open uploaded file')
    def openResumeLink(self):
        self.browser.find_element(*self.resume_link).click()

    @allure.step('Validate the contents of opened file')
    def validateFileContent(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
        return self.browser.find_element(*self.file_content).text

    @allure.step('Close the tab for opened file')
    def closeFileBrowserTab(self):
        # self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])