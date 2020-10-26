from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime
import dateutil.relativedelta
import os
import allure
import time

class school_myRotationsPage:

    tab_MyRotations = (By.XPATH, "//div[@id='mainmenu']//li[contains(@class,'dropdown')][1]/a")
    option_newRotation = (By.XPATH, "//li/a[text()='New']")
    option_viewRotations = (By.XPATH, "//li/a[text()='View Rotations']")
    dropdown_hospitalid = (By.XPATH, "//select[@id='hospital_id']")
    dropdown_disciplineid = (By.XPATH, "//select[@id='discipline_id']")
    dropdown_rotationType = (By.XPATH, "//select[@id='rotation_type']")
    dropdown_totalSlots = (By.XPATH, "//select[@id='total_slots']")
    link_addShift = (By.XPATH, "//a[@id='a_add_shift']")
    dropdown_startTime = (By.XPATH, "//select[@id='start_time']")
    dropdown_endTime = (By.XPATH, "//select[@id='end_time']")
    button_next = (By.XPATH, "//button[text()='NEXT']")
    input_startDate = (By.XPATH, "//input[@id='calendar_start_date']")
    input_endDate = (By.XPATH, "//input[@id='calendar_end_date']")
    checkbox_monday = (By.XPATH, "//input[@id='mon']")
    checkbox_tuesday = (By.XPATH, "//input[@id='tue']")
    checkbox_wednesday = (By.XPATH, "//input[@id='wed']")
    checkbox_thursday = (By.XPATH, "//input[@id='thu']")
    checkbox_friday = (By.XPATH, "//input[@id='fri']")
    checkbox_saturday = (By.XPATH, "//input[@id='sat']")
    checkbox_sunday = (By.XPATH, "//input[@id='sun']")
    button_save = (By.XPATH, "//button[text()='SAVE']")
    dropdown_label = (By.XPATH, "//select[@id='label_id']")
    textarea_comments = (By.XPATH, "//textarea[@id='comments']")
    button_submit = (By.XPATH, "//button[@id='crm_submit']")
    button_ok = (By.XPATH, "//button[text()='OK']")
    confirmation_text = (By.XPATH, "//span[@class='noty_text']/center")
    button_viewRotations = (By.XPATH, "//button[text()='View Rotations']")
    text_rotationNumber = (By.XPATH, "//table[@id='my_rotations']/tbody/tr[1]/td[1]")
    text_rotationNumber_hospUSer = (By.XPATH, "//table[@id='my_rotations_view']/tbody/tr[1]/td[2]")
    text_rotationLabel = (By.XPATH, "//table[@id='my_rotations']/tbody/tr[1]/td[1]/select")
    text_hospitalDetails = (By.XPATH, "//table[@id='my_rotations']/tbody/tr[1]/td[2]")
    text_startDate = (By.XPATH, "//table[@id='my_rotations']/tbody/tr[1]/td[4]")
    text_endDate = (By.XPATH, "//table[@id='my_rotations']/tbody/tr[1]/td[5]/div")
    text_totalStudents = (By.XPATH, "//table[@id='my_rotations']/tbody/tr[1]/td[8]/div")
    tab_manage = (By.XPATH, "//li[@class='dropdown']/a[contains(text(),'Manage')]")
    option_manageDatabase = (By.XPATH, "//li/a[text()='Manage Database']")
    input_rotationToEdit = (By.XPATH, "//input[@id='rotation_to_edit']")
    button_go = (By.XPATH, "//input[@id='edit_rotation']")
    text_rotationInfo = (By.XPATH, "//div[@id='rotation_info']")
    date_activeDay = (By.XPATH, "//td[@class='active day']")
    datepicker_next = (By.XPATH, "//div[@class='datepicker-days']//th[@class='next']")
    datepicker_day1 = (By.XPATH, "//td[@class='day' and text()='1']")
    button_pendingApproval = (By.XPATH, "//a[text()='Pending Approval']")
    button_process = (By.XPATH, "//table[@id='my_rotations_view']//tr[1]//td[9]/a")
    button_decline = (By.XPATH, "//table[@id='my_rotations_view']//td[11]/a")
    notification_text = (By.XPATH, "//span[@class='noty_text']")
    button_active = (By.XPATH, "//a[text()='Active']")
    button_confirm = (By.XPATH, "//button[text()='CONFIRM']")
    button_declined = (By.XPATH, "//a[text()='Declined']")
    label_from = (By.XPATH, "//label[text()='From']")
    button_pending_approval = (By.XPATH, "//button[text()='Pending Approval']")
    button_active_rotation = (By.XPATH, "//button[text()='Active Rotation']")
    button_yes = (By.XPATH, "//button[text()='YES']")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Click on YES button')
    def click_yes(self):
        self.browser.find_element(*self.button_yes).click()

    @allure.step('Click on Pending Approval button')
    def click_pending_approval(self):
        self.browser.find_element(*self.button_pending_approval).click()

    @allure.step('Click on Active Rotation button')
    def click_active_rotation(self):
        self.browser.find_element(*self.button_active_rotation).click()

    @allure.step('Verify the notification text for successful approval')
    def verify_successMessage(self):
        return self.browser.find_element(*self.notification_text).text

    @allure.step('Click on Confirm button')
    def click_confirm(self):
        self.browser.find_element(*self.button_confirm).click()

    @allure.step('Click on Decline button to decline rotation')
    def click_decline(self):
        self.browser.find_element(*self.button_decline).click()

    @allure.step('Click on Process button to approve rotation')
    def click_process(self):
        self.browser.find_element(*self.button_process).click()

    @allure.step('Click on filter Declined')
    def click_declined(self):
        self.browser.find_element(*self.button_declined).click()

    @allure.step('Click on filter Active')
    def click_active(self):
        self.browser.find_element(*self.button_active).click()

    @allure.step('Click on filter Pending Approval')
    def click_pendingApproval(self):
        self.browser.find_element(*self.button_pendingApproval).click()

    @allure.step('Verifying Rotation Status')
    def verify_rotationStatus(self):
        return self.browser.find_element(*self.text_rotationInfo).text

    @allure.step('Click Go button')
    def click_go(self):
        self.browser.find_element(*self.button_go).click()

    @allure.step('Enter rotation number')
    def enter_rotationNumberEdit(self, rot):
        self.browser.find_element(*self.input_rotationToEdit).clear()
        self.browser.find_element(*self.input_rotationToEdit).send_keys(rot)

    @allure.step('Click Option - Manage Database')
    def click_optionManageDatabase(self):
        self.browser.find_element(*self.option_manageDatabase).click()

    @allure.step('Click Tab - Manage')
    def click_tabManage(self):
        self.browser.find_element(*self.tab_manage).click()

    @allure.step('Verifying Slots offered')
    def verify_slotsOffered(self):
        return self.browser.find_element(*self.text_totalStudents).text

    @allure.step('Verifying End Date')
    def verify_endDate(self):
        return self.browser.find_element(*self.text_endDate).text

    @allure.step('Verifying Start Date')
    def verify_startDate(self):
        return self.browser.find_element(*self.text_startDate).text

    @allure.step('Verifying Hospital Details')
    def verify_HospitalDetails(self):
        return self.browser.find_element(*self.text_hospitalDetails).text

    @allure.step('Verifying Rotation Label')
    def verify_RotationLabel(self):
        select = Select(self.browser.find_element(*self.text_rotationLabel))
        msg = select.first_selected_option
        msg = msg.text
        return msg.strip()

    @allure.step('Verifying Rotation Number')
    def verify_RotationNumber(self):
        return self.browser.find_element(*self.text_rotationNumber).text

    @allure.step('Verifying Rotation Number')
    def verify_RotationNumber_hospUser(self):
        return self.browser.find_element(*self.text_rotationNumber_hospUSer).text

    @allure.step('Click View Rotations')
    def click_viewRotations(self):
        self.browser.find_element(*self.button_viewRotations).click()

    @allure.step('Reading rotation number')
    def get_rotationNumber(self):
        msg = self.browser.find_element(*self.confirmation_text).text
        msg = msg.split(' ')[1].strip()
        return msg

    @allure.step('Click OK')
    def click_ok(self):
        self.browser.find_element(*self.button_ok).click()

    @allure.step('Click Submit')
    def click_submit(self):
        self.browser.find_element(*self.button_submit).click()

    @allure.step('Enter Comments')
    def enter_comments(self, cmnt):
        self.browser.find_element(*self.textarea_comments).send_keys(cmnt)

    @allure.step('Select the rotation label')
    def select_rotationLabel(self, lbl):
        select = Select(self.browser.find_element(*self.dropdown_label))
        select.select_by_visible_text(lbl)

    @allure.step('Click Save')
    def click_save(self):
        self.browser.find_element(*self.button_save).click()

    @allure.step('Select checkbox for Monday')
    def check_monday(self):
        self.browser.find_element(*self.checkbox_monday).click()

    @allure.step('Select checkbox for All Days')
    def check_allDays(self):
        self.browser.find_element(*self.checkbox_monday).click()
        self.browser.find_element(*self.checkbox_tuesday).click()
        self.browser.find_element(*self.checkbox_wednesday).click()
        self.browser.find_element(*self.checkbox_thursday).click()
        self.browser.find_element(*self.checkbox_friday).click()
        self.browser.find_element(*self.checkbox_saturday).click()
        self.browser.find_element(*self.checkbox_sunday).click()

    @allure.step('Enter End Date')
    def enter_endDate(self):
        time.sleep(3)
        self.browser.find_element(*self.input_endDate).click()
        self.browser.find_element(*self.datepicker_next).click()
        time.sleep(1)
        self.browser.find_element(*self.datepicker_next).click()
        self.browser.find_element(*self.datepicker_day1).click()
        self.browser.find_element(*self.label_from).click()
        dt = self.browser.find_element(*self.input_endDate).get_attribute('value')
        ndt = self.normalize_date(dt)
        return ndt

    @allure.step('Enter End Date')
    def enter_endDate_mod(self, days, months, yrs):
        time.sleep(3)
        curr_date = self.browser.find_element(*self.input_endDate).get_attribute("value")
        date_obj = datetime.strptime(curr_date, "%m/%d/%Y")
        month_incre = date_obj + dateutil.relativedelta.relativedelta(months=+months)  # Add  month
        month_store = month_incre.month
        new_date_obj = date_obj.replace(year=date_obj.year + yrs).replace(month=month_store).replace(day=date_obj.day + days)
        new_date = new_date_obj.strftime("%m/%d/%Y")
        print("End Date " + str(new_date))
        self.browser.find_element(*self.input_endDate).clear()
        self.browser.find_element(*self.input_endDate).send_keys(new_date)
        return new_date

    @allure.step('Enter End Date')
    def enter_endDate_new(self):
        time.sleep(3)
        # self.browser.find_element(*self.input_endDate).click()
        # self.browser.find_element(By.XPATH, "//div[@class='datepicker-days']//th[@class='datepicker-switch']").click()
        # time.sleep(2)
        # self.browser.find_element(By.XPATH, "//div[@class='datepicker-months']//th[@class='datepicker-switch']").click()
        # time.sleep(2)
        # self.browser.find_element(By.XPATH, "//span[@class='year' and text()='2025']").click()
        # time.sleep(2)
        # self.browser.find_element(By.XPATH, "//span[@class='month' and text()='Dec']").click()
        # time.sleep(2)
        # self.browser.find_element(By.XPATH, "//td[@class='day' and text()='31']").click()
        # time.sleep(2)
        # self.browser.find_element(*self.label_from).click()
        # dt = self.browser.find_element(*self.input_endDate).get_attribute('value')
        # ndt = self.normalize_date(dt)
        # return ndt
        curr_date = self.browser.find_element(*self.input_endDate).get_attribute("value")
        date_obj = datetime.strptime(curr_date, "%m/%d/%Y")
        year_incre = date_obj.replace(year=date_obj.year + 1) # Add 1 year
        new_date = year_incre + dateutil.relativedelta.relativedelta(months=+3)  # Add 3 month
        new_date = new_date.strftime("%m/%d/%Y")
        print("End Date Disc3:" + str(new_date))
        self.browser.find_element(*self.input_endDate).clear()
        self.browser.find_element(*self.input_endDate).send_keys(new_date)
        return new_date

    @allure.step('Enter Start Date')
    def enter_startDate_new(self):
        # self.browser.find_element(*self.input_startDate).click()
        # self.browser.find_element(By.XPATH, "//div[@class='datepicker-days']//th[@class='datepicker-switch']").click()
        # time.sleep(2)
        # self.browser.find_element(By.XPATH, "//div[@class='datepicker-months']//th[@class='datepicker-switch']").click()
        # time.sleep(2)
        # self.browser.find_element(By.XPATH, "//span[@class='year' and text()='2025']").click()
        # time.sleep(2)
        # self.browser.find_element(By.XPATH, "//span[@class='month' and text()='Dec']").click()
        # time.sleep(2)
        # self.browser.find_element(By.XPATH, "//td[@class='day' and text()='1']").click()
        # time.sleep(2)
        # self.browser.find_element(*self.label_from).click()
        # dt = self.browser.find_element(*self.input_startDate).get_attribute('value')
        # ndt = self.normalize_date(dt)
        # return ndt
        curr_date = self.browser.find_element(*self.input_startDate).get_attribute("value")
        date_obj = datetime.strptime(curr_date, "%m/%d/%Y")
        year_incre = date_obj.replace(year=date_obj.year + 1)  # Add 1 year
        new_date = year_incre + dateutil.relativedelta.relativedelta(months=+1)  # Add 1 month
        new_date = new_date.strftime("%m/%d/%Y")
        print("Start Date Disc3:" + str(new_date))
        self.browser.find_element(*self.input_startDate).clear()
        self.browser.find_element(*self.input_startDate).send_keys(new_date)
        print()
        return new_date

    @allure.step('Enter Start Date')
    def enter_startDate_mod(self, days, months, yrs):
        curr_date = self.browser.find_element(*self.input_startDate).get_attribute("value")
        date_obj = datetime.strptime(curr_date, "%m/%d/%Y")
        month_incre = date_obj + dateutil.relativedelta.relativedelta(months=+months)  # Add  month
        month_store = month_incre.month
        new_date_obj = date_obj.replace(year=date_obj.year + yrs).replace(month=month_store).replace(day=date_obj.day + days)
        new_date = new_date_obj.strftime("%m/%d/%Y")
        print("Start Date " + str(new_date))
        self.browser.find_element(*self.input_startDate).clear()
        self.browser.find_element(*self.input_startDate).send_keys(new_date)
        return new_date

    @allure.step('Enter Start Date')
    def enter_startDate(self):
        self.browser.find_element(*self.input_startDate).click()
        self.browser.find_element(*self.datepicker_next).click()
        self.browser.find_element(*self.datepicker_day1).click()
        self.browser.find_element(*self.label_from).click()
        dt = self.browser.find_element(*self.input_startDate).get_attribute('value')
        ndt = self.normalize_date(dt)
        return ndt

    def normalize_date(self, dt):
        day = dt.split('/')[0]
        if day in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            day = '0' + day
        month = dt.split('/')[1]
        if month in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            month = '0' + month
        year = dt.split('/')[2]
        return day + '/' + month + '/' + year

    @allure.step('Click Next')
    def click_next(self):
        self.browser.find_element(*self.button_next).click()

    @allure.step('Select the end time')
    def select_endTime(self, end):
        select = Select(self.browser.find_element(*self.dropdown_endTime))
        select.select_by_visible_text(end)

    @allure.step('Select the start time')
    def select_startTime(self, strt):
        time.sleep(3)
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(self.dropdown_startTime))
        select = Select(self.browser.find_element(*self.dropdown_startTime))
        select.select_by_visible_text(strt)

    @allure.step('Click Add Shift')
    def click_addShift(self):
        self.browser.find_element(*self.link_addShift).click()

    def browser_zoom_out(self, steps):
        self.browser.execute_script("document.body.style.transform = 'scale(0.75)'")
        # for step in range(1, steps+1):
        #     self.browser.find_element_by_tag_name('html').send_keys(Keys.CONTROL, Keys.SUBTRACT)

    def browser_zoom_in(self, steps):
        self.browser.execute_script("document.body.style.transform = 'scale(0.75)'")
        # for step in range(1, steps+1):
        #     self.browser.find_element_by_tag_name('html').send_keys(Keys.CONTROL, Keys.ADD)

    @allure.step('Select the number of students')
    def select_studentsCount(self, stu):
        select = Select(self.browser.find_element(*self.dropdown_totalSlots))
        select.select_by_visible_text(stu)

    @allure.step('Select the rotation type')
    def select_rotationType(self, rot):
        select = Select(self.browser.find_element(*self.dropdown_rotationType))
        select.select_by_visible_text(rot)

    @allure.step('Select the discipline')
    def select_discipline(self, disc):
        select = Select(self.browser.find_element(*self.dropdown_disciplineid))
        select.select_by_visible_text(disc)

    @allure.step('Select the hospital')
    def select_hospital(self, hosp):
        select = Select(self.browser.find_element(*self.dropdown_hospitalid))
        select.select_by_visible_text(hosp)

    @allure.step('Select the discipline')
    def select_discipline(self, disc):
        select = Select(self.browser.find_element(*self.dropdown_disciplineid))
        select.select_by_visible_text(disc)

    @allure.step('Click option - View Rotations')
    def click_option_viewRotations(self):
        self.browser.find_element(*self.option_viewRotations).click()

    @allure.step('Click option - New')
    def click_option_new(self):
        self.browser.find_element(*self.option_newRotation).click()

    @allure.step('Click tab - My Rotations')
    def click_tab_MyRotations(self):
        self.browser.find_element(*self.tab_MyRotations).click()