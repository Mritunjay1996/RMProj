"""
This module contains web test cases for the trial.
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""

import pytest, time, random, allure
from datetime import datetime, timedelta
from pages.homepage import homepageObjects
from pages.registrationPage import registrationPage
from pages.schoolFiles import schoolFilesPage
from pages.myAccount import myAccountPage
from pages.admin_crm import adminCRMObj
from pages.admin_hospitals import adminHospitalObj
from resources.variables import *
from pages.admin_hospital_requirement import adminhospitalreqObj
from pages.hospuser_create_hospreq import hospusercreatehospreqObj
from pages.admin_hospital_users import adminHospitalUsersObj
from pages.adminsets_school_price import adminsetsschoolpriceObj
from pages.adminsets_school_licenses import adminsetsschoollicensesObj
from pages.school_schoolFiles import school_schoolFilesPage
from pages.studentHelp import HelpPage
from pages.school_myRotations import school_myRotationsPage
from pages.gmail import gmailPage
from pages.hospuser_customize_units import customizeUnits
from pages.school_myStudents import school_myStudentsPage
from pages.hospuser_myRotations import hosp_myRotationsPage
from pages import gmailApi
from pages import deleteApi
import importlib

rotationNumber = ""
rotation_h5 = ""
rotation_h6 = ""
rotation_h10 = ""


@allure.title('A1: Admin creates a school and a school user')
def test_admin_create_school_and_crm(browser):
    home_page = homepageObjects(browser)
    crm_page = adminCRMObj(browser)
    print(randNum)
    counter = 1
    while True:
        home_page.load()
        time.sleep(4)
        home_page.enterUsername(admin_username)
        home_page.enterPassword(admin_password)
        home_page.clickLogin()
        time.sleep(10)
        crm_page.click_tab_crm()
        print("Five")
        crm_page.click_crm_create()
        crm_page.enter_firstname_crm(crm_firstname)
        crm_page.enter_lastname_crm(crm_lastname)
        crm_page.enter_schoolname_crm(school_name)
        crm_page.enter_campusname_crm(campus_name)
        crm_page.enter_disciplinename_crm(discipline_name)
        crm_page.enter_phone_crm(phone_number)
        crm_page.enter_email_crm(crm_email)
        crm_page.enter_password_crm(crm_password)
        crm_page.click_submit()
        time.sleep(5)
        if crm_page.verify_crm_creation_school() == school_name:
            break
        crm_page.enter_email_crm(randNum + str(counter) + "@xyz.com")
        counter = counter + 1
        crm_page.click_save()
        time.sleep(6)
    # assert crm_page.verify_crm_creation_message() == "CRM was Created Sucessfully!!!", "CRM not created. Success message is not displayed."
    assert crm_page.verify_crm_creation_email() == crm_email, "Login: " + crm_page.verify_crm_creation_email() + \
                                                              " is wrong for the created CRM. Instead email should be " + crm_email
    assert crm_page.verify_crm_creation_firstname() == crm_firstname, "First name: " + crm_page.verify_crm_creation_firstname() + \
                                                                      " is wrong for the created CRM. Instead first name should be " + crm_firstname
    assert crm_page.verify_crm_creation_lastname() == crm_lastname, "Last name: " + crm_page.verify_crm_creation_lastname() + \
                                                                    " is wrong for the created CRM. Instead last name should be " + crm_lastname
    assert crm_page.verify_crm_creation_school() == school_name, "School name: " + crm_page.verify_crm_creation_school() + \
                                                                 " is wrong for the created CRM. Instead school name should be " + school_name
    assert crm_page.verify_crm_creation_campus() == campus_name, "Campus name: " + crm_page.verify_crm_creation_campus() + \
                                                                 " is wrong for the created CRM. Instead campus name should be " + campus_name
    assert crm_page.verify_crm_creation_discipline() == discipline_name, "Discipline name: " + crm_page.verify_crm_creation_discipline() + \
                                                                         " is wrong for the created CRM. Instead discipline name should be " \
                                                                         + discipline_name
    assert crm_page.verify_crm_creation_phone() == phone_number, "Phone number: " + crm_page.verify_crm_creation_phone() + \
                                                                 " is wrong for the created CRM. Instead phone number should be " + phone_number
    assert crm_page.verify_crm_creation_email() == crm_email, "Email: " + crm_page.verify_crm_creation_email() + \
                                                              " is wrong for the created CRM. Instead email should be " + crm_email
    assert crm_page.verify_crm_creation_shadowing() == 'OFF', "Shadowing CRM option: " + crm_page.verify_crm_creation_shadowing() + \
                                                              " is wrong for the created CRM. Instead option should be OFF"
    # assert crm_page.verify_crm_creation_ccemail() == 'OFF', "CC Email option: " + crm_page.verify_crm_creation_ccemail() + \
    #                                                         " is wrong for the created CRM. Instead option should be OFF"


@allure.title('A2: Admin creates a hospital and links first school to it')
def test_admin_create_hospital(browser):
    home_page = homepageObjects(browser)
    hosp_obj = adminHospitalObj(browser)
    hosp_obj.click_tab_hospital()
    hosp_obj.click_hospitals_create()
    hosp_obj.enter_hospital_name(hospital_name)
    hosp_obj.enter_discipline1(discipline1)
    hosp_obj.enter_discipline1_speciality1(discipline1_speciality1)
    hosp_obj.enter_discipline1_speciality2(discipline1_speciality2)
    hosp_obj.enter_discipline2(discipline2)
    hosp_obj.enter_discipline2_speciality1(discipline2_speciality1)
    hosp_obj.enter_discipline2_speciality2(discipline2_speciality2)
    hosp_obj.select_school(school_name + " - " + campus_name + " - " + discipline_name)
    hosp_obj.click_submit()
    time.sleep(15)
    assert hosp_obj.verify_hospital_creation() == "Edit Hospital", "Hospital object is not created."
    assert hosp_obj.verify_hospital_creation_hospitalname() == hospital_name, \
        "Hospital name: " + hosp_obj.verify_hospital_creation_hospitalname() + \
        " is wrong for the created Hospital. Instead hospital name should be " + hospital_name
    assert hosp_obj.verify_hospital_creation_discipline1() == discipline1, \
        "Discipline1: " + hosp_obj.verify_hospital_creation_discipline1() + \
        " is wrong for the created Hospital. Instead discipline1 should be " + discipline1
    assert hosp_obj.verify_hospital_creation_discipline2() == discipline2, \
        "Discipline2: " + hosp_obj.verify_hospital_creation_discipline2() + \
        " is wrong for the created Hospital. Instead discipline2 should be " + discipline2
    assert hosp_obj.verify_hospital_creation_discipline1speciality1() == discipline1_speciality1, \
        "Discipline1 - Speciality1: " + hosp_obj.verify_hospital_creation_discipline1speciality1() + \
        " is wrong for the created Hospital. Instead discipline1 - speciality1 should be " + discipline1_speciality1
    assert hosp_obj.verify_hospital_creation_discipline1speciality2() == discipline1_speciality2, \
        "Discipline1 - Speciality2: " + hosp_obj.verify_hospital_creation_discipline1speciality2() + \
        " is wrong for the created Hospital. Instead discipline1 - speciality2 should be " + discipline1_speciality2
    assert hosp_obj.verify_hospital_creation_discipline2speciality1() == discipline2_speciality1, \
        "Discipline2 - Speciality1: " + hosp_obj.verify_hospital_creation_discipline2speciality1() + \
        " is wrong for the created Hospital. Instead discipline2 - speciality1 should be " + discipline2_speciality1
    assert hosp_obj.verify_hospital_creation_discipline2speciality2() == discipline2_speciality2, \
        "Discipline2 - Speciality2: " + hosp_obj.verify_hospital_creation_discipline2speciality2() + \
        " is wrong for the created Hospital. Instead discipline2 - speciality2 should be " + discipline2_speciality2
    assert hosp_obj.verify_hospital_creation_disc1shadowing() == "OFF", \
        "Discipline1 - Shadowing: " + hosp_obj.verify_hospital_creation_disc1shadowing() + \
        " is wrong for the created Hospital. Instead discipline1 - shadowing should be OFF"
    assert hosp_obj.verify_hospital_creation_disc1scheduler() == "OFF", \
        "Discipline1 - Scheduler: " + hosp_obj.verify_hospital_creation_disc1scheduler() + \
        " is wrong for the created Hospital. Instead discipline1 - scheduler should be OFF"
    assert hosp_obj.verify_hospital_creation_disc1approval() == "Yes", \
        "Discipline1 - Approval: " + hosp_obj.verify_hospital_creation_disc1approval() + \
        " is wrong for the created Hospital. Instead discipline1 - approval should be Yes"
    assert hosp_obj.verify_hospital_creation_disc2shadowing() == "OFF", \
        "Discipline2 - Shadowing: " + hosp_obj.verify_hospital_creation_disc2shadowing() + \
        " is wrong for the created Hospital. Instead discipline2 - shadowing should be OFF"
    assert hosp_obj.verify_hospital_creation_disc2scheduler() == "OFF", \
        "Discipline2 - Scheduler: " + hosp_obj.verify_hospital_creation_disc2scheduler() + \
        " is wrong for the created Hospital. Instead discipline2 - scheduler should be OFF"
    assert hosp_obj.verify_hospital_creation_disc2approval() == "Yes", \
        "Discipline2 - Approval: " + hosp_obj.verify_hospital_creation_disc2approval() + \
        " is wrong for the created Hospital. Instead discipline2 - approval should be Yes"


@allure.title('A3: Admin edits hospital structure')
def test_admin_edits_hospital(browser):
    home_page = homepageObjects(browser)
    hosp_obj = adminHospitalObj(browser)
    hosp_obj.select_discipline1_shadowing("ON")
    hosp_obj.select_discipline1_scheduler("ON")
    hosp_obj.select_discipline1_approval("No")
    hosp_obj.edit_discipline1_speciality(discipline1_speciality1, discipline1_speciality2)
    hosp_obj.add_discipline1_location("1234567")
    hosp_obj.click_save_changes()
    time.sleep(15)
    assert hosp_obj.verify_hospital_creation_hospitalname() == hospital_name, \
        "Hospital name: " + hosp_obj.verify_hospital_creation_hospitalname() + \
        " is wrong for the created Hospital. Instead hospital name should be " + hospital_name
    assert hosp_obj.verify_hospital_creation_discipline1() == discipline1, \
        "Discipline1: " + hosp_obj.verify_hospital_creation_discipline1() + \
        " is wrong for the created Hospital. Instead discipline1 should be " + discipline1
    assert hosp_obj.verify_hospital_creation_discipline2() == discipline2, \
        "Discipline2: " + hosp_obj.verify_hospital_creation_discipline2() + \
        " is wrong for the created Hospital. Instead discipline2 should be " + discipline2
    assert hosp_obj.verify_hospital_creation_discipline1speciality1() == discipline1_speciality1 + " edited", \
        "Discipline1 - Speciality1: " + hosp_obj.verify_hospital_creation_discipline1speciality1() + \
        " is wrong for the created Hospital. Instead discipline1 - speciality1 should be " + discipline1_speciality1 + " edited"
    assert hosp_obj.verify_hospital_creation_discipline1speciality2() == discipline1_speciality2 + " edited", \
        "Discipline1 - Speciality2: " + hosp_obj.verify_hospital_creation_discipline1speciality2() + \
        " is wrong for the created Hospital. Instead discipline1 - speciality2 should be " + discipline1_speciality2 + " edited"
    assert hosp_obj.verify_hospital_creation_discipline2speciality1() == discipline2_speciality1, \
        "Discipline2 - Speciality1: " + hosp_obj.verify_hospital_creation_discipline2speciality1() + \
        " is wrong for the created Hospital. Instead discipline2 - speciality1 should be " + discipline2_speciality1
    assert hosp_obj.verify_hospital_creation_discipline2speciality2() == discipline2_speciality2, \
        "Discipline2 - Speciality2: " + hosp_obj.verify_hospital_creation_discipline2speciality2() + \
        " is wrong for the created Hospital. Instead discipline2 - speciality2 should be " + discipline2_speciality2
    assert hosp_obj.verify_hospital_creation_disc1shadowing() == "ON", \
        "Discipline1 - Shadowing: " + hosp_obj.verify_hospital_creation_disc1shadowing() + \
        " is wrong for the created Hospital. Instead discipline1 - shadowing should be ON"
    assert hosp_obj.verify_hospital_creation_disc1scheduler() == "ON", \
        "Discipline1 - Scheduler: " + hosp_obj.verify_hospital_creation_disc1scheduler() + \
        " is wrong for the created Hospital. Instead discipline1 - scheduler should be ON"
    assert hosp_obj.verify_hospital_creation_disc1approval() == "No", \
        "Discipline1 - Approval: " + hosp_obj.verify_hospital_creation_disc1approval() + \
        " is wrong for the created Hospital. Instead discipline1 - approval should be No"
    assert hosp_obj.verify_hospital_creation_disc2shadowing() == "OFF", \
        "Discipline2 - Shadowing: " + hosp_obj.verify_hospital_creation_disc2shadowing() + \
        " is wrong for the created Hospital. Instead discipline2 - shadowing should be OFF"
    assert hosp_obj.verify_hospital_creation_disc2scheduler() == "OFF", \
        "Discipline2 - Scheduler: " + hosp_obj.verify_hospital_creation_disc2scheduler() + \
        " is wrong for the created Hospital. Instead discipline2 - scheduler should be OFF"
    assert hosp_obj.verify_hospital_creation_disc2approval() == "Yes", \
        "Discipline2 - Approval: " + hosp_obj.verify_hospital_creation_disc2approval() + \
        " is wrong for the created Hospital. Instead discipline2 - approval should be Yes"
    assert hosp_obj.verify_hospital_creation_discipline1location() == "1234567", \
        "Discipline1 - Location: " + hosp_obj.verify_hospital_creation_discipline1location() + \
        " is wrong for the created Hospital. Instead discipline1 - location should be 1234567"
    hosp_obj.click_addRow()
    hosp_obj.enter_discipline3(discipline3)
    hosp_obj.enter_discipline3_speciality1(discipline3_speciality1)
    hosp_obj.enter_discipline3_speciality2(discipline3_speciality2)
    hosp_obj.click_addRow()
    hosp_obj.enter_discipline4(discipline4)
    hosp_obj.select_discipline4_shadowing("ON")
    hosp_obj.enter_discipline4_speciality1(discipline4_speciality1)
    hosp_obj.enter_discipline4_speciality2(discipline4_speciality2)
    hosp_obj.select_discipline1_shadowing("OFF")
    hosp_obj.select_discipline1_scheduler("OFF")
    time.sleep(3)
    hosp_obj.click_save_changes()
    hosp_obj.select_discipline3_scheduler("ON")
    hosp_obj.add_discipline3_location("112233")
    time.sleep(3)
    hosp_obj.click_save_changes()
    time.sleep(5)


@allure.title('A4: Admin creates hospital user and puts school under management of this new user')
def test_admin_create_hospitalUser(browser):
    home_page = homepageObjects(browser)
    hospUser_obj = adminHospitalUsersObj(browser)
    hospUser_obj.click_tab_hospitalUsers()
    hospUser_obj.click_hospitalUsers_create()
    hospUser_obj.hospital_select(hospital_name)
    hospUser_obj.enter_firstname(hospUser_firstname)
    hospUser_obj.enter_lastname(hospUser_lastname)
    hospUser_obj.enter_phone(phone_number)
    hospUser_obj.enter_email(hospUser_email)
    hospUser_obj.select_receiveEmail_no()
    hospUser_obj.select_cancelRotations_yes()
    hospUser_obj.select_editRotations_no()
    hospUser_obj.enter_password(hospUser_password)
    hospUser_obj.click_submit()
    time.sleep(10)
    assert hospUser_obj.verify_login_username() == hospUser_email, \
        "Login username: " + hospUser_obj.verify_login_username() + \
        " is wrong for the created Hospital User. Instead hospital user name should be " + hospUser_email
    assert hospUser_obj.verify_hospital_name() == hospital_name, \
        "Associated hospital name: " + hospUser_obj.verify_hospital_name() + \
        " is wrong for the created Hospital User. Instead hospital name should be " + hospital_name
    assert hospUser_obj.verify_firstname() == hospUser_firstname, \
        "First name: " + hospUser_obj.verify_firstname() + \
        " is wrong for the created Hospital User. Instead first name should be " + hospUser_firstname
    assert hospUser_obj.verify_lastname() == hospUser_lastname, \
        "Last name: " + hospUser_obj.verify_lastname() + \
        " is wrong for the created Hospital User. Instead last name should be " + hospUser_lastname
    assert hospUser_obj.verify_phone() == phone_number, \
        "Phone number: " + hospUser_obj.verify_phone() + \
        " is wrong for the created Hospital User. Instead phone number should be " + phone_number
    assert hospUser_obj.verify_email() == hospUser_email, \
        "Email: " + hospUser_obj.verify_email() + \
        " is wrong for the created Hospital User. Instead email should be " + hospUser_email
    assert hospUser_obj.verify_receiveEmails_no() == True, \
        "Receive Emails: Yes is wrong for the created Hospital User. Instead it should be No"
    assert hospUser_obj.verify_cancelRotations_yes() == True, \
        "Cancel Rotations: No is wrong for the created Hospital User. Instead it should be Yes"
    assert hospUser_obj.verify_editRotations_no() == True, \
        "Edit Rotations: Yes is wrong for the created Hospital User. Instead it should be No"
    hospUser_obj.add_discipline(hospital_name + " - " + discipline1)
    hospUser_obj.add_school(school_name + " - " + campus_name + " - " + discipline_name)
    time.sleep(3)
    hospUser_obj.add_discipline(hospital_name + " - " + discipline2)
    time.sleep(3)
    hospUser_obj.click_save_changes()
    time.sleep(10)
    assert hospUser_obj.verify_managed_discipline() == hospital_name + " - " + discipline1, \
        "Managed discipline: " + hospUser_obj.verify_managed_discipline() + \
        " is wrong for the created Hospital User. Instead managed discipline should be " + hospital_name + " - " + discipline1
    assert hospUser_obj.verify_managed_school() == school_name + " - " + campus_name + " - " + discipline_name, \
        "Managed school: " + hospUser_obj.verify_managed_school() + \
        " is wrong for the created Hospital User. Instead managed school should be " + school_name + " - " + campus_name + " - " + discipline_name


@allure.title('A5: Admin creates a hospital requirement')
def test_admin_manage_requirement(browser):
    home_page = homepageObjects(browser)
    req_page = adminhospitalreqObj(browser)
    req_page.click_tab_manage()
    req_page.click_manage_requirement()
    req_page.enter_reqName(manage_reqName)
    req_page.enter_shortForm(manage_shortForm)
    req_page.enter_description(manage_description)
    req_page.click_buttonReq()
    req_page.click_okButton()
    req_page.enter_reqName(multiple_reqName)
    req_page.enter_shortForm(multiple_shortForm)
    req_page.enter_description(multiple_description)
    req_page.click_buttonReq()
    req_page.click_okButton()
    req_page.search_filter(manage_reqName)
    assert req_page.verify_requirementName() == manage_reqName, "Manage requiremenet : " + req_page.verify_requirementName() + \
                                                                " is wrong Instead Requirement name should be " + manage_reqName
    assert req_page.verify_requirementShortForm() == manage_shortForm, "Manage requirement short name : " + req_page.verify_requirementShortForm() + \
                                                                       " is wrong Instead Requirement name should be " + manage_shortForm
    req_page.click_logout_button()


@allure.title('H1: Hospital User Creates Hospital Requirement')
def test_hospital_user_creathospReq(browser):
    home_page = homepageObjects(browser)
    hosp_user = hospusercreatehospreqObj(browser)
    home_page.enterUsername(hospUser_email)
    home_page.enterPassword(hospUser_password)
    home_page.clickLogin()
    hosp_user.click_iagree_button()
    hosp_user.click_tab_mydiscipline()
    hosp_user.click_editstudentReq()
    time.sleep(5)
    hosp_user.select_read_document()
    time.sleep(3)
    hosp_user.enter_read_docname(read_document_name)
    time.sleep(3)
    hosp_user.choose_read_file()
    # hosp_user.click_savechanges_uploadfile()
    time.sleep(2)
    hosp_user.select_read_mandatory(read_mand)
    hosp_user.click_buttonSavechange()
    time.sleep(2)
    hosp_user.select_document()
    # hosp_user.select_provide_document(manage_reqName)
    hosp_user.enter_document_name(manage_reqName)
    time.sleep(2)
    hosp_user.choose_provide_file()
    # hosp_user.click_savechanges_uploadfile()
    time.sleep(2)
    hosp_user.select_doc_expirationdate(read_mand)
    hosp_user.select_provide_mandatory(read_mand)
    hosp_user.click_buttonSavechange()
    time.sleep(2)
    hosp_user.select_document()
    # hosp_user.select_provide_document(multiple_reqName)
    hosp_user.enter_document_name(multiple_reqName)
    time.sleep(2)
    hosp_user.choose_provide_file()
    time.sleep(3)
    # hosp_user.click_savechanges_uploadfile()
    time.sleep(3)
    hosp_user.select_doc_expirationdate("No")
    hosp_user.select_provide_mandatory(read_mand)
    hosp_user.click_buttonSavechange()
    time.sleep(2)
    hosp_user.click_tab_mydiscipline()
    hosp_user.click_editstudentReq()
    time.sleep(3)
    assert hosp_user.verify_document_name() == read_document_name, "Document name for read :" + hosp_user.verify_document_name() + \
                                                                   " is wrong . Instead Document name should be " + read_document_name
    assert hosp_user.verify_file_name() == "sample.pdf", "File name : " + hosp_user.verify_file_name() + \
                                                         " is wrong . File name should be sample.pdf"
    assert hosp_user.verify_mandatory() == read_mand, "Mandatory type is : " + hosp_user.verify_mandatory() + \
                                                      " However mandatory type should be " + read_mand
    assert hosp_user.verify_document_name_upl() == manage_reqName, "Document name for student provide : " + hosp_user.verify_document_name_upl() + \
                                                                   " is wrong. Instead Name should be " + manage_reqName
    assert hosp_user.verify_docdate_upl() == read_mand, "Document expiration is : " + hosp_user.verify_docdate_upl() + \
                                                        " However Type should be " + read_mand
    assert hosp_user.verify_mandatory_upl() == read_mand, "Mandatory type for student provide is : " + hosp_user.verify_mandatory_upl() + \
                                                          " However Mandatory type should be " + read_mand
    hosp_user.click_logout_button()


@allure.title('A6 : Admin sets school price')
def test_admin_set_school_price(browser):
    home_page = homepageObjects(browser)
    admin_price = adminsetsschoolpriceObj(browser)
    home_page.load()
    home_page.enterUsername(admin_username)
    home_page.enterPassword(admin_password)
    home_page.clickLogin()
    time.sleep(8)
    admin_price.click_tab_manage()
    admin_price.click_school_option()
    time.sleep(5)
    admin_price.select_school_list(school_discpline)
    admin_price.enter_register_price(school_price)
    admin_price.enter_register_period(subscription_period)
    admin_price.enter_renewal_price(renewal_price)
    admin_price.click_create_schoolprice()
    time.sleep(3)
    admin_price.enter_school_search(school_discpline)
    time.sleep(2)

    assert admin_price.verify_school_name() == school_discpline_assert, "School name " + admin_price.verify_school_name() + \
                                                                        " is wrong . School name should be : " + school_discpline_assert
    time.sleep(2)
    admin_price.click_edit_button()
    assert admin_price.verify_school_price() == school_price, "School price " + admin_price.verify_school_price() + \
                                                              "is wrong . Price should be " + school_price
    admin_price.click_logout_tab()
    time.sleep(4)
    admin_price.click_register_tab()
    admin_price.select_reg_school(school_campus_discipline)
    time.sleep(3)
    assert admin_price.verify_register_price() == school_price_assert, "School price in register page " + admin_price.verify_register_price() + \
                                                                       " is wrong . Price sgould be " + school_price
    time.sleep(2)


@allure.title('A7 : Admin sets school licenses')
def test_admin_school_licenses(browser):
    home_page = homepageObjects(browser)
    skul_lcns = adminsetsschoollicensesObj(browser)
    home_page.load()
    home_page.enterUsername(admin_username)
    home_page.enterPassword(admin_password)
    home_page.clickLogin()
    time.sleep(5)
    skul_lcns.click_tab_manage()
    time.sleep(3)
    skul_lcns.click_school_licenses_option()
    skul_lcns.click_add_new_button()
    time.sleep(3)
    skul_lcns.select_school_displine(school_discpline)
    skul_lcns.enter_number_license(num_of_license)
    skul_lcns.click_on_amount()
    time.sleep(2)
    skul_lcns.click_on_submit()
    time.sleep(4)
    skul_lcns.click_on_ok()
    time.sleep(4)
    assert skul_lcns.verify_license_name() == school_discpline, " License name in summary table : " + skul_lcns.verify_license_name() + \
                                                                " is wrong . Name should be " + school_discpline
    assert skul_lcns.verify_numof_license() == num_of_license, " Number of License in purchase : " + skul_lcns.verify_numof_license() + \
                                                               " is wrong . It should be :" + num_of_license
    assert skul_lcns.verify_subscription_period() == "2 Months", "Subscription period in purchase table: " + skul_lcns.verify_subscription_period() + \
                                                                 " is wrong. period should be 2 Months"


@allure.title('I1: Instructor creates an account')
def test_register_instructor(browser):
    home_page = homepageObjects(browser)
    register_page = registrationPage(browser)
    home_page.load()
    home_page.clickRegister()
    time.sleep(3)
    register_page.select_studentType("Instructor")
    register_page.enter_firstName(instructor_fname)
    register_page.enter_lastName(instructor_lname)
    register_page.selectSchoolCampusDiscipline(school_campus_discipline)
    register_page.enter_address("8262", "Main Street", "Massachusetts", "Quincy", "02169")
    register_page.enter_phoneNumber("2025551234")
    register_page.enter_email(instructor_email)
    register_page.enter_password(instructor_password)
    register_page.select_agreementCheckbox()
    register_page.click_submitButton()
    time.sleep(2)
    assert register_page.validate_successfulRegistration() == True, "Registration of student Failed with license."
    home_page.load()
    home_page.enterUsername(instructor_email)
    home_page.enterPassword(instructor_password)
    home_page.clickLogin()
    time.sleep(5)
    assert "INSTRUCTOR - " + instructor_fname + " " + instructor_lname == home_page.validateSuccessfulLogin(), \
        "Login failed with the new registered instructor."


@allure.title('S1: As student, register with credit card')
def test_register_student_creditcard(browser):
    home_page = homepageObjects(browser)
    register_page = registrationPage(browser)
    home_page.load()
    time.sleep(3)
    home_page.clickRegister()
    time.sleep(3)
    register_page.enter_firstName(student_regwith_credit_fname)
    register_page.enter_lastName(student_regwith_credit_lname)
    register_page.selectSchoolCampusDiscipline("ASA College - Miami - Nursing")  # ASA College2 - Miami1 - Nursing
    register_page.enter_graduationDate()
    register_page.enter_address("8262", "Main Street", "Massachusetts", "Quincy", "02169")
    register_page.enter_phoneNumber("2025550197")
    register_page.enter_email(student_credit_email)
    register_page.enter_password(student_credit_password)
    register_page.enter_creditcard_number("4242424242424242")
    register_page.enter_creditcard_expyr("2021")
    register_page.enter_creditcard_ccv("123")
    register_page.select_checkbox_sameaddress()
    register_page.select_agreementCheckbox()
    register_page.click_submitButton()
    assert register_page.validate_successfulRegistration() == True, "Registration of student Failed with credit card."
    home_page.load()
    time.sleep(3)
    home_page.enterUsername(student_credit_email)
    home_page.enterPassword(student_credit_password)
    home_page.clickLogin()
    assert "STUDENT - " + student_regwith_credit_fname + " " + student_regwith_credit_lname == home_page.validateSuccessfulLogin(), \
        "Login failed with the new registered student with credit card."


@allure.title('S2: As student, register with school license')
def test_register_student_license(browser):
    home_page = homepageObjects(browser)
    register_page = registrationPage(browser)
    home_page.load()
    home_page.enterUsername(admin_username)
    home_page.enterPassword(admin_password)
    home_page.clickLogin()
    time.sleep(3)
    home_page.manage_schoolLicenses()
    home_page.enter_search_word(school_discpline)
    assigned_licenses = int(home_page.return_assignedLicenses().replace(',', ''))
    remaining_licenses = int(home_page.return_remainingLicenses().replace(',', ''))
    home_page.clickLogout()
    home_page.clickRegister()
    time.sleep(3)
    register_page.enter_firstName(student_license_fname)
    register_page.enter_lastName(student_license_lname)
    register_page.selectSchoolCampusDiscipline(school_campus_discipline)
    register_page.enter_graduationDate()
    register_page.enter_address("8262", "Main Street", "Massachusetts", "Quincy", "02169")
    register_page.enter_phoneNumber("2025550197")
    register_page.enter_email(student_license_email)
    register_page.enter_password(student_license_password)
    register_page.select_agreementCheckbox()
    register_page.click_submitButton()
    time.sleep(2)
    assert register_page.validate_successfulRegistration() == True, "Registration of student Failed with license."
    home_page.load()
    home_page.enterUsername(admin_username)
    home_page.enterPassword(admin_password)
    home_page.clickLogin()
    time.sleep(5)
    home_page.manage_schoolLicenses()
    home_page.enter_search_word(school_discpline)
    assigned_licenses_new = int(home_page.return_assignedLicenses().replace(',', ''))
    remaining_licenses_new = int(home_page.return_remainingLicenses().replace(',', ''))
    assert assigned_licenses == assigned_licenses_new - 1, "Assigned licenses are not correct after registering a student with license."
    assert remaining_licenses == remaining_licenses_new + 1, "Remaining licenses are not correct after registering a student with license."
    home_page.clickLogout()
    home_page.enterUsername(student_license_email)
    home_page.enterPassword(student_license_password)
    home_page.clickLogin()
    assert "STUDENT - " + student_license_fname + " " + student_license_lname == home_page.validateSuccessfulLogin(), \
        "Login failed with the new registered student with license."


@allure.title('S3: Student updates profile in My Account screen')
def test_edit_student_profile(browser):
    my_account = myAccountPage(browser)
    home_page = homepageObjects(browser)
    my_account.edit_email(student_license_email_edited)
    my_account.edit_phone("(202)555-7910")
    my_account.edit_address1("2628")
    my_account.edit_address2("New Street")
    my_account.edit_state("Florida")
    my_account.edit_city("Beverly Hills")
    my_account.edit_zip("90035")
    time.sleep(4)
    my_account.click_save_account()
    time.sleep(3)
    home_page.clickLogout()
    home_page.enterUsername(student_license_email_edited)
    home_page.enterPassword(student_license_password)
    home_page.clickLogin()
    time.sleep(3)
    assert my_account.verify_email() == student_license_email_edited, "User's email address is not saved after the edit."
    assert my_account.verify_phone() == "(202)555-7910", "User's phone number is not saved after the edit"
    assert my_account.verify_address1() == "2628", "User's address 1 is not saved after the edit"
    assert my_account.verify_address2() == "New Street", "User's address 2 is not saved after the edit"
    assert my_account.verify_state() == "FL", "User's state is not saved after the edit"
    assert my_account.verify_city() == "Beverly Hills", "User's city is not saved after the edit"
    assert my_account.verify_zip() == "90035", "User's zip code is not saved after the edit"
    my_account.edit_email(student_license_email)
    time.sleep(4)
    my_account.click_save_account()
    time.sleep(3)


@allure.title('S4: Student edits password and try the new password')
def test_edit_student_password(browser):
    my_account = myAccountPage(browser)
    home_page = homepageObjects(browser)
    time.sleep(3)
    my_account.click_change_password()
    my_account.enter_cuurent_password(student_license_password)
    my_account.enter_new_password(student_license_password_new)
    time.sleep(2)
    my_account.click_submit_password()
    assert my_account.verify_alert_message() == "Your password has been changed successfully"
    home_page.clickLogout()
    home_page.enterUsername(student_license_email)
    home_page.enterPassword(student_license_password_new)
    home_page.clickLogin()
    assert "STUDENT - " + student_license_fname + " " + student_license_lname == home_page.validateSuccessfulLogin(), \
        "Login failed with the new registered student with license."
    time.sleep(3)
    # my_account.click_change_password()
    # my_account.enter_cuurent_password("Password2")
    # my_account.enter_new_password(student_license_password)
    # time.sleep(2)
    # my_account.click_submit_password()
    # assert my_account.verify_alert_message() == "Your password has been changed successfully"


@allure.title('SL1: School creates school file requirements for students  of type UPLOAD AND DOWNLOAD')
def test_create_schoolFileRequirement_student(browser):
    schoolfiles = school_schoolFilesPage(browser)
    home_page = homepageObjects(browser)
    home_page.load()
    home_page.enterUsername(crm_email)
    home_page.enterPassword(crm_password)
    home_page.clickLogin()
    time.sleep(4)
    schoolfiles.click_button_agreement()
    schoolfiles.click_tab_schoolFiles()
    schoolfiles.click_option_forStudents()
    time.sleep(5)
    schoolfiles.select_option_studentMust("download")
    schoolfiles.enter_documentName(documentName_readRequirement)
    schoolfiles.selectFileForUpload()
    # schoolfiles.click_savechanges_uploadfile()
    time.sleep(2)
    schoolfiles.click_saveChanges()
    time.sleep(5)
    schoolfiles.select_option_studentMust("provide")
    # schoolfiles.select_option_requirement(manage_reqName)
    schoolfiles.enter_requirement_provide(manage_reqName)
    time.sleep(2)
    schoolfiles.selectFileForUpload()
    # schoolfiles.click_savechanges_uploadfile()
    time.sleep(2)
    schoolfiles.select_option_expirationDate("Yes")
    schoolfiles.click_saveChanges()
    time.sleep(5)
    schoolfiles.select_option_studentMust("provide")
    # schoolfiles.select_option_requirement(manage_reqName)
    schoolfiles.enter_requirement_provide(manage_reqName)
    schoolfiles.selectFileForUpload()
    # schoolfiles.click_savechanges_uploadfile()
    time.sleep(2)
    schoolfiles.select_option_expirationDate("No")
    schoolfiles.click_saveChanges()
    time.sleep(5)
    schoolfiles.select_option_studentMust("provide")
    # schoolfiles.select_option_requirement(manage_reqName)
    schoolfiles.enter_requirement_provide(manage_reqName)
    schoolfiles.selectFileForUpload()
    # schoolfiles.click_savechanges_uploadfile()
    time.sleep(2)
    schoolfiles.select_option_expirationDate("Yes")
    schoolfiles.click_saveChanges()
    time.sleep(5)
    schoolfiles.select_option_studentMust("provide")
    # schoolfiles.select_option_requirement(multiple_reqName)
    schoolfiles.enter_requirement_provide(manage_reqName)
    schoolfiles.selectFileForUpload()
    # schoolfiles.click_savechanges_uploadfile()
    time.sleep(2)
    schoolfiles.select_option_expirationDate("No")
    schoolfiles.click_saveChanges()
    time.sleep(5)
    schoolfiles.select_option_studentMust("provide")
    # schoolfiles.select_option_requirement(multiple_reqName)
    schoolfiles.enter_requirement_provide(manage_reqName)
    schoolfiles.selectFileForUpload()
    # schoolfiles.click_savechanges_uploadfile()
    time.sleep(2)
    schoolfiles.select_option_expirationDate("No")
    schoolfiles.click_saveChanges()
    time.sleep(5)
    schoolfiles.select_option_studentMust("provide")
    # schoolfiles.select_option_requirement(multiple_reqName)
    schoolfiles.enter_requirement_provide(manage_reqName)
    schoolfiles.selectFileForUpload()
    # schoolfiles.click_savechanges_uploadfile()
    time.sleep(2)
    schoolfiles.select_option_expirationDate("No")
    schoolfiles.click_saveChanges()
    time.sleep(5)
    assert schoolfiles.verify_readRequirementName() == documentName_readRequirement, "Document name for read requirement is not correct."
    assert schoolfiles.verify_readRequirementMandatory() == "Yes", "Mandatory flag for read requirement is not correct."
    assert schoolfiles.verify_provideRequirementName() == manage_reqName, "Document name for provide requirement is not correct."
    assert schoolfiles.verify_provideRequirementMandatory() == "Yes", "Mandatory flag for provide requirement is not correct."
    assert schoolfiles.verify_provideRequirementExpiration() == "Yes", "Expiration date flag for provide requirement is not correct."


@allure.title('SL2: School creates school file requirements for INSTRUCTORS of type UPLOAD AND DOWNLOAD')
def test_create_schoolFileRequirement_instructor(browser):
    schoolfiles = school_schoolFilesPage(browser)
    schoolfiles.click_tab_schoolFiles()
    schoolfiles.click_option_forInstructors()
    time.sleep(12)
    schoolfiles.select_option_instructorMust("download")
    schoolfiles.enter_documentName(documentName_readRequirement)
    schoolfiles.selectFileForUpload()
    # schoolfiles.click_savechanges_uploadfile()
    time.sleep(2)
    schoolfiles.click_saveChanges()
    time.sleep(5)
    schoolfiles.select_option_instructorMust("provide")
    # schoolfiles.select_option_requirement(manage_reqName)
    schoolfiles.enter_requirement_provide(manage_reqName)
    time.sleep(2)
    schoolfiles.selectFileForUpload()
    # schoolfiles.click_savechanges_uploadfile()
    time.sleep(2)
    schoolfiles.select_option_expirationDate("Yes")
    schoolfiles.click_saveChanges()
    time.sleep(7)
    assert schoolfiles.verify_readRequirementName() == documentName_readRequirement, "Document name for read requirement is not correct."
    assert schoolfiles.verify_readRequirementMandatory() == "Yes", "Mandatory flag for read requirement is not correct."
    assert schoolfiles.verify_provideRequirementName() == manage_reqName, "Document name for provide requirement is not correct."
    assert schoolfiles.verify_provideRequirementMandatory() == "Yes", "Mandatory flag for provide requirement is not correct."
    assert schoolfiles.verify_provideRequirementExpiration() == "Yes", "Expiration date flag for provide requirement is not correct."


@allure.title('S5: Student completes school file requirement by uploading from computer')
def test_student_upload_local_file(browser):
    home_page = homepageObjects(browser)
    schoolfiles_page = schoolFilesPage(browser)
    home_page.load()
    home_page.enterUsername(student_license_email)
    home_page.enterPassword(student_license_password_new)
    home_page.clickLogin()
    home_page.clickSchoolFiles()
    time.sleep(3)
    schoolfiles_page.clickUploadResume()
    schoolfiles_page.addFileToUpload()
    time.sleep(2)
    schoolfiles_page.enter_ExpDate('01/01/2022')
    schoolfiles_page.clickSelectButton()
    time.sleep(10)
    assert "green.png" in schoolfiles_page.validateSuccessfulUpload1(), "Uploading the file failed."


@allure.title('S6 - Student completes school file requirement by uploading from "My Student Account"')
def test_student_upload_from_document(browser):
    schoolfiles_page = schoolFilesPage(browser)
    schoolfiles_page.clickUploadResume2()
    time.sleep(2)
    schoolfiles_page.select_upload_type("account")
    time.sleep(4)
    schoolfiles_page.click_radio_button()
    time.sleep(3)
    schoolfiles_page.click_document_select_button()
    time.sleep(7)
    assert "green.png" in schoolfiles_page.validateSuccessfulUpload2(), "Uploading the file failed."


@allure.title('S7 - Student completes school file requirement by uploading document with expiration date')
def test_upload_document_expiration_date(browser):
    schoolfiles_page = schoolFilesPage(browser)
    schoolfiles_page.do_refresh()
    time.sleep(6)
    schoolfiles_page.clickUploadResume3()
    time.sleep(2)
    schoolfiles_page.select_upload_type("account")
    time.sleep(4)
    schoolfiles_page.click_radio_button()
    schoolfiles_page.enter_ExpDate('01/01/2022')
    time.sleep(3)
    schoolfiles_page.click_document_select_button()
    assert "green.png" in schoolfiles_page.validateSuccessfulUpload3(), "Uploading the file failed."
#

@allure.title('S8 - School completes multiple school file requirements with one file')
def test_school_upload_multiple_req(browser):
    home_page = homepageObjects(browser)
    myStudents = school_myStudentsPage(browser)
    home_page.load()
    home_page.enterUsername(crm_email)
    home_page.enterPassword(crm_password)
    home_page.clickLogin()
    time.sleep(3)
    home_page.clickMyStudents()
    time.sleep(2)
    home_page.clickOptionStudents()
    myStudents.click_student_name()
    myStudents.click_upload_button()
    # myStudents.click_crossIcon()
    time.sleep(5)
    myStudents.upload_file()
    myStudents.select_fulfill_yes()
    myStudents.check_multiple_req()
    myStudents.click_confirm()
    time.sleep(5)
    assert myStudents.verify_completed_multiple_req() == True, "One or more multiple requirements are not successfully completed."


@allure.title('S21: Student loads FAQs, Call me back, views tutorial and places helpdesk ticket')
def test_student_checks_helpSection(browser):
    home_page = homepageObjects(browser)
    help_page = HelpPage(browser)
    home_page.load()
    home_page.enterUsername(student_license_email)
    home_page.enterPassword(student_license_password_new)
    home_page.clickLogin()
    time.sleep(3)
    home_page.clickHelp()
    assert help_page.clickOptionTutorial() == True, "Tutorial video did not opened"
    home_page.clickHelp()
    time.sleep(2)
    # home_page.clickOptionCallMeBack()
    # time.sleep(2)
    # assert help_page.validateCallMeBack() == "Calendly - Karen Canon", "Call Me Back page is not loaded successfully"
    # help_page.closeCallMeBackTab()
    # home_page.clickHelp()
    home_page.clickOptionFAQ()
    time.sleep(2)
    assert help_page.validateFAQ() == "FAQs", "FAQ page is not loaded correctly."
    # help_page.switchTo_iframe_faqs()
    # help_page.click_faqFolder1()
    # assert help_page.verify_faqFolder_heading() == "CLINICAL ROTATION MANAGER (SCHOOL) USER FAQs", "FAQ Folder 1 did not loaded correctly"
    # help_page.click_goBack()
    # help_page.click_faqFolder2()
    # assert help_page.verify_faqFolder_heading() == "HOSPITAL USER FAQs", "FAQ Folder 2 did not loaded correctly"
    # help_page.click_goBack()
    # help_page.click_faqFolder3()
    # assert help_page.verify_faqFolder_heading() == "STUDENT AND INSTRUCTOR FAQs", "FAQ Folder 3 did not loaded correctly"
    # help_page.click_goBack()
    # help_page.switchTo_defaultContent()
    home_page.clickHelp()
    home_page.clickOptionHelpdesk()
    time.sleep(3)
    # help_page.switchTo_iframe_faqs()
    # help_page.click_NewTicket()
    # time.sleep(10)
    # help_page.enter_phone('1234567890')
    # help_page.enter_ext('123')
    # help_page.select_helpTopic('General Questions')
    # help_page.enter_subject('Test Subject Automation')
    help_page.enter_message('This is a test message created by Automation ' + randNum)
    help_page.click_CreateTicket()
    time.sleep(1)
    ticket = help_page.get_ticketNumber()
    assert "was created sucessfully!" in ticket, "Helpdesk ticket failed to be created."
    # help_page.switchTo_defaultContent()
    # home_page.clickLogout()
    # home_page.enterUsername(admin_username)
    # home_page.enterPassword(admin_password)
    # home_page.clickLogin()
    # home_page.clickHelp()
    # home_page.clickOptionHelpdesk()
    # help_page.switchTo_iframe_faqs()
    # help_page.enter_ticketNumber(ticket)
    # help_page.click_search()
    # help_page.click_ticket()
    # assert help_page.verify_ticketName() == student_license_fname + " " + student_license_lname, "Name on the ticket is wrong."
    # assert student_license_email in help_page.verify_ticketEmail(), "Email on ticket is wrong."
    # assert help_page.verify_ticketHelpTopic() == "General Questions", "Help Topic on the ticket is wrong."
    # assert help_page.verify_ticketSubject() == 'Test Subject Automation', "Subject on the ticket is wrong."
    # assert help_page.verify_ticketMessage() == 'This is a test message created by Automation', "Message is wrong on the ticket."
    # help_page.switchTo_defaultContent()


@allure.title('SL3: School requests rotation in a hospital discilpine that does not require approval')
def test_create_rotation_without_approval(browser):
    home_page = homepageObjects(browser)
    rotations_page = school_myRotationsPage(browser)
    help_page = HelpPage(browser)
    help_page.switchTo_defaultContent()
    home_page.clickLogout()
    home_page.load()
    home_page.enterUsername(crm_email)
    home_page.enterPassword(crm_password)
    # home_page.enterUsername("crm_email_940524@email.com")
    # home_page.enterPassword("Password1")
    home_page.clickLogin()
    time.sleep(3)
    rotations_page.click_tab_MyRotations()
    rotations_page.click_option_new()
    time.sleep(3)
    rotations_page.select_hospital(hospital_name)
    # rotations_page.select_hospital("Hospital Automation 940524")
    time.sleep(5)
    rotations_page.select_rotationType('Observation')
    rotations_page.select_studentsCount('8')
    time.sleep(5)
    # rotations_page.browser_zoom_out(2)
    rotations_page.click_addShift()
    rotations_page.select_startTime("5:00 (5:00 AM)")
    rotations_page.select_endTime("9:00 (9:00 AM)")
    time.sleep(3)
    rotations_page.click_next()
    time.sleep(3)
    start_date = rotations_page.enter_startDate()
    end_date = rotations_page.enter_endDate()
    rotations_page.check_allDays()
    rotations_page.click_next()
    time.sleep(2)
    rotations_page.click_save()
    # rotations_page.browser_zoom_in(2)
    rotations_page.select_rotationLabel('Fall')
    rotations_page.enter_comments('Comment by Automation')
    time.sleep(5)
    rotations_page.click_submit()
    time.sleep(5)
    rotations_page.click_ok()
    time.sleep(10)
    rotationNumber = rotations_page.get_rotationNumber()
    rotations_page.click_viewRotations()
    time.sleep(3)
    assert rotationNumber in rotations_page.verify_RotationNumber(), "Rotation number not found in My Rotations"
    assert rotations_page.verify_RotationLabel() == "Fall", "Rotation Label is incorrect."
    hosp_details = rotations_page.verify_HospitalDetails()
    assert hospital_name in hosp_details, "Hospital Name not found My Rotations"
    assert discipline1 in hosp_details, "Discipline name not found in My Rotations"
    assert 'Observation' in hosp_details, "Rotation Type not found in My Rotations"
    assert 'Comment by Automation' in hosp_details, "Comment not found in My Rotations"
    assert rotations_page.verify_startDate() == start_date, "Start Date not found in My Rotations"
    assert rotations_page.verify_endDate() == end_date, "End Date not found in My Rotations"
    assert rotations_page.verify_slotsOffered() == '8', "Total slots offered is not correct."
    home_page.clickLogout()
    home_page.enterUsername(admin_username)
    home_page.enterPassword(admin_password)
    home_page.clickLogin()
    rotations_page.click_tabManage()
    rotations_page.click_optionManageDatabase()
    rotations_page.enter_rotationNumberEdit(rotationNumber)
    rotations_page.click_go()
    time.sleep(5)
    assert 'Current Status: Active' in rotations_page.verify_rotationStatus(), "Rotation status is not active in rotation info"


@allure.title('SL4: School requests rotation in a hospital discilpine that requires approval')
def test_create_rotation_with_approval(browser):
    home_page = homepageObjects(browser)
    rotations_page = school_myRotationsPage(browser)
    home_page.clickLogout()
    home_page.enterUsername(crm_email)
    home_page.enterPassword(crm_password)
    home_page.clickLogin()
    time.sleep(3)
    rotations_page.click_tab_MyRotations()
    rotations_page.click_option_new()
    time.sleep(3)
    rotations_page.select_hospital(hospital_name)
    time.sleep(5)
    rotations_page.select_discipline(discipline2)
    time.sleep(5)
    rotations_page.select_rotationType('Observation')
    time.sleep(2)
    rotations_page.select_studentsCount('8')
    rotations_page.click_addShift()
    rotations_page.select_startTime("5:00 (5:00 AM)")
    rotations_page.select_endTime("9:00 (9:00 AM)")
    time.sleep(3)
    rotations_page.click_next()
    start_date = rotations_page.enter_startDate()
    end_date = rotations_page.enter_endDate()
    rotations_page.check_allDays()
    rotations_page.click_next()
    time.sleep(2)
    rotations_page.click_save()
    rotations_page.select_rotationLabel('Fall')
    rotations_page.enter_comments('Comment by Automation')
    time.sleep(5)
    rotations_page.click_submit()
    time.sleep(5)
    rotations_page.click_ok()
    time.sleep(10)
    global rotationNumber
    rotationNumber = rotations_page.get_rotationNumber()
    rotations_page.click_viewRotations()
    time.sleep(3)
    assert rotationNumber in rotations_page.verify_RotationNumber(), "Rotation number not found in My Rotations"
    hosp_details = rotations_page.verify_HospitalDetails()
    assert hospital_name in hosp_details, "Hospital Name not found My Rotations"
    assert discipline2 in hosp_details, "Discipline name not found in My Rotations"
    assert 'Observation' in hosp_details, "Rotation Type not found in My Rotations"
    assert 'Comment by Automation' in hosp_details, "Comment not found in My Rotations"
    assert rotations_page.verify_startDate() == start_date, "Start Date not found in My Rotations"
    assert rotations_page.verify_endDate() == end_date, "End Date not found in My Rotations"
    assert rotations_page.verify_slotsOffered() == '8', "Total slots offered is not correct."
    home_page.clickLogout()
    home_page.enterUsername(admin_username)
    home_page.enterPassword(admin_password)
    home_page.clickLogin()
    rotations_page.click_tabManage()
    rotations_page.click_optionManageDatabase()
    rotations_page.enter_rotationNumberEdit(rotationNumber)
    rotations_page.click_go()
    time.sleep(5)
    assert 'Current Status: Pending Approval' in rotations_page.verify_rotationStatus(), "Rotation status is not Pending Approval in rotation info"


@allure.title('H2: Hospital approves rotation that is pending approval')
def test_hospital_approves_rotation(browser):
    home_page = homepageObjects(browser)
    rotations_page = school_myRotationsPage(browser)
    home_page.clickLogout()
    home_page.enterUsername(hospUser_email)
    home_page.enterPassword(hospUser_password)
    home_page.clickLogin()
    time.sleep(3)
    rotations_page.click_tab_MyRotations()
    rotations_page.click_option_viewRotations()
    rotations_page.click_pendingApproval()
    rotations_page.click_process()
    global rotationNumber
    time.sleep(5)
    assert rotations_page.verify_successMessage() == "Success\nRotation #" + rotationNumber + " has been created successfully"
    rotations_page.click_ok()
    time.sleep(10)
    rotations_page.click_active()
    time.sleep(5)
    assert rotationNumber in rotations_page.verify_RotationNumber_hospUser(), "Rotation number not found in Active Rotations"
    home_page.clickLogout()
    home_page.enterUsername(admin_username)
    home_page.enterPassword(admin_password)
    home_page.clickLogin()
    time.sleep(3)
    rotations_page.click_tabManage()
    rotations_page.click_optionManageDatabase()
    rotations_page.enter_rotationNumberEdit(rotationNumber)
    rotations_page.click_go()
    time.sleep(5)
    assert 'Current Status: Active' in rotations_page.verify_rotationStatus(), "Rotation status is not active in rotation info"
    time.sleep(15)
    gmail_page = gmailPage(browser)
    gmail_page.open_mailbox(crm_email.split('@')[0])
    time.sleep(5)
    gmail_page.open_email_rotationApproved()
    time.sleep(5)
    assert gmail_page.verify_subject_rotationApproved() == "Rotation was Approved", "Email subject is wrong for rotation approved email"
    email_text = gmail_page.verify_emailText_rotationApproved()
    assert hospital_name in email_text, "Hospital name is wrong in rotation approved email"
    assert discipline2 in email_text, "Discipline name is wrong in rotation approved email"
    assert "#" + rotationNumber in email_text, "Rotation number is wrong in rotation approved email"
    assert "approved" in email_text, "Approved keyword not found in email text"
    # gmail_page.delete_emails()
    gmail_page.close_gmail()
    # gmail_page = gmailPage(browser)
    # time.sleep(2)
    # gmail_page.open_gmail()
    # gmail_page.login_gmail(crm_gmail_username, crm_gmail_password)
    # gmail_page.open_email_rotationApproved()
    # assert gmail_page.verify_subject_rotationApproved() == "Rotation was Approved", "Email subject is wrong for rotation approved email"
    # email_text = gmail_page.verify_emailText_rotationApproved()
    # assert hospital_name in email_text, "Hospital name is wrong in rotation approved email"
    # assert discipline2 in email_text, "Discipline name is wrong in rotation approved email"
    # assert "#"+rotationNumber in email_text, "Rotation number is wrong in rotation approved email"
    # assert "approved" in email_text, "Approved keyword not found in email text"
    # gmail_page.delete_emails()
    # email_text = gmailApi.main()
    # assert hospital_name in email_text, "Hospital name is wrong in rotation approved email"
    # assert discipline2 in email_text, "Discipline name is wrong in rotation approved email"
    # assert "#"+rotationNumber in email_text, "Rotation number is wrong in rotation approved email"
    # assert "approved" in email_text, "Approved keyword not found in email text"
    # gmail_page.delete_emails()


@allure.title('H3: Hospital declines rotation that is pending approval')
def test_hospital_declines_rotation(browser):
    home_page = homepageObjects(browser)
    rotations_page = school_myRotationsPage(browser)
    # gmail_page = gmailPage(browser)
    # gmail_page.open_gmail()
    # gmail_page.login_gmail(crm_gmail_username, crm_gmail_password)
    # gmail_page.delete_emails()
    test_create_rotation_with_approval(browser)
    home_page.clickLogout()
    home_page.enterUsername(hospUser_email)
    home_page.enterPassword(hospUser_password)
    home_page.clickLogin()
    time.sleep(5)
    rotations_page.click_tab_MyRotations()
    rotations_page.click_option_viewRotations()
    rotations_page.click_pendingApproval()
    # rotations_page.click_process()
    rotations_page.click_decline()
    time.sleep(5)
    rotations_page.click_confirm()
    global rotationNumber
    time.sleep(5)
    rotations_page.click_declined()
    time.sleep(5)
    assert rotationNumber in rotations_page.verify_RotationNumber_hospUser(), "Rotation number not found in Active Rotations"
    home_page.clickLogout()
    home_page.enterUsername(admin_username)
    home_page.enterPassword(admin_password)
    home_page.clickLogin()
    time.sleep(3)
    rotations_page.click_tabManage()
    rotations_page.click_optionManageDatabase()
    rotations_page.enter_rotationNumberEdit(rotationNumber)
    rotations_page.click_go()
    time.sleep(7)
    assert 'Current Status: Declined' in rotations_page.verify_rotationStatus(), "Rotation status is not declined in rotation info"
    time.sleep(60)
    gmail_page = gmailPage(browser)
    gmail_page.open_mailbox(crm_email.split('@')[0])
    gmail_page.open_email_rotationDeclined()
    assert gmail_page.verify_subject_rotationApproved() == "Rotation Manager", "Email subject is wrong for rotation declined email"
    email_text = gmail_page.verify_emailText_rotationApproved()
    assert hospital_name in email_text, "Hospital name is wrong in rotation declined email"
    assert discipline2 in email_text, "Discipline name is wrong in rotation declined email"
    assert "#" + rotationNumber in email_text, "Rotation number is wrong in rotation declined email"
    assert "declined" in email_text, "Declined keyword not found in email text"
    # gmail_page.delete_emails()
    gmail_page.close_gmail()


@allure.title('H4: Hospital sets up unit schedules')
def test_hospital_setup_unit_schedule(browser):
    home_page = homepageObjects(browser)
    customize_unit = customizeUnits(browser)
    hosp_obj = adminHospitalObj(browser)
    home_page.load()
    time.sleep(3)
    ############################################
    ##### Should be deleted after bug fix ######
    ############################################
    home_page.enterUsername(admin_username)
    home_page.enterPassword(admin_password)
    home_page.clickLogin()
    time.sleep(3)
    hosp_obj.click_tab_hospital()
    hosp_obj.click_hospitals_edit()
    hosp_obj.choose_hospital(hospital_name)
    hosp_obj.click_submit()
    time.sleep(5)
    customize_unit.click_unit_schedule()
    time.sleep(6)
    home_page.clickLogout()
    time.sleep(3)
    ###############################################
    home_page.enterUsername(hospUser_email)
    home_page.enterPassword(hospUser_password)
    home_page.clickLogin()
    time.sleep(3)
    home_page.clickCustomize()
    home_page.clickOptionUnits()
    customize_unit.click_tab_schedules()
    time.sleep(3)
    start_date1 = customize_unit.edit_startdate_disc1()
    end_date1 = customize_unit.edit_enddate_disc1()
    customize_unit.edit_starttime_disc1("16:00 (4:00 PM)")
    customize_unit.edit_endtime_disc1("17:00 (5:00 PM)")
    customize_unit.edit_students_disc1("5")
    customize_unit.select_days_disc1()
    start_date2 = customize_unit.edit_startdate_disc2()
    end_date2 = customize_unit.edit_enddate_disc2()
    customize_unit.edit_starttime_disc2("18:00 (6:00 PM)")
    customize_unit.edit_endtime_disc2("19:00 (7:00 PM)")
    customize_unit.edit_students_disc2("10")
    customize_unit.select_days_disc2()
    customize_unit.click_save()
    time.sleep(5)
    browser.refresh()
    time.sleep(7)
    assert start_date1 == customize_unit.verify_startdate_disc1(), "Start date for discipline 1 is not saved."
    assert end_date1 == customize_unit.verify_enddate_disc1(), "End date for discipline 1 is not saved."
    assert customize_unit.verify_starttime_disc1() == "16:00 (4:00 PM)", "Start time for discipline 1 is not saved."
    assert customize_unit.verify_endtime_disc1() == "17:00 (5:00 PM)", "End time for discipline 1 is not saved."
    assert customize_unit.verify_students_disc1() == "5", "Number of students for discipline 1 is not saved."
    assert start_date2 == customize_unit.verify_startdate_disc2(), "Start date for discipline 2 is not saved."
    assert end_date2 == customize_unit.verify_enddate_disc2(), "End date for discipline 2 is not saved."
    assert customize_unit.verify_starttime_disc2() == "18:00 (6:00 PM)", "Start time for discipline 2 is not saved."
    assert customize_unit.verify_endtime_disc2() == "19:00 (7:00 PM)", "End time for discipline 2 is not saved."
    assert customize_unit.verify_students_disc2() == "10", "Number of students for discipline 2 is not saved."
    assert customize_unit.verify_days_disc2() == True, "Selected days for discipline 2 are not saved."


@allure.title('H5: Hospital creates rotation that will overlap with others later')
def test_create_rotation_to_overlap(browser):
    home_page = homepageObjects(browser)
    rotations_page = school_myRotationsPage(browser)
    home_page.clickLogout()
    home_page.load()
    home_page.enterUsername(hospUser_email)
    home_page.enterPassword(hospUser_password)
    home_page.clickLogin()
    home_page.clickMyDisciplines()
    home_page.choose_discipline_to_add(discipline3)
    time.sleep(1)
    home_page.clickSubmitAddDiscipline()
    time.sleep(2)
    home_page.clickCloseModal()
    time.sleep(3)
    home_page.clickLogout()
    home_page.enterUsername(crm_email)
    home_page.enterPassword(crm_password)
    home_page.clickLogin()
    rotations_page.click_tab_MyRotations()
    rotations_page.click_option_new()
    rotations_page.select_hospital(hospital_name)
    time.sleep(2)
    rotations_page.select_discipline(discipline3)
    time.sleep(5)
    rotations_page.select_rotationType('Observation')
    rotations_page.select_studentsCount('5')
    time.sleep(5)
    rotations_page.click_addShift()
    rotations_page.select_startTime("16:00 (4:00 PM)")
    rotations_page.select_endTime("18:00 (6:00 PM)")
    time.sleep(3)
    rotations_page.click_next()
    time.sleep(3)
    start_date = rotations_page.enter_startDate_new()
    end_date = rotations_page.enter_endDate_new()
    rotations_page.check_allDays()
    rotations_page.click_next()
    time.sleep(2)
    rotations_page.click_save()
    rotations_page.select_rotationLabel('Fall')
    rotations_page.enter_comments('Comment by Automation')
    time.sleep(5)
    rotations_page.click_submit()
    time.sleep(5)
    rotations_page.click_ok()
    time.sleep(5)
    global rotation_h5
    rotationNumber = rotations_page.get_rotationNumber()
    rotation_h5 = rotationNumber
    print("Rotation H5: " + rotation_h5)
    rotations_page.click_viewRotations()
    assert rotationNumber in rotations_page.verify_RotationNumber(), "Rotation number not found in My Rotations"
    hosp_details = rotations_page.verify_HospitalDetails()
    assert hospital_name in hosp_details, "Hospital Name not found My Rotations"
    assert discipline3 in hosp_details, "Discipline name not found in My Rotations"
    assert rotations_page.verify_startDate() == start_date, "Start Date not found in My Rotations"
    assert rotations_page.verify_endDate() == end_date, "End Date not found in My Rotations"
    assert rotations_page.verify_slotsOffered() == '5', "Total slots offered is not correct."
    home_page.clickLogout()
    home_page.enterUsername(admin_username)
    home_page.enterPassword(admin_password)
    home_page.clickLogin()
    time.sleep(3)
    rotations_page.click_tabManage()
    rotations_page.click_optionManageDatabase()
    rotations_page.enter_rotationNumberEdit(rotationNumber)
    rotations_page.click_go()
    time.sleep(5)
    assert 'Current Status: Pending Approval' in rotations_page.verify_rotationStatus(), "Rotation status is not " \
                                                                                         "pending approval in " \
                                                                                         "rotation info "


@allure.title(
    'SL5.1: School requests rotations for a hospital discipline that fits unit schedule and overlaps with other '
    'rotation.')
def test_school_requests_rotation_fitYes_overlapYes(browser):
    home_page = homepageObjects(browser)
    rotations_page = school_myRotationsPage(browser)
    home_page.clickLogout()
    home_page.load()
    time.sleep(4)
    home_page.enterUsername(crm_email)
    home_page.enterPassword(crm_password)
    home_page.clickLogin()
    rotations_page.click_tab_MyRotations()
    rotations_page.click_option_new()
    rotations_page.select_hospital(hospital_name)
    time.sleep(5)
    rotations_page.select_discipline(discipline3)
    time.sleep(2)
    rotations_page.select_rotationType('Observation')
    rotations_page.select_studentsCount('1')
    time.sleep(5)
    rotations_page.click_addShift()
    rotations_page.select_startTime("16:00 (4:00 PM)")
    rotations_page.select_endTime("17:00 (5:00 PM)")
    time.sleep(3)
    rotations_page.click_next()
    time.sleep(3)
    start_date = rotations_page.enter_startDate_mod(2, 1, 1)
    end_date = rotations_page.enter_endDate_mod(4, 1, 1)
    rotations_page.check_allDays()
    rotations_page.click_next()
    time.sleep(2)
    rotations_page.click_save()
    rotations_page.select_rotationLabel('Fall')
    rotations_page.enter_comments('Comment by Automation')
    time.sleep(5)
    rotations_page.click_submit()
    time.sleep(5)
    rotations_page.click_ok()
    time.sleep(5)
    rotationNumber = rotations_page.get_rotationNumber()
    rotations_page.click_viewRotations()
    time.sleep(3)
    assert rotationNumber in rotations_page.verify_RotationNumber(), "Rotation number not found in My Rotations"
    hosp_details = rotations_page.verify_HospitalDetails()
    assert hospital_name in hosp_details, "Hospital Name not found My Rotations"
    assert discipline3 in hosp_details, "Discipline name not found in My Rotations"
    assert rotations_page.verify_startDate() == start_date, "Start Date not found in My Rotations"
    assert rotations_page.verify_endDate() == end_date, "End Date not found in My Rotations"
    assert rotations_page.verify_slotsOffered() == '1', "Total slots offered is not correct."


@allure.title(
    'SL5.2: School requests rotations for a hospital discipline that fits unit schedule and not overlaps with other '
    'rotation.')
def test_school_requests_rotation_fitYes_overlapNo(browser):
    home_page = homepageObjects(browser)
    rotations_page = school_myRotationsPage(browser)
    rotations_page.click_tab_MyRotations()
    rotations_page.click_option_new()
    rotations_page.select_hospital(hospital_name)
    time.sleep(5)
    rotations_page.select_discipline(discipline3)
    time.sleep(2)
    rotations_page.select_rotationType('Observation')
    rotations_page.select_studentsCount('1')
    time.sleep(5)
    rotations_page.click_addShift()
    rotations_page.select_startTime("16:00 (4:00 PM)")
    rotations_page.select_endTime("17:00 (5:00 PM)")
    time.sleep(3)
    rotations_page.click_next()
    time.sleep(3)
    start_date = rotations_page.enter_startDate_mod(2, 0, 1)
    end_date = rotations_page.enter_endDate_mod(4, 0, 1)
    rotations_page.check_allDays()
    rotations_page.click_next()
    time.sleep(2)
    rotations_page.click_save()
    rotations_page.select_rotationLabel('Fall')
    rotations_page.enter_comments('Comment by Automation')
    time.sleep(5)
    rotations_page.click_submit()
    time.sleep(5)
    rotations_page.click_ok()
    time.sleep(5)
    rotationNumber = rotations_page.get_rotationNumber()
    rotations_page.click_viewRotations()
    time.sleep(3)
    assert rotationNumber in rotations_page.verify_RotationNumber(), "Rotation number not found in My Rotations"
    hosp_details = rotations_page.verify_HospitalDetails()
    assert hospital_name in hosp_details, "Hospital Name not found My Rotations"
    assert discipline3 in hosp_details, "Discipline name not found in My Rotations"
    assert rotations_page.verify_startDate() == start_date, "Start Date not found in My Rotations"
    assert rotations_page.verify_endDate() == end_date, "End Date not found in My Rotations"
    assert rotations_page.verify_slotsOffered() == '1', "Total slots offered is not correct."


@allure.title(
    'SL5.3: School requests rotations for a hospital discipline that does not fit unit schedule and overlaps with '
    'other rotation.')
def test_school_requests_rotation_fitNo_overlapYes(browser):
    home_page = homepageObjects(browser)
    rotations_page = school_myRotationsPage(browser)
    rotations_page.click_tab_MyRotations()
    rotations_page.click_option_new()
    rotations_page.select_hospital(hospital_name)
    time.sleep(5)
    rotations_page.select_discipline(discipline3)
    time.sleep(2)
    rotations_page.select_rotationType('Observation')
    rotations_page.select_studentsCount('1')
    time.sleep(5)
    rotations_page.click_addShift()
    rotations_page.select_startTime("16:00 (4:00 PM)")
    rotations_page.select_endTime("17:00 (5:00 PM)")
    time.sleep(3)
    rotations_page.click_next()
    time.sleep(3)
    start_date = rotations_page.enter_startDate_mod(0, -1, 1)#-4, 3, 1
    end_date = rotations_page.enter_endDate_mod(3, 1, 1)#-2, 3, 1
    rotations_page.check_allDays()
    rotations_page.click_next()
    time.sleep(2)
    rotations_page.click_save()
    rotations_page.select_rotationLabel('Fall')
    rotations_page.enter_comments('Comment by Automation')
    time.sleep(5)
    rotations_page.click_submit()
    time.sleep(5)
    rotations_page.click_ok()
    time.sleep(5)
    rotationNumber = rotations_page.get_rotationNumber()
    rotations_page.click_viewRotations()
    time.sleep(3)
    assert rotationNumber in rotations_page.verify_RotationNumber(), "Rotation number not found in My Rotations"
    hosp_details = rotations_page.verify_HospitalDetails()
    assert hospital_name in hosp_details, "Hospital Name not found My Rotations"
    assert discipline3 in hosp_details, "Discipline name not found in My Rotations"
    assert rotations_page.verify_startDate() == start_date, "Start Date not found in My Rotations"
    assert rotations_page.verify_endDate() == end_date, "End Date not found in My Rotations"
    assert rotations_page.verify_slotsOffered() == '1', "Total slots offered is not correct."


@allure.title(
    'SL5.4: School requests rotations for a hospital discipline that does not fit unit schedule and not overlaps with '
    'other rotation.')
def test_school_requests_rotation_fitNo_overlapNo(browser):
    home_page = homepageObjects(browser)
    rotations_page = school_myRotationsPage(browser)
    rotations_page.click_tab_MyRotations()
    rotations_page.click_option_new()
    rotations_page.select_hospital(hospital_name)
    time.sleep(5)
    rotations_page.select_discipline(discipline3)
    time.sleep(2)
    rotations_page.select_rotationType('Observation')
    rotations_page.select_studentsCount('1')
    time.sleep(5)
    rotations_page.click_addShift()
    rotations_page.select_startTime("16:00 (4:00 PM)")
    rotations_page.select_endTime("17:00 (5:00 PM)")
    time.sleep(3)
    rotations_page.click_next()
    time.sleep(3)
    start_date = rotations_page.enter_startDate_mod(0, -2, 1)#0, 4, 1
    end_date = rotations_page.enter_endDate_mod(1, -2, 1)#2, 4, 1
    rotations_page.check_allDays()
    rotations_page.click_next()
    time.sleep(2)
    rotations_page.click_save()
    rotations_page.select_rotationLabel('Fall')
    rotations_page.enter_comments('Comment by Automation')
    time.sleep(5)
    rotations_page.click_submit()
    time.sleep(5)
    rotations_page.click_ok()
    time.sleep(5)
    rotationNumber = rotations_page.get_rotationNumber()
    rotations_page.click_viewRotations()
    time.sleep(3)
    assert rotationNumber in rotations_page.verify_RotationNumber(), "Rotation number not found in My Rotations"
    hosp_details = rotations_page.verify_HospitalDetails()
    assert hospital_name in hosp_details, "Hospital Name not found My Rotations"
    assert discipline3 in hosp_details, "Discipline name not found in My Rotations"
    assert rotations_page.verify_startDate() == start_date, "Start Date not found in My Rotations"
    assert rotations_page.verify_endDate() == end_date, "End Date not found in My Rotations"
    assert rotations_page.verify_slotsOffered() == '1', "Total slots offered is not correct."


@allure.title('H10: Hospital processes rotation that fits unit schedule but overlaps with other rotations')
def test_hospital_process_rotation_fitYes_overlapYes(browser):
    home_page = homepageObjects(browser)
    rotations_page = hosp_myRotationsPage(browser)
    home_page.load()
    home_page.enterUsername(hospUser_email)
    home_page.enterPassword(hospUser_password)
    home_page.clickLogin()
    time.sleep(3)
    rotations_page.click_myRotations()
    rotations_page.click_viewRotations()
    rotations_page.click_pendingApprovals()
    rotations_page.click_process_hospitalRotation()
    time.sleep(4)
    rotations_page.click_acceptRequest()
    time.sleep(3)
    rotations_page.click_ok()
    time.sleep(4)
    rotations_page.click_process_fitYes_overlapYes()
    time.sleep(5)
    assert "The rotation that you are processing overlaps with active rotations" in rotations_page.verify_message_process()
    rotations_page.click_acceptRequest()
    global rotationNumber
    time.sleep(4)
    global rotation_h10
    rotationNumber = rotations_page.get_rotationNumber()
    rotation_h10 = rotationNumber
    print("Rotation H10: " + rotation_h10)
    rotations_page.click_ok()
    time.sleep(3)
    rotations_page.click_Active()
    time.sleep(3)
    assert rotationNumber in rotations_page.verify_first_rotation(), "Approved rotation not found on Active rotations " \
                                                                     "page "


@allure.title('H8: Hospital processes rotation that fits unit schedule and does not overlap with other rotations')
def test_hospital_process_rotation_fitYes_overlapNo(browser):
    home_page = homepageObjects(browser)
    rotations_page = hosp_myRotationsPage(browser)
    home_page.load()
    home_page.enterUsername(hospUser_email)
    home_page.enterPassword(hospUser_password)
    home_page.clickLogin()
    time.sleep(3)
    rotations_page.click_myRotations()
    rotations_page.click_viewRotations()
    rotations_page.click_pendingApprovals()
    time.sleep(2)
    rotations_page.click_process_fitYes_overlapNo()
    time.sleep(5)
    assert rotations_page.verify_message_process2() == "This rotation fits your calendar and does not overlap with " \
                                                       "other rotations."
    rotations_page.click_acceptRequest()
    global rotationNumber
    time.sleep(3)
    rotationNumber = rotations_page.get_rotationNumber()
    rotations_page.click_ok()
    time.sleep(3)
    rotations_page.click_Active()
    time.sleep(3)
    assert rotationNumber in rotations_page.verify_first_rotation(), "Approved rotation not found on Active rotations " \
                                                                     "page "


@allure.title('H6: Hospital processes rotation that does not fit unit schedule and overlaps with active rotation')
def test_hospital_process_rotation_fitNo_overlapYes(browser):
    home_page = homepageObjects(browser)
    rotations_page = hosp_myRotationsPage(browser)
    home_page.load()
    home_page.enterUsername(hospUser_email)
    home_page.enterPassword(hospUser_password)
    home_page.clickLogin()
    time.sleep(3)
    rotations_page.click_myRotations()
    rotations_page.click_viewRotations()
    rotations_page.click_pendingApprovals()
    rotations_page.click_process_fitNo_overlapYes()
    time.sleep(5)
    assert rotations_page.verify_message_process() == "The rotation you are processing does not fit the hospital schedule, and also overlapswith active rotation(s).", "Message displayed during the processing of rotation is wrong. "
    rotations_page.click_confirm()
    global rotation_h6
    time.sleep(3)
    rotationNumber = rotations_page.get_rotationNumber()
    rotation_h6 = rotationNumber
    print("Rotation H6: " + rotation_h6)
    rotations_page.click_ok()
    time.sleep(3)
    rotations_page.click_Active()
    time.sleep(4)
    assert rotationNumber in rotations_page.verify_first_rotation(), "Approved rotation not found on Active rotations page"


@allure.title('H9: Hospital processes rotation that does not fit unit schedule and does not overlap')
def test_hospital_process_rotation_fitNo_overlapNo(browser):
    home_page = homepageObjects(browser)
    rotations_page = hosp_myRotationsPage(browser)
    home_page.load()
    home_page.enterUsername(hospUser_email)
    home_page.enterPassword(hospUser_password)
    home_page.clickLogin()
    time.sleep(3)
    rotations_page.click_myRotations()
    rotations_page.click_viewRotations()
    rotations_page.click_pendingApprovals()
    rotations_page.click_process_fitNo_overlapNo()
    time.sleep(5)
    assert rotations_page.verify_message_process() == "This rotation does not fit the schedule for the unit."
    rotations_page.click_acceptRequest()
    global rotationNumber
    time.sleep(3)
    rotationNumber = rotations_page.get_rotationNumber()
    rotations_page.click_ok()
    time.sleep(3)
    rotations_page.click_Active()
    time.sleep(3)
    assert rotationNumber in rotations_page.verify_first_rotation(), "Approved rotation not found on Active rotations page"


@allure.title('A10: Admin resets rotation status')
def test_admin_resets_rotation(browser):
    home_page = homepageObjects(browser)
    rotations_page = school_myRotationsPage(browser)
    home_page.load()
    home_page.enterUsername(admin_username)
    home_page.enterPassword(admin_password)
    home_page.clickLogin()
    rotations_page.click_tabManage()
    rotations_page.click_optionManageDatabase()
    rotations_page.enter_rotationNumberEdit(rotation_h6)
    rotations_page.click_go()
    time.sleep(5)
    rotations_page.click_pending_approval()
    time.sleep(3)
    rotations_page.click_yes()
    time.sleep(3)
    rotations_page.click_ok()
    rotations_page.enter_rotationNumberEdit(rotation_h6)
    rotations_page.click_go()
    time.sleep(5)
    assert 'Current Status: Pending Approval' in rotations_page.verify_rotationStatus(), "Rotation status is not " \
                                                                                         "pending approval in " \
                                                                                         "rotation info "
    rotations_page.enter_rotationNumberEdit(rotation_h10)
    rotations_page.click_go()
    time.sleep(5)
    rotations_page.click_pending_approval()
    time.sleep(3)
    rotations_page.click_yes()
    time.sleep(3)
    rotations_page.click_ok()
    rotations_page.enter_rotationNumberEdit(rotation_h10)
    rotations_page.click_go()
    time.sleep(5)
    assert 'Current Status: Pending Approval' in rotations_page.verify_rotationStatus(), "Rotation status is not " \
                                                                                         "pending approval in " \
                                                                                         "rotation info "


@allure.title(
    'H10.1: Hospital processes rotation that fits unit schedule but overlaps with other rotations that get cancelled')
def test_hospital_process_rotation_fitYes_cancelOverlap(browser):
    home_page = homepageObjects(browser)
    rotations_page = hosp_myRotationsPage(browser)
    home_page.load()
    home_page.enterUsername(hospUser_email)
    home_page.enterPassword(hospUser_password)
    home_page.clickLogin()
    rotations_page.click_myRotations()
    rotations_page.click_viewRotations()
    rotations_page.click_pendingApprovals()
    rotations_page.click_process_fitNo_overlapYes()
    time.sleep(10)
    assert "The rotation that you are processing overlaps with active rotations" in rotations_page.verify_message_process()
    rotations_page.select_cancel_overlap("YES")
    rotations_page.click_acceptRequest()
    global rotationNumber
    time.sleep(3)
    rotationNumber = rotations_page.get_rotationNumber()
    rotations_page.click_ok()
    time.sleep(3)
    rotations_page.click_Active()
    time.sleep(3)
    assert rotations_page.verify_all_rotation(
        rotationNumber) == True, "Approved rotation not found on Active rotations page"
    rotations_page.click_cancelledBtn()
    time.sleep(3)
    assert rotations_page.verify_all_rotation(
        rotation_h5) == True, "Cancelled overlapping rotation not found on Declined rotations page"


@allure.title(
    'H6.1: Hospital processes rotation that does not fit unit schedule and overlaps with active rotation that gets cancelled')
def test_hospital_process_rotation_fitNo_cancelOverlap(browser):
    home_page = homepageObjects(browser)
    rotations_page = hosp_myRotationsPage(browser)
    rotations_school = school_myRotationsPage(browser)
    home_page.load()
    home_page.enterUsername(admin_username)
    home_page.enterPassword(admin_password)
    home_page.clickLogin()
    time.sleep(3)
    rotations_school.click_tabManage()
    rotations_school.click_optionManageDatabase()
    rotations_school.enter_rotationNumberEdit(rotation_h5)
    rotations_school.click_go()
    time.sleep(5)
    rotations_school.click_active_rotation()
    time.sleep(3)
    rotations_school.click_yes()
    time.sleep(3)
    rotations_school.click_ok()
    home_page.load()
    home_page.enterUsername(hospUser_email)
    home_page.enterPassword(hospUser_password)
    home_page.clickLogin()
    rotations_page.click_myRotations()
    rotations_page.click_viewRotations()
    rotations_page.click_pendingApprovals()
    rotations_page.click_process_fitNo_overlapNo()
    time.sleep(5)
    assert rotations_page.verify_message_process() == "The rotation you are processing does not fit the hospital " \
                                                      "schedule, and also overlapswith active rotation(s).", \
        "Message displayed during the processing of rotation is wrong. "
    rotations_page.select_cancel_overlap("YES")
    rotations_page.click_confirm()
    time.sleep(3)
    rotationNumber = rotations_page.get_rotationNumber()
    rotations_page.click_ok()
    time.sleep(3)
    rotations_page.click_Active()
    time.sleep(3)
    assert rotations_page.verify_all_rotation(
        rotationNumber) == True, "Approved rotation not found on Active rotations page"
    rotations_page.click_cancelledBtn()
    time.sleep(3)
    assert rotations_page.verify_all_rotation(
        rotation_h5) == True, "Cancelled overlapping rotation not found on Declined rotations page"
