"""
This file contains all the configurable variables used
by the test cases.
"""

import random

randNum = str(random.randrange(100000, 999999))


def generateRandNum(self):
    self.randNum = str(random.randrange(100000, 999999))


# student_username = "rob.stark." + str(randNum) + "@email.com"
# student_password = "Robstark123"
admin_username = "admin@rotationmanager.com"
admin_password = "adminyou22"
crm_firstname = "CRM_User_" + randNum
crm_lastname = "Automation"
school_name = "School Automation " + randNum
campus_name = "Campus Automation " + randNum
discipline_name = "Discipline Automation " + randNum
phone_number = "123456789" + randNum
crm_email = "crm.user.email" + randNum + "@mailinator.com"
crm_password = "Password1"
hospital_name = "Hospital Automation " + randNum
discipline1 = "Discipline1 Automation " + randNum
discipline2 = "Discipline2 Automation " + randNum
discipline3 = "Discipline3 Automation " + randNum
discipline4 = "Discipline4 Automation " + randNum
discipline1_speciality1 = "Discipline1 Speciality1 Automation " + randNum
discipline1_speciality2 = "Discipline1 Speciality2 Automation " + randNum
discipline2_speciality1 = "Discipline2 Speciality1 Automation " + randNum
discipline2_speciality2 = "Discipline2 Speciality2 Automation " + randNum
discipline3_speciality1 = "Discipline3 Speciality1 Automation " + randNum
discipline3_speciality2 = "Discipline3 Speciality2 Automation " + randNum
discipline4_speciality1 = "Discipline4 Speciality1 Automation " + randNum
discipline4_speciality2 = "Discipline4 Speciality2 Automation " + randNum
hospUser_firstname = "Hospital_User_" + randNum
hospUser_lastname = "Automation"
hospUser_email = "hospital.user.email" + randNum + "@mailinator.com"
hospUser_password = "Password1"
manage_reqName = "Requirement Automation " + randNum
manage_shortForm = "ReqAuton"
manage_description = "Requirement Description Automation "
multiple_reqName = "Multiple Automation " + randNum
multiple_shortForm = "MulReqAuton"
multiple_description = "Multiple Requirement Description Automation "
read_mand = "Yes"
read_document_name = "Automation document"
school_price = '20.00'
subscription_period = "2"
school_price_assert = '$20.00'
renewal_price = '10.00'
school_discpline = school_name + " - " + discipline_name
school_discpline_assert = school_name + "-" + discipline_name
school_campus_discipline = school_name + " - " + campus_name + " - " + discipline_name
num_of_license = "10"
student_license_fname = "Student"
student_license_lname = "License"
student_license_email = "student.license.email" + randNum + "@mailinator.com"
student_license_email_edited = "student_license_edited_" + randNum + "@mailinator.com"
student_license_password = "Password1"
student_license_password_new = "Password2"
student_regwith_credit_fname = "Student"
student_regwith_credit_lname = "Credit"
student_credit_email = "student.credit.email" + randNum + "@mailinator.com"
student_credit_password = "Password1"
instructor_fname = "Instructor_" + randNum
instructor_lname = "Automation"
instructor_email = "instructor.user.email" + randNum + "@mailinator.com"
instructor_password = "Password1"
documentName_readRequirement = "Read Requirement " + randNum
crm_gmail_username = "crm.user.email@gmail.com"
crm_gmail_password = "Password!23"
hospital_gmail_username = "hospital.user.email@gmail.com"
hospital_gmail_password = "Password!23"
