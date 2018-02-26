# -*- coding: utf-8 -*-
from model.users import Users

def test_add_user(app, json_users):
    user = json_users
    old_users = app.users.get_users_list()
    app.users.create(user)
    assert len(old_users) + 1 == app.users.count()
    new_users = app.users.get_users_list()
    old_users.append(user)
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)
