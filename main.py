from configparser import ConfigParser
from selenium import webdriver
from Manage_pack import Login_page,Create_Pack,Update_pack,Assign_pack,View_Pack
from Manage_User import Create_User,Update_User,Assign_Pack_To_User
from Manage_Control import Evaluvate_Answer_Sheets,Manage_Consent,Admin_Exam_Result_Review
from Manage_Corporate import Manage_Corporate,Manage_Corporate_Course


def main():
    config = ConfigParser()
    config.read("Manage_Pack/my.properties")  # Ensure the correct path to properties file

    if not config.has_section('ok'):
        raise ValueError("Section 'ok' not found in the configuration file.")
    if not config.has_option('ok', 'url'):
        raise ValueError("Option 'url' not found in section 'ok' of the configuration file.")

    driver = webdriver.Chrome()
    driver.maximize_window()
    url = config.get('ok', 'url')
    if url:
        driver.get(url)
        login_page = Login_page.Log_in(driver)
        login_page.login()
        #create_pack = Create_Pack.create(driver)
        #create_pack.create_New_pack()
        #update_pack = Update_pack.Update(driver)
        #update_pack.Update_Pack()
        #assign_pack = Assign_pack.Assign(driver)
        #assign_pack.assign_pack()
        #view_pack = View_Pack.View(driver)
        #view_pack.Views()
        #create_user=Create_User.CreateUser(driver)
        #create_user.create_user()
        # create_user.Multiple_user()
        # update_user=Update_User.Update_User(driver)
        # update_user.Update_User()
        # assign=Assign_Pack_To_User.Assign_Pack_To_User(driver)
        # assign.Assign_Pack_To_User()
        # Evaluate=Evaluvate_Answer_Sheets.Evaluate_answer_sheet(driver)
        # Evaluate.EValuate_sheet()
        # Admin_Exam=Admin_Exam_Result_Review.Admin_exam_Review(driver)
        # Admin_Exam.Result_Review()
        # Admin_Exam.search_by_Subject()
        # manage_constant=Manage_Consent.Manage_Consent(driver)
        # manage_constant.ManageConsent()
        # manage_corporate=Manage_Corporate.create_Corporate(driver)
        # manage_corporate.create_New_pack()
        # manage_corporate.edit_Corporate()
        manage_corporate_course=Manage_Corporate_Course.Manage_Corporate_Course(driver)
        manage_corporate_course.Edit_Course()


    driver.quit()

if __name__ == "__main__":
    main()
