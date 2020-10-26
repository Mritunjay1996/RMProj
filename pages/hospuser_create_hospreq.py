import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure
import pyautogui

class hospusercreatehospreqObj:

    pyautogui.FAILSAFE = False
    hosp_agreement = (By.XPATH, "//a[@class='btn btn-inverse']")
    hosp_mydiscipline = (By.XPATH, "//a[contains(text(),'My Disciplines')]")
    hosp_edithospReq = (By.XPATH, "//a[contains(text(),'Edit Student Requirements')]")
    disc_selectdocument =(By.XPATH, "//div[@class='span12']//select")
    read_docname = (By.XPATH, "//tbody[@class='ui-sortable']//input[@placeholder='Enter Document Name']")
    read_choosefile = (By.XPATH, "//tbody[@class='ui-sortable']//input[@id='upload_file']")
    read_chusefile = (By.ID, "upload_file")
    attach_file = (By.XPATH, "(//a[contains(text(),'ATTACH')])[1]")
    choose_file = (By.XPATH, "//a[@id='upload_file_btn']")
    choose_file1 = (By.XPATH, "//input[@id='upload_file']")
    choose_file_direct = (By.XPATH, "(//input[contains(@id,'upload_file_')])[1]")
    read_mandatory = (By.XPATH, "//tbody[@class='ui-sortable']//select[@name='mandatory[]']")
    provide_selname = (By.XPATH, "//tbody[@class='ui-sortable']//select[@id='glossary']")
    provide_chusfile = (By.XPATH, "//tbody[@class='ui-sortable']//input[@name='ex_files[]']")
    provide_mandatory = (By.XPATH, "//tbody[@class='ui-sortable']//select[@name='mandatory[]']")
    provide_expiration = (By.XPATH, "//tbody[@class='ui-sortable']//select[@name='exp_date_req[]']")
    button_savechanges = (By.XPATH, "//button[@class='btn btn-primary']")

    veri_docname = (By.XPATH, "//form[@id='edit_requirements']//tr[1]//td[2]/input")
    veri_filename = (By.XPATH, "//form[@id='edit_requirements']//tr[1]//td[3]")
    veri_mand = (By.XPATH, "//form[@id='edit_requirements']//tr[1]//td[6]//b[1]")

    veri_docname_up = (By.XPATH, "//form[@id='edit_requirements']//tr[2]//td[2]/input")
    veri_filename_up = (By.XPATH, "//form[@id='edit_requirements']//tr[2]//td[3]")
    veri_mand_up = (By.XPATH, "//form[@id='edit_requirements']//tr[2]//td[6]//b[1]")
    veri_docdate_up = (By.XPATH, "//form[@id='edit_requirements']//tr[2]//td[5]//b[1]")

    log_out = (By.XPATH, "//a[contains(text(),'Logout')]")
    save_change = (By.XPATH, "//button[contains(text(),'Save Changes')]")
    input_documentname = (By.XPATH, "//tbody[@class='ui-sortable']//input[@placeholder='Document Name']")
    # read_attachBtn = (By.XPATH, "//tbody[@class='ui-sortable']//td[input[@placeholder='Enter Document Name']]/following-sibling::td[1]/a")
    # read_attachBtn = (By.XPATH, "(//a[contains(text(),'ATTACH')])[1]")
    read_attachBtn = (By.XPATH, "//table[@id='req_files']//a[contains(text(),'ATTACH')]")
    # provide_attachBtn = (By.XPATH, "//tbody[@class='ui-sortable']//td[div[input[@placeholder='Document Name']]]/following-sibling::td[2]/a")
    # provide_attachBtn = (By.XPATH, "(//a[contains(text(),'ATTACH')])[1]")
    provide_attachBtn = (By.XPATH, "//table[@id='req_files']//a[contains(text(),'ATTACH')]")


    def __init__(self, browser):
        self.browser = browser

    @allure.step('Clicking on I Agree button to move forward')
    def click_iagree_button(self):
        self.browser.find_element(*self.hosp_agreement).click()

    @allure.step('Clicking tab -> My Discipline')
    def click_tab_mydiscipline(self):
        self.browser.find_element(*self.hosp_mydiscipline).click()

    @allure.step('Clicking button -> Edit student requirement')
    def click_editstudentReq(self):
        self.browser.find_element(*self.hosp_edithospReq).click()

    @allure.step('Select Read orientation agenda from dropdown')
    def select_read_document(self):
        sel = Select(self.browser.find_element(*self.disc_selectdocument))
        sel.select_by_visible_text("Read, ex: orientation agenda")

    @allure.step('Entering name for read document')
    def enter_read_docname(self, docname):
        self.browser.find_element(*self.read_docname).send_keys(docname)

    @allure.step('Choose .pdf file for read document')
    def choose_read_file(self):
        # self.browser.find_element(*self.read_attachBtn).click()
        # time.sleep(8)
        # path = os.getcwd()+"\\resources\\sample.pdf"
 #       # self.browser.find_element(*self.choose_file1).send_keys(os.getcwd()+"\\resources\\sample.pdf")
        # self.browser.find_element(*self.choose_file).click()
        # time.sleep(4)  # waiting for window popup to open
        # pyautogui.write(path)  # path of File
        # pyautogui.press('enter')
        self.browser.find_element(*self.choose_file_direct).send_keys(os.getcwd() + "\\resources\\sample.pdf")

    @allure.step('Click on save changes button to upload file')
    def click_savechanges_uploadfile(self):
        # self.browser.find_element(*self.save_change).click()
        element = self.browser.find_element(*self.save_change)
        # self.browser.execute_script("arguments[0].click();", element)
        ActionChains(self.browser).move_to_element(element).click(element).perform()

    @allure.step('Select Yes from mandatory in read document')
    def select_read_mandatory(self, verify):
        ele = Select(self.browser.find_element(*self.read_mandatory))
        ele.select_by_visible_text(verify)

    @allure.step('Clicking button save changes')
    def click_buttonSavechange(self):
        self.browser.find_element(*self.button_savechanges).click()

    def page_refresh(self):
        self.browser.refresh()


    @allure.step('Select Provide ex: confidentiality agreement from dropdown')
    def select_document(self):
        sel = Select(self.browser.find_element(*self.disc_selectdocument))
        sel.select_by_visible_text("Provide, ex: Confidentiality Agreement, Drug Screening, CPR License")

    @allure.step('Select requirement created in use case A5 in the drop down')
    def select_provide_document(self, verify):
        selec = Select(self.browser.find_element(*self.provide_selname))
        selec.select_by_visible_text(verify)

    @allure.step('Enter requirement created in use case A5')
    def enter_document_name(self, reqName):
        self.browser.find_element(*self.input_documentname).send_keys(reqName)

    @allure.step('Choose .pdf file for provide document ')
    def choose_provide_file(self):
        # self.browser.find_element(*self.provide_attachBtn).click()
        # time.sleep(4)
        # path = os.getcwd()+"\\resources\\sample.pdf"
        # # self.browser.find_element(*self.choose_file1).send_keys(os.getcwd()+"\\resources\\sample.pdf")
        # self.browser.find_element(*self.choose_file).click()
        # time.sleep(4)  # waiting for window popup to open
        # pyautogui.write(path)  # path of File
        # pyautogui.press('enter')
        self.browser.find_element(*self.choose_file_direct).send_keys(os.getcwd() + "\\resources\\sample.pdf")

    @allure.step('Select Yes for doc expiration date')
    def select_doc_expirationdate(self, verify):
        date = Select(self.browser.find_element(*self.provide_expiration))
        date.select_by_visible_text(verify)

    @allure.step('Select yes for mandatory in provide document')
    def select_provide_mandatory(self, verify):
        man = Select(self.browser.find_element(*self.provide_mandatory))
        man.select_by_visible_text(verify)

    @allure.step("Verify document name for read")
    def verify_document_name(self):
        # return self.browser.find_element(*self.veri_docname).text
        msg = self.browser.find_element(*self.veri_docname).get_attribute('value')
        return msg

    @allure.step("Verify file name for read")
    def verify_file_name(self):
        return self.browser.find_element(*self.veri_filename).text

    @allure.step("Verify mandatory type for read")
    def verify_mandatory(self):
        return self.browser.find_element(*self.veri_mand).text

    @allure.step("Verify document name for provide")
    def verify_document_name_upl(self):
        msg = self.browser.find_element(*self.veri_docname_up).get_attribute('value')
        return msg

    @allure.step("Verify mandatory type for provide")
    def verify_mandatory_upl(self):
        return self.browser.find_element(*self.veri_mand_up).text

    @allure.step("Verify document expiration type for provide")
    def verify_docdate_upl(self):
        return self.browser.find_element(*self.veri_docdate_up).text

    @allure.step("Click tab -> logout")
    def click_logout_button(self):
        self.browser.find_element(*self.log_out).click()