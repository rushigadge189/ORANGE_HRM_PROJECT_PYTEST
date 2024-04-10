import time

from pynput.keyboard import Controller, Key
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Test_Add_Emp():
    pim_tab_xp=(By.XPATH, "//span[normalize-space()='PIM']") ;
    add_button_xp=(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]') ;
    firtname_tf_xp=(By.XPATH, '//input[@name="firstName"]') ;
    middlename_tf_xp=(By.XPATH, '//input[@name="middleName"]') ;
    lastname_tf_xp=(By.XPATH, '//input[@name="lastName"]') ;
    upload_icon_xp=(By.XPATH, '//i[@class="oxd-icon bi-plus"]') ;
    save_button_xp=(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]') ;
    success_msg_xp=(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']")
    get_id_xp=(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/input[1]')

    def __init__(self,driver):
        self.driver=driver ;

    def test_click_pim_tab(self):
        self.driver.find_element(*Test_Add_Emp.pim_tab_xp).click() ;

    def test_click_add_button(self):
        self.driver.find_element(*Test_Add_Emp.add_button_xp).click() ;

    def test_ebter_first_name(self,firstename):
        self.driver.find_element(*Test_Add_Emp.firtname_tf_xp).send_keys(firstename) ;

    def test_enter_middle_name(self,middlename):
        self.driver.find_element(*Test_Add_Emp.middlename_tf_xp).send_keys(middlename) ;

    def test_enter_last_name(self,lastname):
        self.driver.find_element(*Test_Add_Emp.lastname_tf_xp).send_keys(lastname) ;

    def test_get_emp_id_value(self):
        emp_id123=self.driver.find_element(*Test_Add_Emp.get_id_xp).get_attribute("value") ;
        print("\nEmployee ID", emp_id123) ;

    def test_upload_img(self):
        self.driver.find_element(*Test_Add_Emp.upload_icon_xp).click() ;
        time.sleep(2) ;
        keyboard=Controller() ;
        keyboard.type("D:\\PYTHON CT15\\ORANGEH_PROJECT\\testdata\\EMPLOYEE.png") ;
        time.sleep(2) ;
        keyboard.press(Key.enter) ;
        time.sleep(2) ;
        keyboard.release(Key.enter) ;
        time.sleep(2) ;

    def test_click_save_button(self):
        self.driver.find_element(*Test_Add_Emp.save_button_xp).click() ;
        time.sleep(1) ;

    def test_print_success_msg(self):
        try:
            success_msg=self.driver.find_element(*Test_Add_Emp.success_msg_xp).text ;
            print("\nTEXT AFTER ADDING EMPLOYEE") ;
            print("\n",success_msg) ;
            return True ;

        except NoSuchElementException:
            return False ;
