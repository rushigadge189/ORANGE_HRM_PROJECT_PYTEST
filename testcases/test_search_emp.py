import time

import allure
from allure_commons.types import AttachmentType

from pages.test_pages_oramgehrm import Test_ohrm_login
from pages.test_add_emp_pages import Test_Add_Emp
from pages.test_search_emp_pages import Test_Search_Emp
from utilities.ReadConfig import ReadConfig
from utilities.logger import LogGenerator

class Test_searchch_empemp():

    USERNAME=ReadConfig.getUserName() ;
    PASSWORD=ReadConfig.getPassword() ;

    log=LogGenerator.logger() ;

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("TITLE OF TEST CASE IS #3 ")
    @allure.issue("THIS IS THE ISSUE #3")
    @allure.story("THIS IS THE STORY #3")
    def test_search_emp_004(self,setup):

        self.log.info("TESTCASE TEST_SEARCH_EMP_004 IS STARTED") ;

        self.log.info("OPEN THE BROWSER") ;

        self.log.info("MAXI MIZE THE BROWSER") ;

        self.driver=setup ;

        self.obj=Test_ohrm_login(self.driver) ;

        self.log.info("NAVIGATING TO THE URL") ;
        self.obj.test_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") ;

        self.log.info("ENTERING THE USERNAME") ;
        self.obj.test_enter_username(self.USERNAME) ;

        self.log.info("ENTERING THE PASSWORD") ;
        self.obj.test_enter_password(self.PASSWORD) ;

        self.log.info("CLICK ON LOGIN BUTTON") ;
        self.obj.test_click_login() ;

        self.obj2=Test_Add_Emp(self.driver) ;

        self.log.info("CLCIK ONN THE PIM TAB") ;
        self.obj2.test_click_pim_tab() ;

        self.obj3=Test_Search_Emp(self.driver) ;

        self.log.info("SEARCHIN FOR EMPLOYEE") ;
        self.obj3.test_enter_search_emp("0294") ;

        self.log.info("CLCIK ON THE SEARCH BUTTON") ;
        self.obj3.test_click_search_button() ;

        time.sleep(3) ;

        print("DETAILS OF ADDED EMPLOYEE ARE FOLLOWING") ;

        self.log.info("CHECKING FOR THE STATUS") ;
        if(self.obj3.test_search_results()==True) :
            allure.attach(self.driver.get_screenshot_as_png(), name="test_search_emp_004_pass",attachment_type=AttachmentType.PNG) ;
            self.log.info("DETAILS OF EMPLOYEE ARE PRINTED") ;
            self.log.info("TAKING THE SCREENSHOT") ;
            self.log.info("TEST CASE IS PASSED") ;
            self.driver.save_screenshot("D:\\PYTHON CT15\\ORANGEH_PROJECT\\screenshots\\test_sarch_emp_004_pass.png") ;

            assert True ;

        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_search_emp_004-pass", attachment_type=AttachmentType.PNG) ;
            self.log.info("TEST CASE IS FAILED") ;
            self.driver.save_screenshot("D:\\PYTHON CT15\\ORANGEH_PROJECT\\screenshots\\test_sarch_emp_004_fail.png") ;

            assert False ;

        self.log.info("TESTCASE TEST_SEARCH_EMP_004 IS COMPLETED") ;