# -*- coding: utf-8 -*-
from model.users import Users

def test_add_user(app):
#    app.session.login(username="admin", password="secret")
    app.users.create(Users(firs_name="sdf", middle_name="sdfsd", last_name="sdfsdf", nick_name="sdfsd", title="sfdsd", companyname="sdfsd", address="sdfsdf", home="sdfsdf", mobile="sdfsdf",
                           work="fhgfdgh", fax="fjhfgd", email="dfs@fgd.com"))
#   app.session.logout()

def test_add_empty_user(app):
#    app.session.login(username="admin", password="secret")
    app.users.create(Users(firs_name="", middle_name="", last_name="", nick_name="", title="", companyname="", address="", home="", mobile="",
                           work="", fax="", email=""))
#    app.session.logout()