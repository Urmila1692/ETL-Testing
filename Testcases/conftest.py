import pytest
from selenium import webdriver


@pytest.fixture # decorator
def demo_fixture(): # function
    print(f"\nThis is demo fixture, this will run first, before testcases") # First
    yield # after running the testcase before code will run
    print(f"\n Thi is demo fixture, this will run at last, after testcases") # End

# Browser--> open --> first
# Browser --> close --> end

# @pytest.fixture # decorator
# def browser_setup(): # function
#     print(f"\nBrowser Open")
#     driver = webdriver.Edge()
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     yield driver
#     driver.quit()
#     print("\nBrowser Close")

# Follow above code, need to change required browser name everytime, (that means you are change code everytime).
# Good practice is to have code, which is run according to your pytest command.
# e.g. --> pytest --browser edge


# Customize pytest command line
# pytest_addoption -->
# Adoption is the hookup function extending pytest framework features.
# Python adoption functions are used to pass command line arguments to pytest test and
# Here we are going to add --browser in command line argument, which is user define or custom argument.


def pytest_addoption(parser): # special name, same you have to use # parser --> to add customer argument
    parser.addoption("--browser") # add a new command line option called --browser
    # Here have we just define the "--browser" not assigned any value to it.


@pytest.fixture # decorator
def browser_setup(request): # function
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("\nOpening chrome browser")
        #driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        # Create an "options" object for Chrome.
        # We use it to control Chrome settings before the browser launches.

        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            # This turns OFF Chrome's "credentials service"
            # Chrome will not offer to save usernames/passwords.

            "profile.password_manager_enabled": False
            # This turns OFF Chrome's built-in Password Manager feature.
            # Password Manager related popups (Save password / breach warning) will not come.
        }
                                               )
        driver = webdriver.Chrome(options=chrome_options)
        # Launch Chrome using the above options.
        # So Chrome starts with password manager disabled and those popups are avoided.


    elif browser == "firefox":
        print("\nOpening firefox browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("\nOpening edge browser")
        driver = webdriver.Edge()
    elif browser == "headless":
        print("\nOpening chrome headless browser")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options = chrome_options)
    else:
        print("\nOpening Firefox browser")
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    print("\nBrowser Closed")
    driver.quit()

# Your task
# How to handle not secure site
# Incognito/ Private window
# Password save browser message --> done
# Browser handle thr Remote desktop

#Test Data
@pytest.fixture(params = [
    ("Credencetest@test.com", "Credence@123", "login_pass"), # All correct #
    ("Credencetest@test.com11", "Credence@123", "login_fail"), # username wrong #
    ("Credencetest@test.com", "Credence@1231", "login_fail"), # password wrong
    ("Credencetest@test.com1", "Credence@1231", "login_fail")  # username and password wrong

])
def credkart_login_data(request):
    return request.param