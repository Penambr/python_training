from model.users import Users
import re

class UserHelper:

    def __init__(self, app):
        self.app = app

    def open_webpage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_name("searchform")) > 0):
            wd.get("http://localhost/addressbook/")

    def open_user_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_link_text("add new").click()

    def fill_users_form(self, user):
        wd = self.app.wd
        self.change_field_value("firstname", user.firstname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, users):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.open_user_creation()
        wd.find_element_by_name("firstname").send_keys(users.firstname)
        wd.find_element_by_name("lastname").send_keys(users.lastname)
        wd.find_element_by_name("home").send_keys(users.homephone)
        wd.find_element_by_name("mobile").send_keys(users.mobilephone)
        wd.find_element_by_name("work").send_keys(users.workphone)
        wd.find_element_by_name("phone2").send_keys(users.secondaryphone)
        wd.find_element_by_name("email").send_keys(users.email)
        wd.find_element_by_name("email2").send_keys(users.email2)
        wd.find_element_by_name("email3").send_keys(users.email3)
        wd.find_element_by_name("address").send_keys(users.address)

        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.user_cache = None

    def select_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def click_edit_user_by_index(self, index):
        wd = self.app.wd
        self.app.open_webpage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def delete_first_user(self):
        self.delete_user_by_index(0)

    def delete_user_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_user_by_index(index)
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        wd.find_element_by_link_text("home").click()
        self.user_cache = None

    def edit_user_by_index(self, index, new_user_data):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.click_edit_user_by_index(index)
        self.fill_users_form(new_user_data)
        wd.find_element_by_name("update").click()
        self.return_to_users_page()
        self.user_cache = None

    def return_to_users_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))

    user_cache = None

    def get_users_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.open_webpage()
            self.user_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.user_cache.append(Users(firstname=firstname, lastname=lastname, id=id, address=address,
                                             all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.user_cache)

    def open_users_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_webpage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_users_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_webpage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_users_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_users_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Users(firstname=firstname,lastname=lastname, id=id, homephone=homephone, workphone=workphone,address=address,
                     mobilephone=mobilephone, secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)

    def get_users_from_view_page(self, index):
        wd = self.app.wd
        self.open_users_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Users(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)
