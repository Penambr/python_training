
def test_delete_first_user(app):
#    app.sessionusers.login(username="admin", password="secret")
    app.users.delete_first_user()
#    app.sessionusers.logout()
