"""
This module contains the page object
for the homepage.
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure

class homepageObjects:
    """
    Define all web element locators and test steps
    in this class for homepage
    """

    URL = "https://rmdev2.com/"
    register_link = (By.XPATH, '//a[text()="Register"]')
    username_input = (By.XPATH, '//input[@name="username"]')
    password_input = (By.XPATH, '//input[@name="password"]')
    login_button = (By.XPATH, '//input[@value="Login"]')
    label_username = (By.XPATH, '//label[contains(text(),"You are logged in as")]/b')
    schoolFiles_link = (By.XPATH, '//a[text()="My School Files"]')
    logout_link = (By.XPATH, "//a[text()='Logout']")
    manage_dropdown = (By.XPATH, "//a[contains(text(),'Manage') and @class='dropdown-toggle']")
    schoolLicenses_option = (By.XPATH, "//a[text()='School Licenses']")
    searchBox = (By.XPATH, "//input[@type='search']")
    student_licenseAssigned = (By.XPATH, "//td[contains(text(),'School Automation')]/following-sibling::td[2]")
    student_licenseRemaining = (By.XPATH, "//td[contains(text(),'School Automation')]/following-sibling::td[3]")
    #log_out = (By.XPATH, "//a[contains(text(),'Logout')]")
    tab_help = (By.XPATH, "//li/a[text()='Help']")
    tab_customize = (By.XPATH, "//li/a[text()='Customize']")
    option_FAQ = (By.XPATH, "//li/a[contains(text(),'FAQ')]")
    option_Tutorial = (By.XPATH, "//li/a[text()='Tutorial']")
    option_CallMeBack = (By.XPATH, "//li/a[text()='Call me back']")
    option_Helpdesk = (By.XPATH, "//li/a[text()='HelpDesk']")
    option_units = (By.XPATH, "//li/a[text()='Units']")
    tab_MyStudents = (By.XPATH,"//div[@id='mainmenu']//li[@class='dropdown'][2]/a")
    tab_MyDisciplines = (By.XPATH, "//li/a[text()='My Disciplines']")
    option_students = (By.XPATH, "//li//li/a[text()='Students']")
    select_addDiscipline = (By.XPATH, "//select[@id='my_discipline_add_discipline']")
    button_submitAddDiscipline = (By.XPATH, "//a[@id='my_discipline_add_discipline_button']")
    button_close_modal = (By.XPATH, "//button[text()='Close']")

    def __init__(self, browser):
        self.browser = browser

    @allure.step
    def choose_discipline_to_add(self, disc):
        select = Select(self.browser.find_element(*self.select_addDiscipline))
        select.select_by_visible_text(disc)

    @allure.step('Click close button on modal')
    def clickCloseModal(self):
        self.browser.find_element(*self.button_close_modal).click()

    @allure.step('Click submit button')
    def clickSubmitAddDiscipline(self):
        self.browser.find_element(*self.button_submitAddDiscipline).click()

    @allure.step('Click the menu option Students')
    def clickOptionStudents(self):
        self.browser.find_element(*self.option_students).click()

    @allure.step('Click the tab My Disciplines')
    def clickMyDisciplines(self):
        self.browser.find_element(*self.tab_MyDisciplines).click()

    @allure.step('Click the tab My Students')
    def clickMyStudents(self):
        self.browser.find_element(*self.tab_MyStudents).click()

    @allure.step('Click the menu option Units')
    def clickOptionUnits(self):
        self.browser.find_element(*self.option_units).click()

    @allure.step('Click the tab for Customize')
    def clickCustomize(self):
        self.browser.find_element(*self.tab_customize).click()

    @allure.step("Click Help -> HelpDesk")
    def clickOptionHelpdesk(self):
        self.browser.find_element(*self.option_Helpdesk).click()

    @allure.step("Click Help -> Call Me Back")
    def clickOptionCallMeBack(self):
        self.browser.find_element(*self.option_CallMeBack).click()

    @allure.step("Click Help -> FAQ's")
    def clickOptionFAQ(self):
        self.browser.find_element(*self.option_FAQ).click()

    @allure.step('Click the tab for Help section')
    def clickHelp(self):
        self.browser.find_element(*self.tab_help).click()

    @allure.step('Load the homepage in browser')
    def load(self):
        self.browser.get(self.URL)

    @allure.step('Click Register link')
    def clickRegister(self):
        self.browser.find_element(*self.register_link).click()

    @allure.step('Enter username for login')
    def enterUsername(self, username):
        self.browser.find_element(*self.username_input).send_keys(username)

    @allure.step('Enter password for login')
    def enterPassword(self, password):
        self.browser.find_element(*self.password_input).send_keys(password)

    @allure.step('Click login button')
    def clickLogin(self):
        self.browser.find_element(*self.login_button).click()


    @allure.step('Validate successful login')
    def validateSuccessfulLogin(self):
        time.sleep(3)
        return self.browser.find_element(*self.label_username).text

    @allure.step('Click on My School Files tab')
    def clickSchoolFiles(self):
        self.browser.find_element(*self.schoolFiles_link).click()

    @allure.step('Logout current user')
    def clickLogout(self):
        self.browser.find_element(*self.logout_link).send_keys(Keys.ENTER)

    @allure.step('Opening option Manage -> School Licenses')
    def manage_schoolLicenses(self):
        self.browser.find_element(*self.manage_dropdown).click()
        self.browser.find_element(*self.schoolLicenses_option).click()

    @allure.step('Entering keyword to Serach Box')
    def enter_search_word(self, keyword):
        self.browser.find_element(*self.searchBox).send_keys(keyword)

    @allure.step('Checking assigned licenses')
    def return_assignedLicenses(self):
        return self.browser.find_element(*self.student_licenseAssigned).text

    @allure.step('Checking remaining licenses')
    def return_remainingLicenses(self):
        return self.browser.find_element(*self.student_licenseRemaining).text

    # def click_logout_button(self):
    #     self.browser.find_element(*self.log_out).click()
