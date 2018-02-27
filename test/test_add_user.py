# -*- coding: utf-8 -*-
from model.users import Users

def test_add_user(app, db, json_users):
    user = json_users
    old_users = db.get_users_list()
    app.users.create(user)
    new_users = db.get_users_list()
    old_users.append(user)
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)
