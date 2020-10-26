import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime
import allure

class customizeUnits:

    tab_schedules = (By.XPATH, "//a[text()='Schedules']")
    start_date1 = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[1]/td[2]//input[@class='input-small']")
    start_date2 = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[2]/td[2]//input[@class='input-small']")
    end_date1 = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[1]/td[3]//input[@class='input-small']")
    end_date2 = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[2]/td[3]//input[@class='input-small']")
    start_time1 = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[1]/td[5]//select[@class='input-medium']")
    start_time2 = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[2]/td[5]//select[@class='input-medium']")
    end_time1 = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[1]/td[6]//select[@class='input-medium']")
    end_time2 = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[2]/td[6]//select[@class='input-medium']")
    students1 = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[1]/td[7]//input[@class='input-small']")
    students2 = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[2]/td[7]//input[@class='input-small']")
    disc1_monday = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[1]/td[8]//input")
    disc1_tuesday = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[1]/td[9]//input")
    disc1_wednesday = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[1]/td[10]//input")
    disc1_thursday = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[1]/td[11]//input")
    disc1_friday = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[1]/td[12]//input")
    disc1_saturday = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[1]/td[13]//input")
    disc1_sunday = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[1]/td[14]//input")
    disc2_saturday = (By.XPATH, "//table[@id='schedules_table']/tbody/tr[2]/td[13]//input")
    button_save = (By.XPATH, "//div[@id='schedule']//button[@type='submit']")
    unit_sheduleTab = (By.XPATH, "//a[contains(text(),'Unit Schedules')]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Click the tab Schedules')
    def click_tab_schedules(self):
        self.browser.find_element(*self.tab_schedules).click()

    @allure.step('Edit start date for discipline 1')
    def edit_startdate_disc1(self):
        curr_date = self.browser.find_element(*self.start_date1).get_attribute("value")
        date_obj = datetime.strptime(curr_date, "%m/%d/%Y")
        new_date_obj = date_obj.replace(year=date_obj.year+1)
        new_date = new_date_obj.strftime("%m/%d/%Y")
        print("Start Date Disc1:" + str(new_date))
        self.browser.find_element(*self.start_date1).clear()
        self.browser.find_element(*self.start_date1).send_keys(new_date)
        return new_date

    @allure.step('Edit end date for discipline 1')
    def edit_enddate_disc1(self):
        curr_date = self.browser.find_element(*self.end_date1).get_attribute("value")
        date_obj = datetime.strptime(curr_date, "%m/%d/%Y")
        new_date_obj = date_obj.replace(year=date_obj.year + 1).replace(month=date_obj.month + 2)
        new_date = new_date_obj.strftime("%m/%d/%Y")
        print("End Date Disc1:" + str(new_date))
        self.browser.find_element(*self.end_date1).clear()
        self.browser.find_element(*self.end_date1).send_keys(new_date)
        return new_date

    @allure.step('Edit start time for discipline 1')
    def edit_starttime_disc1(self, time):
        select = Select(self.browser.find_element(*self.start_time1))
        select.select_by_visible_text(time)

    @allure.step('Edit end time for discipline 1')
    def edit_endtime_disc1(self, time):
        select = Select(self.browser.find_element(*self.end_time1))
        select.select_by_visible_text(time)

    @allure.step('Edit number of students for discipline 1')
    def edit_students_disc1(self, number):
        self.browser.find_element(*self.students1).clear()
        self.browser.find_element(*self.students1).send_keys(number)

    @allure.step('Select days for discipline 1')
    def select_days_disc1(self):
        self.browser.find_element(*self.disc1_monday).click()
        self.browser.find_element(*self.disc1_tuesday).click()
        self.browser.find_element(*self.disc1_wednesday).click()
        self.browser.find_element(*self.disc1_thursday).click()
        self.browser.find_element(*self.disc1_friday).click()
        self.browser.find_element(*self.disc1_saturday).click()
        self.browser.find_element(*self.disc1_sunday).click()

    @allure.step('Edit start date for discipline 2')
    def edit_startdate_disc2(self):
        curr_date = self.browser.find_element(*self.start_date2).get_attribute("value")
        date_obj = datetime.strptime(curr_date, "%m/%d/%Y")
        new_date_obj = date_obj.replace(year=date_obj.year + 2)
        new_date = new_date_obj.strftime("%m/%d/%Y")
        print("Start Date Disc2:" + str(new_date))
        self.browser.find_element(*self.start_date2).clear()
        self.browser.find_element(*self.start_date2).send_keys(new_date)
        return new_date

    @allure.step('Edit end date for discipline 2')
    def edit_enddate_disc2(self):
        curr_date = self.browser.find_element(*self.end_date2).get_attribute("value")
        date_obj = datetime.strptime(curr_date, "%m/%d/%Y")
        new_date_obj = date_obj.replace(year=date_obj.year + 2).replace(month=date_obj.month + 1)
        new_date = new_date_obj.strftime("%m/%d/%Y")
        print("End Date Disc2:" + str(new_date))
        self.browser.find_element(*self.end_date2).clear()
        self.browser.find_element(*self.end_date2).send_keys(new_date)
        return new_date

    @allure.step('Edit start time for discipline 2')
    def edit_starttime_disc2(self, time):
        select = Select(self.browser.find_element(*self.start_time2))
        select.select_by_visible_text(time)

    @allure.step('Edit end time for discipline 2')
    def edit_endtime_disc2(self, time):
        select = Select(self.browser.find_element(*self.end_time2))
        select.select_by_visible_text(time)

    @allure.step('Edit number of students for discipline 2')
    def edit_students_disc2(self, number):
        self.browser.find_element(*self.students2).clear()
        self.browser.find_element(*self.students2).send_keys(number)

    @allure.step('Select days for discipline 2')
    def select_days_disc2(self):
        self.browser.find_element(*self.disc2_saturday).click()

    @allure.step('Click Save button')
    def click_save(self):
        self.browser.find_element(*self.button_save).click()

    @allure.step('Verify start date for discipline 1')
    def verify_startdate_disc1(self):
        curr_date = self.browser.find_element(*self.start_date1).get_attribute("value")
        return curr_date

    @allure.step('Verify end date for discipline 1')
    def verify_enddate_disc1(self):
        curr_date = self.browser.find_element(*self.end_date1).get_attribute("value")
        return curr_date

    @allure.step('Verify start time for discipline 1')
    def verify_starttime_disc1(self):
        select = Select(self.browser.find_element(*self.start_time1))
        option = select.first_selected_option
        return option.text

    @allure.step('Verify end time for discipline 1')
    def verify_endtime_disc1(self):
        select = Select(self.browser.find_element(*self.end_time1))
        option = select.first_selected_option
        return option.text

    @allure.step('Verify number of students for discipline 1')
    def verify_students_disc1(self):
        return self.browser.find_element(*self.students1).get_attribute("value")

    @allure.step('Verify days for discipline 1')
    def verify_days_disc1(self):
        return self.browser.find_element(*self.disc1_monday).is_selected()

    @allure.step('Verify start date for discipline 2')
    def verify_startdate_disc2(self):
        curr_date = self.browser.find_element(*self.start_date2).get_attribute("value")
        return curr_date

    @allure.step('Verify end date for discipline 2')
    def verify_enddate_disc2(self):
        curr_date = self.browser.find_element(*self.end_date2).get_attribute("value")
        return curr_date

    @allure.step('Verify start time for discipline 2')
    def verify_starttime_disc2(self):
        select = Select(self.browser.find_element(*self.start_time2))
        option = select.first_selected_option
        return option.text

    @allure.step('Verify end time for discipline 2')
    def verify_endtime_disc2(self):
        select = Select(self.browser.find_element(*self.end_time2))
        option = select.first_selected_option
        return option.text

    @allure.step('Verify number of students for discipline 2')
    def verify_students_disc2(self):
        return self.browser.find_element(*self.students2).get_attribute("value")

    @allure.step('Verify days for discipline 2')
    def verify_days_disc2(self):
        return self.browser.find_element(*self.disc2_saturday).is_selected()

    @allure.step('Click on unit schedule tab')
    def click_unit_schedule(self):
        self.browser.find_element(*self.unit_sheduleTab).click()