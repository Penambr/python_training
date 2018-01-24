
def test_edit_first_user(app):
    app.session.login(username="admin", password="secret")
    app.users.edit_first_user()
    app.sessionusers.logout()
