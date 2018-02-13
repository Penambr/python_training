from sys import maxsize

class Users:

    def __init__(self, first_name=None, id=None):
        self.first_name = first_name
        self.id = id
#        self.middle_name = middle_name
#        self.last_name = last_name
#        self.nick_name = nick_name
#        self.title = title
#        self.companyname = companyname
#        self.address = address
#        self.home = home
#        self.mobile = mobile
#        self.work = work
#        self.fax = fax
#        self.email = email

    def __repr__(self):
        return "%s:%s" % (self.id, self.first_name)

    def __eq__(self, other):
#        return self.id == other.id and self.first_name == other.first_name
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
