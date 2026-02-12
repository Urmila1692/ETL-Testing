import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.Excel_Utilities import Excel_methods # imported user define class


class Test_007:

    excel_file_path = r"D:\Batch Notes\Automation Testing Dec 2025\03. Python_Pytest_Basic\Test_Data\Credkart_Test_Data.xlsx"
    sheet_name = "login_data"

    @pytest.mark.web
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Credkart_login_excel_016(self, browser_setup ):

        driver = browser_setup
        driver.get("https://automation.credence.in/login")

        rows = Excel_methods.get_count_rows(self.excel_file_path,self.sheet_name)
        print(f"rows in excel--> {rows}")

        result_list = []
        for i in range(2, rows+1):
            email_id = Excel_methods.read_data_from_excel(self.excel_file_path,self.sheet_name,i,2)
            password_data = Excel_methods.read_data_from_excel(self.excel_file_path, self.sheet_name, i, 3)
            expected_result = Excel_methods.read_data_from_excel(self.excel_file_path, self.sheet_name, i, 4)

            print(f"email_id-->{email_id}")
            print(f"password-->{password_data}")
            print(f"expected_result-->{expected_result}")

            # Enter Username
            email = driver.find_element(By.XPATH, "//input[@id='email']")
            email.send_keys(email_id) # correct

            # Enter Password
            password = driver.find_element(By.XPATH, "//input[@id='password']")
            password.send_keys(password_data) # inorrect

            # Click on Login button
            login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            time.sleep(2)
            wait = WebDriverWait(driver, 5)
            try:
                wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
                element = driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
                print("User Login Successful")
                #driver.save_screenshot(f"User Login Successful_{email_id}.png")
                menu = driver.find_element(By.XPATH, "//a[@role='button']")
                menu.click()
                logout = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
                logout.click()
                actual_result = 'login_pass'

            except:
                print("User Login Fail")
                #driver.save_screenshot(f"User Login Fail_{email_id}.png")
                #assert False, "User Login Fail"
                actual_result = 'login_fail'


            if actual_result ==expected_result:
               result_list.append("Pass")
               test_case_status = "Pass"
            else:
                result_list.append("Fail")
                test_case_status = "Fail"

            Excel_methods.write_data_from_excel(self.excel_file_path, self.sheet_name, i, 5, actual_result)
            Excel_methods.write_data_from_excel(self.excel_file_path, self.sheet_name, i, 6, test_case_status)
            driver.get("https://automation.credence.in/login")

        print(f"result_list--> {result_list}")
        if "Fail" not in result_list:
            print("Test Case Passed")
        else:
            print("Test Case Failed")
            assert False

