import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_006:

    @pytest.mark.web
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Credkart_login_params_015(self, browser_setup, credkart_login_data ):

        email_id = credkart_login_data[0]
        password_data = credkart_login_data[1]
        expected_result = credkart_login_data[2]

        print(f"email_id-->{email_id}")
        print(f"password-->{password_data}")
        print(f"expected_result-->{expected_result}")

        driver = browser_setup
        driver.get("https://automation.credence.in/login")
        if driver.title == "CredKart":
            print(f"You are landed on correct page and its title is {driver.title}")


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
        else:
            print(f" You are landed on wrong page and its title is {driver.title}")

        if actual_result == expected_result :
            print("Testcase Pass")
            assert True
        else:
            print("Testcase Fail")
            assert False


