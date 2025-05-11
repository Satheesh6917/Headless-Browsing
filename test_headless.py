import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By

import time

# preconditions
login_url = "https://www.guvi.in/"
signin_url = "https://www.guvi.in/sign-in/"
login_title = "GUVI"
Email = "satheeshkanna441@gmail.com"
Password = "Bakunamatata@123"
new_url = "https://www.guvi.in/courses/?current_tab=myCourses"
loggedin_url = "My Courses"

#Now I am going to setup browser using fixture method
@pytest.fixture()
def validate():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless--")
    driver = webdriver.Chrome(options=options)
    driver.get(login_url)
    driver.maximize_window()
    # assert driver.title == login_title, "There is a title mismatch"
    yield driver
    driver.quit()

# Calling the above fixture to this below function. I used ID's to locate web elements for the given url
def test_signin(validate):
    driver = validate
    time.sleep(5)
    Login_button = driver.find_element(By.ID, "login-btn").click()
    assert driver.current_url == signin_url, "Invalid URL provied"
    driver.find_element(By.ID, "email").send_keys(Email)
    driver.find_element(By.ID, "password").send_keys(Password)
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(5)
    assert driver.current_url == new_url, "Invalid URL after login"
    assert loggedin_url in driver.page_source, "User is not logged in"
