import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_ohrm_login():

    username_tf=(By.XPATH, '//input[@placeholder="Username"]') ;
    password_tf=(By.XPATH, '//input[@placeholder="Password"]') ;
    login_button=(By.XPATH, '//button[text()=" Login "]') ;
    menu_button=(By.XPATH, '//p[@class="oxd-userdropdown-name"]') ;
    logout_button=(By.XPATH, '//a[contains(text(), "Logout")]') ;

    def __init__(self, driver):
        self.driver=driver ;
        self.wait=WebDriverWait(self.driver, 10) ;


    def test_url(self,url):
        self.driver.get(url) ;
        time.sleep(2) ;

    def test_enter_username(self,username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.username_tf)) ;
        self.driver.find_element(*Test_ohrm_login.username_tf).send_keys(username) ;

    def test_enter_password(self,password):
        self.driver.find_element(*Test_ohrm_login.password_tf).send_keys(password) ;

    def test_click_login(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.password_tf)) ;
        self.driver.find_element(*Test_ohrm_login.login_button).click() ;

    def test_login_status(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.menu_button)) ;
            self.driver.find_element(*Test_ohrm_login.menu_button) ;
            return True ;

        except:
            return False

    def test_click_menu_button(self):
        self.driver.find_element(*Test_ohrm_login.menu_button).click() ;

    def test_click_logout(self):
        self.driver.find_element(*Test_ohrm_login.logout_button).click();