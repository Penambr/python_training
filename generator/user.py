from model.users import Users
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/users.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits(prefix, maxlen):
    digits = string.digits
    return prefix + "".join([random.choice(digits) for i in range(random.randrange(maxlen))])

testuserdata = [Users(firstname="", lastname = "",
                 homephone = "", mobilephone = "", workphone="", address="",
                 secondaryphone = "", email="", email2="", email3="")] + [
    Users(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
          email=random_string("email", 20), email2=random_string("email2", 20), email3=random_string("email3", 20),
          homephone=random_digits("", 20), workphone=random_digits("", 20),
          mobilephone=random_digits("", 20), secondaryphone=random_digits("", 20),
          address=random_string("address", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testuserdata))