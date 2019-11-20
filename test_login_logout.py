from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

driver=webdriver.Chrome()

def test_all_null():
    driver.get('http://localhost:8000/admin/login/?next=/admin/')
    elem_name = driver.find_element_by_name("username")
    elem_name.clear()
    elem_name.send_keys("")
    elem_password = driver.find_element_by_name("password")
    elem_password.clear()
    elem_password.send_keys("")
    elem_password.send_keys(Keys.RETURN)
    assert "Log in | Django site admin" in driver.title

def test_password_null():
    driver.get('http://localhost:8000/admin/login/?next=/admin/')
    elem_name = driver.find_element_by_name("username")
    elem_name.clear()
    elem_name.send_keys("tanjunwu")
    elem_password = driver.find_element_by_name("password")
    elem_password.clear()
    elem_password.send_keys("")
    elem_password.send_keys(Keys.RETURN)
    assert "Log in | Django site admin" in driver.title

def test_wrong_username():
    driver.get('http://localhost:8000/admin/login/?next=/admin/')
    elem_name = driver.find_element_by_name("username")
    elem_name.clear()
    elem_name.send_keys("tanjunuu")
    elem_password = driver.find_element_by_name("password")
    elem_password.clear()
    elem_password.send_keys("T0016860i")
    elem_password.send_keys(Keys.RETURN)
    assert "Log in | Django site admin" in driver.title

def test_wrong_password():
    driver.get('http://localhost:8000/admin/login/?next=/admin/')
    elem_name = driver.find_element_by_name("username")
    elem_name.clear()
    elem_name.send_keys("tanjunwu")
    elem_password = driver.find_element_by_name("password")
    elem_password.clear()
    elem_password.send_keys("assdsd")
    elem_password.send_keys(Keys.RETURN)
    assert "Log in | Django site admin" in driver.title

def test_username_case():
    driver.get('http://localhost:8000/admin/login/?next=/admin/')
    elem_name = driver.find_element_by_name("username")
    elem_name.clear()
    elem_name.send_keys("Tanjunwu")
    elem_password = driver.find_element_by_name("password")
    elem_password.clear()
    elem_password.send_keys("T0016860i")
    elem_password.send_keys(Keys.RETURN)
    assert "Log in | Django site admin" in driver.title

def test_password_case():
    driver.get('http://localhost:8000/admin/login/?next=/admin/')
    elem_name = driver.find_element_by_name("username")
    elem_name.clear()
    elem_name.send_keys("tanjunwu")
    elem_password = driver.find_element_by_name("password")
    elem_password.clear()
    elem_password.send_keys("t0016860i")
    elem_password.send_keys(Keys.RETURN)
    assert "Log in | Django site admin" in driver.title

def test_login_success():
    driver.get('http://localhost:8000/admin/login/?next=/admin/')
    elem_name = driver.find_element_by_name("username")
    elem_name.clear()
    elem_name.send_keys("tanjunwu")
    elem_password = driver.find_element_by_name("password")
    elem_password.clear()
    elem_password.send_keys("T0016860i")
    elem_password.send_keys(Keys.RETURN)
    assert "Site administration | Django site admin" in driver.title

def test_logout():
    #driver.findElement(Keys.linkText("Log out")).click()
    link = driver.find_element_by_xpath("//a[@href=' /admin/logout/']")
    link.click()
    assert "Logged out | Django site admin" in driver.title
