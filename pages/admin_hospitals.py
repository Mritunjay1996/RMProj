import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure

class adminHospitalObj:
    tab_Hospitals = (By.XPATH, "//a[contains(text(),'Hospitals')]")
    hospital_create_option = (By.XPATH, "//a[contains(text(),'Hospitals')]/following-sibling::ul[1]//a[text()='Create Hospital']")
    hospital_edit_option = (By.XPATH, "//a[contains(text(),'Hospitals')]/following-sibling::ul[1]//a[text()='Edit Hospital']")
    input_hospital_name = (By.XPATH, "//input[@name='hospital_name']")
    input_discipline1 = (By.XPATH, "//input[@name='hospital_discipline_row_1']")
    input_discipline2 = (By.XPATH, "//input[@name='hospital_discipline_row_2']")
    input_discipline3 = (By.XPATH, "//input[@name='hospital_discipline_row_3']")
    input_discipline4 = (By.XPATH, "//input[@name='hospital_discipline_row_4']")
    input_discipline1_speciality1 = (By.XPATH, "//input[@name='hospital_specialty_row_1[]'][1]")
    input_discipline1_speciality2 = (By.XPATH, "//input[@name='hospital_specialty_row_1[]'][2]")
    input_discipline2_speciality1 = (By.XPATH, "//input[@name='hospital_specialty_row_2[]'][1]")
    input_discipline2_speciality2 = (By.XPATH, "//input[@name='hospital_specialty_row_2[]'][2]")
    input_discipline3_speciality1 = (By.XPATH, "//input[@name='hospital_specialty_row_3[]'][1]")
    input_discipline3_speciality2 = (By.XPATH, "//input[@name='hospital_specialty_row_3[]'][2]")
    input_discipline4_speciality1 = (By.XPATH, "//input[@name='hospital_specialty_row_4[]'][1]")
    input_discipline4_speciality2 = (By.XPATH, "//input[@name='hospital_specialty_row_4[]'][2]")
    select_school1 = (By.XPATH, "//select[@id='selection']")
    add_school = (By.XPATH, "//span[@id='addOption']/img")
    submit_button = (By.XPATH, "//input[@name='submit']")
    heading = (By.XPATH, "//div[@class='span12']/h2")
    select_hospital = (By.XPATH, "//select[@name='hospital_id']")
    text_discipline1 = (By.XPATH, "//tr[1]/td[@class='discipline']/span")
    text_discipline2 = (By.XPATH, "//tr[2]/td[@class='discipline']/span")
    text_discipline1_speciality1 = (By.XPATH, "//tr[1]/td[@class='specialty']/span[1]")
    text_discipline1_speciality2 = (By.XPATH, "//tr[1]/td[@class='specialty']/span[2]")
    text_discipline2_speciality1 = (By.XPATH, "//tr[2]/td[@class='specialty']/span[1]")
    text_discipline2_speciality2 = (By.XPATH, "//tr[2]/td[@class='specialty']/span[2]")
    select_disc1_shadowing = (By.XPATH, "//tr[1]/td[2]/select")
    select_disc1_scheduler = (By.XPATH, "//tr[1]/td[3]/select")
    select_disc1_approval = (By.XPATH, "//tr[1]/td[4]/select")
    select_disc2_shadowing = (By.XPATH, "//tr[2]/td[2]/select")
    select_disc2_scheduler = (By.XPATH, "//tr[2]/td[3]/select")
    select_disc2_approval = (By.XPATH, "//tr[2]/td[4]/select")
    select_disc3_shadowing = (By.XPATH, "//tr[3]/td[2]/select")
    select_disc3_scheduler = (By.XPATH, "//tr[3]/td[3]/select")
    select_disc3_approval = (By.XPATH, "//tr[3]/td[4]/select")
    select_disc4_shadowing = (By.XPATH, "//tr[4]/td[2]/select")
    select_disc4_scheduler = (By.XPATH, "//tr[4]/td[3]/select")
    select_disc4_approval = (By.XPATH, "//tr[4]/td[4]/select")
    button_edit_speciality_disc1 = (By.XPATH, "//tr[1]//span[contains(@class,'editSpecialty')]")
    edit_discipline1_speciality1 = (By.XPATH, "//tr[1]/td[@class='specialty']/input[1]")
    edit_discipline1_speciality2 = (By.XPATH, "//tr[1]/td[@class='specialty']/input[2]")
    button_disc1_save_speciality = (By.XPATH, "//tr[1]//span[contains(@class,'saveSpecialty')]")
    button_disc1_add_location = (By.XPATH, "//tr[1]//span[contains(@class,'addLocation')]")
    button_disc3_add_location = (By.XPATH, "//tr[3]//span[contains(@class,'addLocation')]")
    input_disc1_location = (By.XPATH, "//tr[1]/td[@class='location']/input")
    input_disc3_location = (By.XPATH, "//tr[3]/td[@class='location']/input")
    button_disc1_save_location = (By.XPATH, "//tr[1]//span[contains(@class,'saveLocation')]")
    button_disc3_save_location = (By.XPATH, "//tr[3]//span[contains(@class,'saveLocation')]")
    button_save_changes = (By.XPATH, "//div[@id='structure']//input[@value='Save Changes']")
    text_discipline1_location = (By.XPATH, "//tr[1]/td[@class='location']/span")
    button_alert_ok = (By.XPATH, "//button[text()='OK']")
    button_addRow = (By.XPATH, "//span[@id='addNewRow']")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Clicking Add new row button')
    def click_addRow(self):
        self.browser.find_element(*self.button_addRow).click()

    @allure.step('Verifying discipline1 - localtion for hospital')
    def verify_hospital_creation_discipline1location(self):
        return self.browser.find_element(*self.text_discipline1_location).text

    @allure.step('Click save changes')
    def click_save_changes(self):
        self.browser.find_element(*self.button_save_changes).click()

    @allure.step('Adding the location for Discipline-1')
    def add_discipline1_location(self, value):
        self.browser.find_element(*self.button_disc1_add_location).click()
        self.browser.find_element(*self.input_disc1_location).send_keys(value)
        time.sleep(3)
        self.browser.find_element(*self.button_disc1_save_location).click()
        time.sleep(3)

    @allure.step('Adding the location for Discipline-3')
    def add_discipline3_location(self, value):
        self.browser.find_element(*self.button_disc3_add_location).click()
        self.browser.find_element(*self.input_disc3_location).send_keys(value)
        time.sleep(3)
        self.browser.find_element(*self.button_disc3_save_location).click()
        time.sleep(3)

    @allure.step('Changing the value for Discipline-1 Speciality')
    def edit_discipline1_speciality(self, value1, value2):
        self.browser.find_element(*self.button_edit_speciality_disc1).click()
        self.browser.find_element(*self.edit_discipline1_speciality1).clear()
        self.browser.find_element(*self.edit_discipline1_speciality1).send_keys(value1 + " edited")
        self.browser.find_element(*self.edit_discipline1_speciality2).clear()
        self.browser.find_element(*self.edit_discipline1_speciality2).send_keys(value2 + " edited")
        time.sleep(3)
        self.browser.find_element(*self.button_disc1_save_speciality).click()
        time.sleep(3)

    @allure.step('Changing the value for Discipline-1 Approval Flag')
    def select_discipline1_approval(self, value):
        select = Select(self.browser.find_element(*self.select_disc1_approval))
        select.select_by_visible_text(value)
        time.sleep(5)
        self.browser.find_element(*self.button_alert_ok).click()
        time.sleep(5)

    @allure.step('Changing the value for Discipline-3 Scheduler Flag')
    def select_discipline3_scheduler(self, value):
        select = Select(self.browser.find_element(*self.select_disc3_scheduler))
        select.select_by_visible_text(value)

    @allure.step('Changing the value for Discipline-1 Scheduler Flag')
    def select_discipline1_scheduler(self, value):
        select = Select(self.browser.find_element(*self.select_disc1_scheduler))
        select.select_by_visible_text(value)

    @allure.step('Changing the value for Discipline-4 Shadowing Flag')
    def select_discipline4_shadowing(self, value):
        select = Select(self.browser.find_element(*self.select_disc4_shadowing))
        select.select_by_visible_text(value)

    @allure.step('Changing the value for Discipline-1 Shadowing Flag')
    def select_discipline1_shadowing(self, value):
        select = Select(self.browser.find_element(*self.select_disc1_shadowing))
        select.select_by_visible_text(value)

    @allure.step('Verifying Discipline2 - Approval Flag for hospital creation')
    def verify_hospital_creation_disc2approval(self):
        select = Select(self.browser.find_element(*self.select_disc2_approval))
        msg = select.first_selected_option
        msg = msg.text
        return msg.strip()

    @allure.step('Verifying Discipline2 - Scheduler Flag for hospital creation')
    def verify_hospital_creation_disc2scheduler(self):
        select = Select(self.browser.find_element(*self.select_disc2_scheduler))
        msg = select.first_selected_option
        msg = msg.text
        return msg.strip()

    @allure.step('Verifying Discipline2 - Shadowing Flag for hospital creation')
    def verify_hospital_creation_disc2shadowing(self):
        select = Select(self.browser.find_element(*self.select_disc2_shadowing))
        msg = select.first_selected_option
        msg = msg.text
        return msg.strip()

    @allure.step('Verifying Discipline1 - Approval Flag for hospital creation')
    def verify_hospital_creation_disc1approval(self):
        select = Select(self.browser.find_element(*self.select_disc1_approval))
        msg = select.first_selected_option
        msg = msg.text
        return msg.strip()

    @allure.step('Verifying Discipline1 - Scheduler Flag for hospital creation')
    def verify_hospital_creation_disc1scheduler(self):
        select = Select(self.browser.find_element(*self.select_disc1_scheduler))
        msg = select.first_selected_option
        msg = msg.text
        return msg.strip()

    @allure.step('Verifying Discipline1 - Shadowing Flag for hospital creation')
    def verify_hospital_creation_disc1shadowing(self):
        select = Select(self.browser.find_element(*self.select_disc1_shadowing))
        msg = select.first_selected_option
        msg = msg.text
        return msg.strip()

    @allure.step('Verifying discipline2 - speciality2 for hospital creation')
    def verify_hospital_creation_discipline2speciality2(self):
        return self.browser.find_element(*self.text_discipline2_speciality2).text

    @allure.step('Verifying discipline2 - speciality1 for hospital creation')
    def verify_hospital_creation_discipline2speciality1(self):
        return self.browser.find_element(*self.text_discipline2_speciality1).text

    @allure.step('Verifying discipline1 - speciality2 for hospital creation')
    def verify_hospital_creation_discipline1speciality2(self):
        return self.browser.find_element(*self.text_discipline1_speciality2).text

    @allure.step('Verifying discipline1 - speciality1 for hospital creation')
    def verify_hospital_creation_discipline1speciality1(self):
        return self.browser.find_element(*self.text_discipline1_speciality1).text

    @allure.step('Verifying discipline2 for hospital creation')
    def verify_hospital_creation_discipline2(self):
        return self.browser.find_element(*self.text_discipline2).text

    @allure.step('Verifying discipline1 for hospital creation')
    def verify_hospital_creation_discipline1(self):
        return self.browser.find_element(*self.text_discipline1).text

    @allure.step('Verifying hospital name for hospital creation')
    def verify_hospital_creation_hospitalname(self):
        select = Select(self.browser.find_element(*self.select_hospital))
        msg = select.first_selected_option
        msg = msg.text
        return msg.strip()

    @allure.step('Select hospital')
    def choose_hospital(self, hosp):
        select = Select(self.browser.find_element(*self.select_hospital))
        select.select_by_visible_text(hosp)
    
    @allure.step('Verifying successful creation of hospital')
    def verify_hospital_creation(self):
        return self.browser.find_element(*self.heading).text

    @allure.step('Click submit button')
    def click_submit(self):
        self.browser.find_element(*self.submit_button).click()

    @allure.step("Selecting School-Campus-Discipline")
    def select_school(self, school):
        select = Select(self.browser.find_element(*self.select_school1))
        select.select_by_visible_text(school)
        self.browser.find_element(*self.add_school).click()

    @allure.step('Enter discipline 4 - speciality 2')
    def enter_discipline4_speciality2(self, disc4_spec2):
        self.browser.find_element(*self.input_discipline4_speciality2).send_keys(disc4_spec2)

    @allure.step('Enter discipline 4 - speciality 1')
    def enter_discipline4_speciality1(self, disc4_spec1):
        self.browser.find_element(*self.input_discipline4_speciality1).send_keys(disc4_spec1)

    @allure.step('Enter discipline 3 - speciality 2')
    def enter_discipline3_speciality2(self, disc3_spec2):
        self.browser.find_element(*self.input_discipline3_speciality2).send_keys(disc3_spec2)

    @allure.step('Enter discipline 3 - speciality 1')
    def enter_discipline3_speciality1(self, disc3_spec1):
        self.browser.find_element(*self.input_discipline3_speciality1).send_keys(disc3_spec1)

    @allure.step('Enter discipline 2 - speciality 2')
    def enter_discipline2_speciality2(self, disc2_spec2):
        self.browser.find_element(*self.input_discipline2_speciality2).send_keys(disc2_spec2)

    @allure.step('Enter discipline 2 - speciality 1')
    def enter_discipline2_speciality1(self, disc2_spec1):
        self.browser.find_element(*self.input_discipline2_speciality1).send_keys(disc2_spec1)

    @allure.step('Enter discipline 1 - speciality 2')
    def enter_discipline1_speciality2(self, disc1_spec2):
        self.browser.find_element(*self.input_discipline1_speciality2).send_keys(disc1_spec2)

    @allure.step('Enter discipline 1 - speciality 1')
    def enter_discipline1_speciality1(self, disc1_spec1):
        self.browser.find_element(*self.input_discipline1_speciality1).send_keys(disc1_spec1)

    @allure.step('Enter discipline 4')
    def enter_discipline4(self, disc4):
        self.browser.find_element(*self.input_discipline4).send_keys(disc4)

    @allure.step('Enter discipline 3')
    def enter_discipline3(self, disc3):
        self.browser.find_element(*self.input_discipline3).send_keys(disc3)

    @allure.step('Enter discipline 2')
    def enter_discipline2(self, disc2):
        self.browser.find_element(*self.input_discipline2).send_keys(disc2)

    @allure.step('Enter discipline 1')
    def enter_discipline1(self, disc1):
        self.browser.find_element(*self.input_discipline1).send_keys(disc1)

    @allure.step('Enter hospital name')
    def enter_hospital_name(self, hosp_name):
        self.browser.find_element(*self.input_hospital_name).send_keys(hosp_name)

    @allure.step('Clicking option Hospitals -> Create')
    def click_hospitals_create(self):
        self.browser.find_element(*self.hospital_create_option).click()

    @allure.step('Clicking option Hospitals -> Edit')
    def click_hospitals_edit(self):
        self.browser.find_element(*self.hospital_edit_option).click()

    @allure.step('Clicking tab - Hospitals')
    def click_tab_hospital(self):
        self.browser.find_element(*self.tab_Hospitals).click()