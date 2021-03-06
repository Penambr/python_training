from model.users import Users
import random

def test_delete_some_user(app, db, check_ui):
    if len(db.get_users_list()) == 0:
        app.users.create(Users(firstname="testuser"))
    old_users = db.get_users_list()
    user = random.choice(old_users)
    app.users.delete_user_by_id(user.id)
    new_users = db.get_users_list()
    assert len(old_users) - 1 == len(new_users)
    old_users.remove(user)
    assert old_users == new_users
    if check_ui:
        assert sorted(new_users, key=Users.id_or_max) == sorted(app.group.get_users_list(), key=Users.id_or_max)


#from model.users import Users
#from random import randrange
#
#def test_delete_some_user(app):
#    if app.users.count() == 0:
#        app.users.create(Users(firstname="testuser"))
#    old_users = app.users.get_users_list()
#    index = randrange(len(old_users))
#    app.users.delete_user_by_index(index)
#    new_users = app.users.get_users_list()
#    assert len(old_users) - 1 == len(new_users)
#    old_users[index:index+1] = []
