import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_005:

    @pytest.mark.web
    @pytest.mark.regression
    def test_Credkart_Checkout_009(self, browser_setup):
        import time

        driver = browser_setup
        driver.get("https://automation.credence.in/login")
        driver.maximize_window()
        driver.implicitly_wait(5)

        # login
        email_id = "Credence_user_1@gmail.com"
        pass_word = "Credence_user_101@123"

        # Enter email
        email = driver.find_element(By.XPATH, "//input[@id='email']")
        email.send_keys(email_id)

        # Enter Password
        password = driver.find_element(By.XPATH, "//input[@id='password']")
        password.send_keys(pass_word)

        # Click on Login button
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Click on Product1
        product1 = driver.find_element(By.XPATH, "//h3[normalize-space()='Playstation 4']")
        product1.click()

        #  add to cart-->
        add_cart = driver.find_element(By.XPATH, "//input[@value='Add to Cart']")
        add_cart.click()

        # CLick on continue_shopping_button
        continue_shopping_button = driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']")
        continue_shopping_button.click()

        # click on product2
        product2 = driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']")
        product2.click()

        # add to cart
        add_cart = driver.find_element(By.XPATH, "//input[@value='Add to Cart']")
        add_cart.click()

        # Checkout
        checkout = driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']")
        checkout.click()

        # Enter first_name
        first_name = driver.find_element(By.XPATH, "//input[@id='first_name']")
        first_name.send_keys("Pooja")

        # Enter last_name
        last_name = driver.find_element(By.XPATH, "//input[@id='last_name']")
        last_name.send_keys("P")

        # Enter Phone
        phone = driver.find_element(By.XPATH, "//input[@id='phone']")
        phone.send_keys("9091929355")

        # Enter address
        address = driver.find_element(By.XPATH, "//textarea[@id='address']")
        address.send_keys("Global Business hub, Kharadi, Pune, MH ")

        # Enter Zip_code
        Zip_code = driver.find_element(By.XPATH, "//input[@id='zip']")
        Zip_code.send_keys("411043")

        # Select State
        select_state = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
        select_state.select_by_visible_text("Pune")

        # Enter Owner
        Owner = driver.find_element(By.XPATH, "//input[@id='owner']")
        Owner.send_keys("Pooja")

        # Enter Cvv
        Cvv = driver.find_element(By.XPATH, "//input[@id='cvv']")
        Cvv.send_keys("043")

        # Enter card number
        card_number = driver.find_element(By.XPATH, "//input[@id='cardNumber']")
        card_number.send_keys("5281")
        card_number.send_keys("0370")
        card_number.send_keys("4891")
        card_number.send_keys("6168")

        # Select Year
        year = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        year.select_by_visible_text("2026")

        # Select Month
        month = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        month.select_by_visible_text("June")

        # Click Continue_checkout
        Continue_checkout = driver.find_element(By.XPATH, "//button[@id='confirm-purchase']")
        Continue_checkout.click()

        # Order Number
        order_number = driver.find_element(By.XPATH, "//p[@class='w-lg-50 mx-auto']")
        print(order_number.text)

    @pytest.mark.web
    @pytest.mark.regression
    def test_Credence_google_search_010(self, browser_setup):
        import time

        from selenium.webdriver import Keys
        from selenium.webdriver.common.by import By

        driver = browser_setup
        driver.get("https://www.google.com/")

        # Search Box
        search_box = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
        search_box.send_keys("Credence IT, Pune", Keys.ENTER)


    @pytest.mark.web
    @pytest.mark.sanity
    def  test_Credence_site_011 (self,browser_setup):
        import time

        from selenium import webdriver
        from selenium.webdriver import Keys
        from selenium.webdriver.common.by import By

        driver = browser_setup
        driver.get("https://credence.in/")

        call_button = driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']")
        call_button.click()

        contacts_count = driver.find_elements(By.XPATH, "/html/body/div[5]/div/div/p/a")
        print(f" len(contacts_count) -- >{len(contacts_count)} ")

        contact_list = []
        for i in range(1, (len(contacts_count) + 1)):
            contact = driver.find_element(By.XPATH, f"/html/body/div[5]/div/div/p/a[{i}]").text
            contact_list.append(contact)

        print(f"contact_list-->{contact_list}")

        num1 = '+91 8237916162'
        if num1 in contact_list:
            print(f"{num1}-->Number found")
        else:
            print(f"{num1}-->Number not found")
            assert False



