# -*- coding: utf-8 -*-
from model.users import Users

def test_add_user(app):
    old_users = app.users.get_users_list()
    user = Users(firstname="aaa", lastname="bbb")
    app.users.create(user)
    assert len(old_users) + 1 == app.users.count()
    new_users = app.users.get_users_list()
    old_users.append(user)
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)


def test_add_empty_user(app):
    old_users = app.users.get_users_list()
    user = Users(firstname="", lastname="")
    app.users.create(user)
    assert len(old_users) + 1 == app.users.count()
    new_users = app.users.get_users_list()
    old_users.append(user)
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)

