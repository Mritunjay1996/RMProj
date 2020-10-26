import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import allure

class HelpPage:
    iframe_faqs = (By.XPATH, "//div[@class='content']//iframe")
    faq_folder1 = (By.XPATH, "//ul[@id='kb']/li[1]//a")
    faq_folder2 = (By.XPATH, "//ul[@id='kb']/li[2]//a")
    faq_folder3 = (By.XPATH, "//ul[@id='kb']/li[3]//a")
    faq_folder_heading = (By.XPATH, "//div[@id='content']/h1/strong")
    link_goBack = (By.XPATH, "//a[@class='back']")
    option_Tutorial = (By.XPATH, "//li/a[text()='Tutorial']")
    button_newTicket = (By.XPATH, "//div[@id='new_ticket']//a")
    input_phone = (By.XPATH, "//input[@id='phone']")
    input_ext = (By.XPATH, "//input[@id='ext']")
    dropdown_helpTopic = (By.XPATH, "//select[@id='topicId']")
    input_subject = (By.XPATH, "//input[@id='subject']")
    textarea_message = (By.XPATH, "//textarea[@id='issue']")
    button_createTicket = (By.XPATH, "//button[@id='submit']")
    label_ticketNumber = (By.XPATH, "//div[contains(@class,'alert-success')]")
    input_searchTicket = (By.XPATH, "//input[@id='basic-ticket-search']")
    button_search = (By.XPATH, "//input[@name='basic_search']")
    link_ticket = (By.XPATH, "//a[@title='Preview Ticket']/b")
    label_ticketName = (By.XPATH, "//th[text()='Name:']/following-sibling::td[1]")
    label_ticketEmail = (By.XPATH, "//th[text()='Email:']/following-sibling::td[1]")
    label_ticketHelpTopic = (By.XPATH, "//th[text()='Help Topic:']/following-sibling::td[1]")
    label_ticketSubject = (By.XPATH, "//ul[@id='threads']/preceding-sibling::h2[1]")
    label_ticketMessage = (By.XPATH, "//table[@class='message']//tr[2]/td")
    faq_heading = (By.XPATH, "//div[@class='content']//h2")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Verifying the message on the ticket')
    def verify_ticketMessage(self):
        msg = self.browser.find_element(*self.label_ticketMessage).text
        return msg.strip()

    @allure.step('Verifying the Subject on the ticket')
    def verify_ticketSubject(self):
        msg = self.browser.find_element(*self.label_ticketSubject).text
        return msg.strip()

    @allure.step('Verifying the help topic on the ticket')
    def verify_ticketHelpTopic(self):
        msg = self.browser.find_element(*self.label_ticketHelpTopic).text
        return msg.strip()

    @allure.step('Verifying the email on the ticket')
    def verify_ticketEmail(self):
        msg = self.browser.find_element(*self.label_ticketEmail).text
        return msg.strip()

    @allure.step('Verifying the name on the ticket')
    def verify_ticketName(self):
        msg = self.browser.find_element(*self.label_ticketName).text
        return msg.strip()

    @allure.step('Click on ticket')
    def click_ticket(self):
        self.browser.find_element(*self.link_ticket).click()

    @allure.step('Click on Search button')
    def click_search(self):
        self.browser.find_element(*self.button_search).click()

    @allure.step('Enter ticket number in search box')
    def enter_ticketNumber(self, tckt):
        self.browser.find_element(*self.input_searchTicket).send_keys(tckt)

    @allure.step('Saving the ticket number')
    def get_ticketNumber(self):
        ticket = self.browser.find_element(*self.label_ticketNumber).text
        return ticket.strip()

    @allure.step('Click on Create Ticket button')
    def click_CreateTicket(self):
        self.browser.find_element(*self.button_createTicket).click()

    @allure.step('Enter message')
    def enter_message(self, msg):
        self.browser.find_element(*self.textarea_message).send_keys(msg)

    @allure.step('Enter subject')
    def enter_subject(self, subj):
        self.browser.find_element(*self.input_subject).send_keys(subj)

    @allure.step('Select help topic')
    def select_helpTopic(self, topic):
        select = Select(self.browser.find_element(*self.dropdown_helpTopic))
        select.select_by_visible_text(topic)

    @allure.step('Enter extension number')
    def enter_ext(self, ext):
        self.browser.find_element(*self.input_ext).send_keys(ext)

    @allure.step('Enter phone number')
    def enter_phone(self, ph):
        self.browser.find_element(*self.input_phone).send_keys(ph)

    @allure.step('Click on New Ticket button')
    def click_NewTicket(self):
        self.browser.find_element(*self.button_newTicket).click()

    @allure.step('Validate the Call Me Back page loads')
    def validateCallMeBack(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
        return self.browser.title

    @allure.step('Validate FAQ page loads')
    def validateFAQ(self):
        return self.browser.find_element(*self.faq_heading).text

    @allure.step('Close the tab for Call Me Back')
    def closeCallMeBackTab(self):
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    @allure.step('Click on Go Back link')
    def click_goBack(self):
        self.browser.find_element(*self.link_goBack).click()

    @allure.step("Click Help -> Tutorial")
    def clickOptionTutorial(self):
        flag = False
        window_before = self.browser.window_handles[0]
        self.browser.find_element(*self.option_Tutorial).click()
        time.sleep(5)
        try:
            window_after = self.browser.window_handles[1]
            self.browser.switch_to.window(window_after)
            flag = True
        except:
            flag = False
        self.browser.close()
        self.browser.switch_to.window(window_before)
        return flag


    @allure.step('Verifying FAQ Folder loaded correctly')
    def verify_faqFolder_heading(self):
        return self.browser.find_element(*self.faq_folder_heading).text

    @allure.step('Switching to iframe')
    def switchTo_iframe_faqs(self):
        self.browser.switch_to.frame(self.browser.find_element(*self.iframe_faqs))

    @allure.step('Switching back to default content')
    def switchTo_defaultContent(self):
        self.browser.switch_to.default_content()

    @allure.step('Click on FAQ folder - 1')
    def click_faqFolder1(self):
        self.browser.find_element(*self.faq_folder1).click()

    @allure.step('Click on FAQ folder - 2')
    def click_faqFolder2(self):
        self.browser.find_element(*self.faq_folder2).click()

    @allure.step('Click on FAQ folder - 3')
    def click_faqFolder3(self):
        self.browser.find_element(*self.faq_folder3).click()