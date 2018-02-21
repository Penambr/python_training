import re

def test_phones_on_homepage(app):
    users_from_home_page = app.users.get_users_list()[0]
    users_from_edit_page = app.users.get_users_info_from_edit_page(0)
    assert users_from_home_page.homephone == clear(users_from_edit_page.homephone)
    assert users_from_home_page.workphone == clear(users_from_edit_page.workphone)
    assert users_from_home_page.mobilephone == clear(users_from_edit_page.mobilephone)
    assert users_from_home_page.secondaryphone == clear(users_from_edit_page.secondaryphone)

def test_phones_on_users_view_page(app):
    users_from_view_page = app.users.get_users_from_view_page(0)
    users_from_edit_page = app.users.get_users_info_from_edit_page(0)
    assert users_from_view_page.homephone == users_from_edit_page.homephone
    assert users_from_view_page.workphone == users_from_edit_page.workphone
    assert users_from_view_page.mobilephone == users_from_edit_page.mobilephone
    assert users_from_view_page.secondaryphone == users_from_edit_page.secondaryphone

def clear(s):
    return re.sub("[() -]", "", s)
