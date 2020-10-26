import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import allure

class adminsetsschoollicensesObj:

    tab_manage = (By.XPATH, "//a[@class='dropdown-toggle'][contains(text(),'Manage')]")
    licenses_option = (By.XPATH, "//a[contains(text(),'School Licenses')]")
    add_button = (By.XPATH, "//button[@class='btn btn-primary']")
    scool_disc = (By.XPATH, "//div[@class='controls']/select")
    num_licenses = (By.XPATH,"//input[@id='quantity']")
    amount = (By.XPATH, "//input[@id='amount']")
    submit_btn = (By.XPATH, "//button[@id='submit']")
    pop_okbtn =(By.XPATH, "//button[@id='button-0']")
    lcns_summary = (By.XPATH, "//table[@class='table table-bordered table-striped dataTable no-footer']/tbody/tr//td[@id]")
    lcns_purchase = (By.XPATH, "//div[@id='purchase_history_wrapper']//td[2]")
    subscription_period_purchase = (By.XPATH, "//div[@id='purchase_history_wrapper']//td[5]")
    subs_period_reg = (By.XPATH, "//label[@id='initial_period_label']")



    def __init__(self, browser):
        self.browser = browser

    @allure.step("Clicking tab -> Manage")
    def click_tab_manage(self):
        self.browser.find_element(*self.tab_manage).click()

    @allure.step("Clicking option Manage -> School licenses")
    def click_school_licenses_option(self):
        self.browser.find_element(*self.licenses_option).click()

    @allure.step("Click button -> Add new ")
    def click_add_new_button(self):
        self.browser.find_element(*self.add_button).click()

    @allure.step("Select School-discpline from Dropdown ")
    def select_school_displine(self, school):
        sel = Select(self.browser.find_element(*self.scool_disc))
        sel.select_by_visible_text(school)

    @allure.step("Entering number of licenses ")
    def enter_number_license(self, number):
        self.browser.find_element(*self.num_licenses).send_keys(number)

    @allure.step("Click on amount textfield")
    def click_on_amount(self):
        self.browser.find_element(*self.amount).click()

    @allure.step("Clicking on button -> SUBMIT")
    def click_on_submit(self):
        self.browser.find_element(*self.submit_btn).click()

    @allure.step("Clicking on popup button -> OK")
    def click_on_ok(self):
        self.browser.find_element(*self.pop_okbtn).click()

    @allure.step("Verify licenses is in summnary table")
    def verify_license_name(self):
        return self.browser.find_element(*self.lcns_summary).text

    @allure.step("Verify num of licenses in purchase table")
    def verify_numof_license(self):
        return self.browser.find_element(*self.lcns_purchase).text

    @allure.step('Verify subscription period from purchase table')
    def verify_subscription_period(self):
        return self.browser.find_element(*self.subscription_period_purchase).text

    @allure.step('Verify subscription period from register table')
    def verify_subscription_period_register(self):
        return self.browser.find_element(*self.subs_period_reg).text











