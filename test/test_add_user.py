# -*- coding: utf-8 -*-
from model.users import Users

def test_add_user(app):
    old_users = app.users.get_users_list()
    user = Users(first_name="sdf", id="id")
    app.users.create(user)
    new_users = app.users.get_users_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)


#def test_add_empty_user(app):
#    app.users.create(Users(first_name="", middle_name="", last_name="", nick_name="", title="", companyname="", address="", home="", mobile="",
#                           work="", fax="", email=""))


#last_name="sdfsdf", mobile="79123245678", email="1@1.com",