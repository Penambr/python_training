from model.users import Users

def test_edit_first_user(app):
    if app.users.count() == 0:
        app.users.create(Users(first_name="testuser", middle_name="1", nick_name="2", title="3", companyname="4", address="5", home="6", mobile="7", email="8", fax="9", work="10", last_name="11"))
    app.users.edit_first_user()
