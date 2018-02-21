import re

def test_fields_on_homepage(app):
    users_from_home_page = app.users.get_users_list()[0]
    users_from_edit_page = app.users.get_users_info_from_edit_page(0)
    app.users.click_edit_user_by_index(0)
    assert users_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(users_from_edit_page)
    assert users_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(users_from_edit_page)
    assert users_from_home_page.address == users_from_edit_page.address
    assert users_from_home_page.firstname == users_from_edit_page.firstname
    assert users_from_home_page.lastname == users_from_edit_page.lastname

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(users):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [users.homephone, users.mobilephone, users.workphone, users.secondaryphone]))))

def merge_emails_like_on_home_page(users):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [users.email, users.email2, users.email3]))))
