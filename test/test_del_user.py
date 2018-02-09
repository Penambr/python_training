from model.users import Users


def test_delete_first_user(app):
    if app.users.count() == 0:
        app.users.create(Users(first_name="testuser", mobile="7", email="8", last_name="11", id="12"))
    old_users = app.users.get_users_list()
    app.users.delete_first_user()
    new_users = app.users.get_users_list()
    assert len(old_users) - 1 == len(new_users)
    old_users[0:1] = []
    assert old_users == new_users

