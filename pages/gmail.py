from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import os
import allure
import time

class gmailPage:
    input_username = (By.XPATH, "//input[@id='identifierId']")
    button_next_username = (By.XPATH, "//div[@id='identifierNext']")
    input_password = (By.XPATH, "//input[@type='password']")
    button_next_password = (By.XPATH, "//div[@id='passwordNext']")
    email_rotationApproved = (By.XPATH, "//a[contains(text(),'Rotation was Approved')]")
    # email_rotationDeclined = (By.XPATH, "//a[b[text()='Rotation Manager']]")
    email_rotationDeclined = (By.XPATH, "//a[contains(text(),'Rotation Manager')]")
    # subject_rotationApproved = (By.XPATH, "//div[@class='messageHeader']/b")
    subject_rotationApproved = (By.XPATH, "//td[contains(text(),'Subject:')]/following-sibling::td[1]/b")
    # emailText_rotationApproved = (By.XPATH, "//div[@id='body']")
    emailText_rotationApproved = (By.XPATH, "//body")
    link_more = (By.XPATH, "//a[text()='More >']")
    link_showQuotedText = (By.XPATH, "//a[text()='Show quoted text']")
    email_back = (By.XPATH, "//div[@class='preamble']//tr/td[1]//a")
    checkbox_selectEmail = (By.XPATH, "//input[@type='checkbox']")
    button_delete = (By.XPATH, "//input[@value='Delete']")
    iframe_emailbody = (By.XPATH,"//iframe[@id='msg_body']")

    # for mailinator
    homepage_searchbox = (By.XPATH, "//input[@id='addOverlay']")
    homepage_button_go = (By.XPATH, "//button[@id='go-to-public']")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Open Mailinator inbox in new Tab')
    def open_mailbox(self, email):
        self.browser.execute_script(
            '''window.open("https://www.mailinator.com/","_blank");''')
        self.browser.switch_to.window(self.browser.window_handles[1])
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(self.homepage_searchbox))
        self.browser.find_element(*self.homepage_searchbox).send_keys(email)
        self.browser.find_element(*self.homepage_button_go).click()


    @allure.step('Deleting an previous old emails')
    def delete_emails(self):
        self.browser.find_element(*self.email_back).click()
        mails = self.browser.find_elements(*self.checkbox_selectEmail)
        if len(mails) != 0:
            for element in self.browser.find_elements(*self.checkbox_selectEmail):
                element.click()
            self.browser.find_element(*self.button_delete).click()

    # @allure.step('Verifying email text for rotation email')
    # def verify_emailText_rotationApproved(self):
    #     msg = self.browser.find_element(*self.emailText_rotationApproved).text
    #     msg = msg.replace('\n',' ')
    #     return msg

    @allure.step('Verifying email text for rotation email')
    def verify_emailText_rotationApproved(self):
        time.sleep(5)
        ifr = self.browser.find_element(*self.iframe_emailbody)
        self.browser.switch_to.frame(ifr)
        time.sleep(2)
        msg = self.browser.find_element(*self.emailText_rotationApproved).text
        msg = msg.replace('\n', ' ')
        print(msg)
        self.browser.switch_to.default_content()
        return msg


    @allure.step('Verifying subject for rotation email')
    def verify_subject_rotationApproved(self):
        return self.browser.find_element(*self.subject_rotationApproved).text

    # @allure.step('Open email for declined rotation')
    # def open_email_rotationDeclined(self):
    #     self.browser.find_element(*self.email_rotationDeclined).click()
    #     try:
    #         self.browser.find_element(*self.link_more).click()
    #         self.browser.find_element(*self.link_showQuotedText).click()
    #     except:
    #         pass

    @allure.step('Open email for declined rotation')
    def open_email_rotationDeclined(self):
        self.browser.find_element(*self.email_rotationDeclined).click()
        try:
            self.browser.find_element(*self.link_more).click()
            self.browser.find_element(*self.link_showQuotedText).click()
        except:
            pass

    @allure.step('Open email for approved rotation')
    def open_email_rotationApproved(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.email_rotationApproved))
        self.browser.find_element(*self.email_rotationApproved).click()
        # try:
        #     self.browser.find_element(*self.link_more).click()
        #     self.browser.find_element(*self.link_showQuotedText).click()
        # except:
        #     pass

    @allure.step('Login to Gmail')
    def login_gmail(self, usrnm, pswrd):
        # user_agent = self.browser.execute_script("return navigator.userAgent;")
        # print(user_agent)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.input_username))
        self.browser.find_element(*self.input_username).send_keys(usrnm)
        self.browser.find_element(*self.button_next_username).click()
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.input_password))
        time.sleep(5)
        self.browser.find_element(*self.input_password).send_keys(pswrd)
        self.browser.find_element(*self.button_next_password).click()
        time.sleep(10)
        self.browser.get("http://m.gmail.com")
        time.sleep(3)

    @allure.step('Switching to Gmail mobile site')
    def switch_mobile_gmail(self):
        self.browser.get("http://m.gmail.com")
        time.sleep(3)

    @allure.step('Open Gmail in new Tab')
    def open_gmail(self):
        # self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        # ActionChains(self.browser).key_down(Keys.LEFT_CONTROL).send_keys('t').key_up(Keys.LEFT_CONTROL).perform()
        # self.browser.execute_script('''window.open("http://m.gmail.com","_blank");''')
        self.browser.execute_script('''window.open("https://accounts.google.com/AccountChooser?service=mail&amp;continue=https://mail.google.com/mail/","_blank");''')
        self.browser.switch_to.window(self.browser.window_handles[1])

    @allure.step('Close Gmail')
    def close_gmail(self):
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])
        # ActionChains(self.browser).key_down(Keys.CONTROL).send_keys('w').key_up(Keys.CONTROL).perform()
        # self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')