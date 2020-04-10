from webbot import Browser
from User import *
from getpass import getpass
import time
import pickle ##Used for serialization

#Security
#encrypt = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"])


#Pickle stuff
try:
    filename = "usersave"
    infile = open(filename, "rb")
    person = pickle.load(infile)

    infile.close()

    print(person)
except(EOFError,FileNotFoundError) as e:
    print("No Previous Account has been found sign up here!")
    username = input("What is your staff id?: ")
    password = getpass()
    person = User(username, password)
    person.serialize()


URL1 = "https://sslvpn.curtin.edu.au/"
URL2 = "tanjiro.cs.curtin.edu.au"

br = Browser()
br.go_to(URL1)

br.type(person.staffId, id = "username")
br.type(person.password, id = "password_input")
br.click("Login")

isFound = True
while(isFound):
    if(br.exists(id = "keepout", xpath = '/html/body/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/input[2]')):
        br.click(id = "keepout", xpath = '/html/body/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/input[2]')
        isFound = False
        print("Page has loaded")
    else:
        print("Waiting for page to load")

br.type(URL2, id = "unicorn_form_url")
br.click(id = "go")

br.type(person.staffId, id = "id_username")
br.type(person.password, id = "id_password")
br.click(id = "btnLogin")