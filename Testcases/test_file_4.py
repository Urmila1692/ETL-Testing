import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_004:

    @pytest.mark.web
    @pytest.mark.sanity

    def test_Credkart_Registration_007(self, browser_setup):
        import time

        driver = browser_setup
        driver.get("https://automation.credence.in/register")

        if driver.title == "CredKart":
            print(f"You are landed on correct page and its title is {driver.title}")
            import random
            value = random.randint(1000, 10000)

            # Enter Username
            username_value = f"Credence_user_{value}"
            username = driver.find_element(By.XPATH, "//input[@id='name']")
            username.send_keys(username_value)

            # Enter Email
            email = driver.find_element(By.XPATH, "//input[@id='email']")
            email.send_keys(f"Credence_user_{value}@gmail.com")

            # Enter Password
            password = driver.find_element(By.XPATH, "//input[@id='password']")
            password.send_keys("Credence_user_101@123")

            # Enter  Confirm Password
            confirm_password = driver.find_element(By.XPATH, "//input[@id='password-confirm']")
            confirm_password.send_keys("Credence_user_101@123")

            time.sleep(2)
            # Click on register button
            register_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            register_button.click()

            time.sleep(3)

            wait = WebDriverWait(driver, 5)
            try:
                wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
                element = driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
                print("User Registration Successful")
                #driver.save_screenshot(f"User Registration Successful_{username_value}.png")
                # assert True, "User Registration Successful"
            except:
                print("User Registration Fail")
                #driver.save_screenshot(f"User Registration Fail_{username_value}.png")
                assert False, "User Registration Fail"
        else:
            print(f" You are landed on wrong page and its title is {driver.title}")


    @pytest.mark.web
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Credkart_login_008(self, browser_setup ):

        # driver = webdriver.Firefox()
        driver = browser_setup
        driver.get("https://automation.credence.in/login")

        if driver.title == "CredKart":
            print(f"You are landed on correct page and its title is {driver.title}")

            email_id = "Credencetest@test.com"
            pass_word = "Credence@123"

            # Enter Username

            email = driver.find_element(By.XPATH, "//input[@id='email']")
            email.send_keys(email_id)

            # Enter Password
            password = driver.find_element(By.XPATH, "//input[@id='password']")
            password.send_keys(pass_word)

            # Click on Login button
            login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()

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

            except:
                print("User Login Fail")
                #driver.save_screenshot(f"User Login Fail_{email_id}.png")
                assert False, "User Login Fail"
        else:
            print(f" You are landed on wrong page and its title is {driver.title}")

