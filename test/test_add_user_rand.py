# -*- coding: utf-8 -*-
from model.users import Users

import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits(prefix, maxlen):
    digits = string.digits
    return prefix + "".join([random.choice(digits) for i in range(random.randrange(maxlen))])


testdata = [Users(firstname="", lastname="", homephone="", workphone="",
                  mobilephone="", secondaryphone="", address="", email="", email2="", email3="", id=None)] + [
    Users(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
          homephone=random_digits("home", 20), workphone=random_digits("work", 20),
          mobilephone=random_digits("mobile", 20), secondaryphone=random_digits("phone2", 20),
          address=random_string("address", 10), email=random_string("email", 10), email2=random_string("email2", 10),
          email3=random_string("email3", 10))
    for i in range(5)
]

@pytest.mark.parametrize("users", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, users):
    old_users = app.users.get_users_list()
    app.users.create(users)
    assert len(old_users) + 1 == app.users.count()
    new_users = app.users.get_users_list()
    old_users.append(users)
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)
