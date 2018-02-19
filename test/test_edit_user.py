from model.users import Users
from random import randrange

def test_edit_first_user_name(app):
    if app.users.count() == 0:
        app.users.create(Users(first_name="testuser"))
    old_users = app.users.get_users_list()
    index = randrange(len(old_users))
    user = Users(first_name="New user")
    user.id = old_users[index].id
    app.users.edit_user_by_index(index, user)
    new_users = app.users.get_users_list()
    assert len(old_users) == len(new_users)
    old_users[index] = user
#    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)
