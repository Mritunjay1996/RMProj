import time
from selenium.webdriver.common.by import By
import allure


class adminhospitalreqObj:
    tab_manage = (By.XPATH, "//a[@class='dropdown-toggle'][contains(text(),'Manage')]")
    req_glossary = (By.XPATH, "//a[contains(text(),'Requirement Glossary')]")
    input_reqName = (By.XPATH, "//input[@id='name']")
    input_shortForm = (By.XPATH, "//input[@id='roster']")
    input_description = (By.XPATH, "//textarea[@id='description']")
    button_createReq = (By.XPATH, "//button[@class='btn btn-primary']")
    pop_okButton = (By.XPATH, "//button[@id='button-0']")
    search_box = (By.XPATH, "//label[contains(text(),'Search:')]//input")
    result_reqName = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]")
    result_reqShortForm = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]")
    log_out = (By.XPATH, "//a[contains(text(),'Logout')]")


    def __init__(self, browser):
        self.browser = browser

    @allure.step('Clicking tab - Manage')
    def click_tab_manage(self):
        self.browser.find_element(*self.tab_manage).click()

    @allure.step('Clicking option Manage -> Requirement Glossary')
    def click_manage_requirement(self):
        self.browser.find_element(*self.req_glossary).click()

    @allure.step('Entering the requirement name')
    def enter_reqName(self, reqname):
        self.browser.find_element(*self.input_reqName).send_keys(reqname)

    @allure.step('Entering the Roster short form')
    def enter_shortForm(self, reqshortname):
        self.browser.find_element(*self.input_shortForm).send_keys(reqshortname)

    @allure.step('Entering the description')
    def enter_description(self, reqdesc):
        self.browser.find_element(*self.input_description).send_keys(reqdesc)

    @allure.step('Clicking button -> create Requirement')
    def click_buttonReq(self):
        self.browser.find_element(*self.button_createReq).click()

    @allure.step('Click popup OK button to reload the page ')
    def click_okButton(self):
        self.browser.find_element(*self.pop_okButton).click()

    @allure.step('Enter requirement name to search ')
    def search_filter(self , srchname):
        self.browser.find_element(*self.search_box).send_keys(srchname)

    @allure.step('Verify save record by requirement name ')
    def verify_requirementName(self):
        return self.browser.find_element(*self.result_reqName).text

    @allure.step('verify save record by short form')
    def verify_requirementShortForm(self):
        return self.browser.find_element(*self.result_reqShortForm).text

    @allure.step('click logout button ')
    def click_logout_button(self):
        self.browser.find_element(*self.log_out).click()







