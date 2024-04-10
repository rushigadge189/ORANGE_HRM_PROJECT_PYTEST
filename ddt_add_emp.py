import time

import allure

from pages.test_pages_oramgehrm import Test_ohrm_login
from pages.test_add_emp_pages import Test_Add_Emp
from utilities.ReadConfig import ReadConfig
from utilities.logger import LogGenerator
from utilities import XUTilies
class Test_Ddt_add_emp():

    USERNAME=ReadConfig.getUserName();
    PASSWORD=ReadConfig.getPassword();

    log=LogGenerator.logger() ;

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("TITLE OF THE TEST CASE #4")
    @allure.story("THIS IS THE STORY #4")
    @allure.issue("THIS IS THE ISSUE #4")
    def test_ddt_hrm_add_005(self, setup):

        self.log.info("TESTCASE DDT_HRM_ADD_005 IS STARTED") ;

        self.log.info("OPENING THE BROWSER") ;

        self.log.info("MAXIMIZING THE WINDOW") ;

        self.driver=setup ;

        self.lp=Test_ohrm_login(self.driver) ;


        self.log.info("NAVIGATION TO HE URL") ;
        self.lp.test_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") ;

        self.log.info("ENTERING THE USERNAME") ;
        self.lp.test_enter_username(self.USERNAME) ;

        self.log.info("ENTERING THE PASSWORD") ;
        self.lp.test_enter_password(self.PASSWORD) ;

        self.log.info("CLICK ON LOGIN BUTTON") ;
        self.lp.test_click_login() ;

        self.ae=Test_Add_Emp(self.driver) ;

        path="D:\\PYTHON CT15\\ORANGEH_PROJECT\\testdata\\OHRM_DDT.xlsx" ;

        rows=XUTilies.getRowCount(path, 'Sheet1') ;

        for r in range(2, rows+1):

            first_name=XUTilies.readData(path, 'Sheet1', r, 1) ;
            middle_name=XUTilies.readData(path, 'Sheet1', r, 2) ;
            last_name=XUTilies.readData(path, 'Sheet1', r, 3) ;

            self.log.info("CLCIK ON THE PIM TAB") ;
            self.ae.test_click_pim_tab() ;

            self.log.info("CLCIK ON ADD BUTTON") ;
            self.ae.test_click_add_button() ;

            self.log.info("ENTERING THE FIRST NAME") ;
            self.ae.test_ebter_first_name(first_name) ;

            self.log.info("ENTERING THE MIDDLE NAME") ;
            self.ae.test_enter_middle_name(middle_name) ;

            self.log.info("ENTERING THE LAST NAME") ;
            self.ae.test_enter_last_name(last_name) ;

            self.log.info("FETCHING EMPLOYEE ID") ;
            self.ae.test_get_emp_id_value() ;

            self.log.info("UPLOADING PROFILE PICTURE") ;
            self.ae.test_upload_img() ;
            time.sleep(2) ;

            self.log.info("CLICKING ON SAVE BUTTON") ;
            self.ae.test_click_save_button() ;

            self.log.info("CHECKING FOR THE SUCCESS MESSAGE") ;
            if(self.ae.test_print_success_msg()==True):
                print("\nEMPLOYEE ADDED SUCCESSFULLY") ;
                XUTilies.writeData(path, 'Sheet1', r, 4, 'EMP_ADDED') ;
                self.log.info("TAKING SCREENSHOT") ;
                self.driver.save_screenshot("D:\\PYTHON CT15\\ORANGEH_PROJECT\\\screenshots\\test_ddt_005_pass.png") ;

                assert True ;
            else:
                print("\nINVALID OPERATION") ;
                XUTilies.writeData(path, 'Sheet1', r, 4, "ERROR") ;
                self.log.info("TAKING SCREENSHOT") ;
                self.driver.save_screenshot("D:\\PYTHON CT15\\ORANGEH_PROJECT\\\screenshots\\test_ddt_005_fail.png") ;

                assert False ;

            self.log.info("TESTCASE DDT_HRM_ADD_005 IS COMPLETED");