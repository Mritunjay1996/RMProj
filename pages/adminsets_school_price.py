import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import allure


class adminsetsschoolpriceObj:
    tab_manage = (By.XPATH, "//a[@class='dropdown-toggle'][contains(text(),'Manage')]")
    school_option = (By.XPATH, "//a[contains(text(),'School Price')]")
    school_list = (By.XPATH, "//div[@class='controls']/select")
    reg_price = (By.XPATH, "//input[@id='price']")
    reg_period = (By.XPATH, "//input[@id='initial_period']")
    renewal_price = (By.XPATH, "//input[@id='renew']")
    school_button = (By.XPATH, "//button[@id='submit']")
    search = (By.XPATH, "//label[contains(text(),'Search:')]//input")
    school_edit = (By.XPATH, "//span[@class='label label-success']")
    schoolresult_name = (By.XPATH, "//table[@id='schools_price']/tbody//tr[@class='odd']/td[@id]")
    log_out = (By.XPATH, "//a[contains(text(),'Logout')]")
    reg_tab = (By.XPATH, "//a[contains(text(),'Register')]")
    selreg_school = (By.XPATH, "//select[@id='combo']")
    reg_charged = (By.XPATH, "//span[@id='charge_label']")
    reg_renewal = (By.XPATH, "//span[@id='renewal_label']")

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Clicking tab -> Manage")
    def click_tab_manage(self):
        self.browser.find_element(*self.tab_manage).click()

    @allure.step("Clicking option Manage -> School Price")
    def click_school_option(self):
        self.browser.find_element(*self.school_option).click()

    @allure.step("Select school name for set price")
    def select_school_list(self, school):
        sel = Select(self.browser.find_element(*self.school_list))
        sel.select_by_visible_text(school)

    @allure.step("Enter Registeration Price")
    def enter_register_price(self, price):
        self.browser.find_element(*self.reg_price).send_keys(price)

    @allure.step("Enter Registeration subscription period ")
    def enter_register_period(self, subs_period):
        prd = self.browser.find_element(*self.reg_period)
        prd.clear()
        time.sleep(2)
        prd.send_keys(subs_period)

    @allure.step("Enter Renewal Price")
    def enter_renewal_price(self, renewal):
        self.browser.find_element(*self.renewal_price).send_keys(renewal)

    @allure.step("Click button -> Create School Prices")
    def click_create_schoolprice(self):
        self.browser.find_element(*self.school_button).click()

    @allure.step("Enter School name for search records ")
    def enter_school_search(self, school):
        self.browser.find_element(*self.search).send_keys(school)

    @allure.step("Verify School is registerd in School Discpline list")
    def verify_school_name(self):
        return self.browser.find_element(*self.schoolresult_name).text


    @allure.step("Click Edit button to verify reg price")
    def click_edit_button(self):
        self.browser.find_element(*self.school_edit).click()

    @allure.step("Verify school price in textfield")
    def verify_school_price(self):
        return self.browser.find_element(*self.reg_price).get_attribute("value")

    @allure.step("Click tab -> logout")
    def click_logout_tab(self):
        self.browser.find_element(*self.log_out).click()

    @allure.step("Click tab -> Register")
    def click_register_tab(self):
        self.browser.find_element(*self.reg_tab).click()

    @allure.step("Select school name in Registeration page")
    def select_reg_school(self, school):
        sel = Select(self.browser.find_element(*self.selreg_school))
        sel.select_by_visible_text(school)

    @allure.step("Verify school price in Registeration page")
    def verify_register_price(self):
        return self.browser.find_element(*self.reg_charged).text

    @allure.step("Verify renewal period in Registeration page")
    def verify_register_period(self):
        return self.browser.find_element(*self.reg_renewal).text
