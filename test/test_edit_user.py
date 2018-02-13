from model.users import Users

def test_edit_first_user_name(app):
    old_users = app.users.get_users_list()
    user = Users(first_name="New user")
    user.id = old_users[0].id
    app.users.edit_first_user(user)
    new_users = app.users.get_users_list()
    assert len(old_users) == len(new_users)
    old_users[0] = user
#    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)
