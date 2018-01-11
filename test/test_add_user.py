# -*- coding: utf-8 -*-
import pytest
from model.users import Users
from fixture.userapplication import Userapplication

@pytest.fixture
def app(request):
    fixture = Userapplication()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.login(username="admin", password="secret")
    app.create_user(Users(firs_name="sdf", middle_name="sdfsd", last_name="sdfsdf", nick_name="sdfsd", title="sfdsd", companyname="sdfsd", address="sdfsdf", home="sdfsdf", mobile="sdfsdf",
                         work="fhgfdgh", fax="fjhfgd", email="dfs@fgd.com"))
    app.logout()


def test_add_empty_user(app):
    app.login(username="admin", password="secret")
    app.create_user(Users(firs_name="", middle_name="", last_name="", nick_name="", title="", companyname="", address="", home="", mobile="",
                         work="", fax="", email=""))
    app.logout()