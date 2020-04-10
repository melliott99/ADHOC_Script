from passlib.context import CryptContext

import pickle



class User:

    def serialize(self):
        #try:
            filename = "usersave"
            outfile = open(filename, 'wb')
            pickle.dump(self, outfile)
            outfile.close()
        #except FileNotFoundError:


    def __init__(self, inStaffID, inPassword):
    
        self.staffId = inStaffID
        self.password = inPassword


