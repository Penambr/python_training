from model.group import Group
from model.users import Users
def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def test_users_list(app, db):
    ui_list = app.users.get_users_list()
    def clean(users):
        return Users(id=id, firstname=users.firstname.strip())
    db_list = map(clean, db.get_users_list())
    assert sorted(ui_list, key=Users.id_or_max) == sorted(db_list, key=Users.id_or_max)