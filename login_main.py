from log import Ui_Form
from cryptography.fernet import Fernet
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc




class LoginWindow(qtw.QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.submit.clicked.connect(self.authenticate)
        self.use_key.clicked.connect(self.generate_key)
        self.Save_My_Message.clicked.connect(self.save_message)
    def authenticate(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        if username == 'use' and password == 'pass':
            ###########################################
            fetched_key = self.get_key()
            if not fetched_key == "None":

                #print(fetched_key)
                #self.generate_message(fetched_key)
                fetched_message = self.get_encrypted_message()
                #print(fetched_message)
                my_message = self.decrypt_message(fetched_message, fetched_key)
                ########################################
                print("My message is : " + my_message)
                qtw.QMessageBox.information(self, 'Success',my_message)
                self.username_lineEdit.setText("")
                self.password_lineEdit.setText("")
            else:
                qtw.QMessageBox.critical(self, 'Fail','You have not got the key')
                self.username_lineEdit.setText("")
                self.password_lineEdit.setText("")
                
        else:
            print("Fail!")
            qtw.QMessageBox.critical(self, 'Fail','You are not getting the message')
            self.username_lineEdit.setText("")
            self.password_lineEdit.setText("")

    def save_message(self):
        print("save_message")
        message = self.message_lineEdit.text()
        print(message)
        # encode the message
        encoded = message.encode()
        # fetch key
        fetched_key = self.get_key()
        # encrypt the message
        print(fetched_key)
        f = Fernet(fetched_key)
        encrypted = f.encrypt(encoded)
        print(encrypted)
        message_file = open('personal_message.txt','wb')
        message_file.write(encrypted)
        message_file.close
        print("written to file")
        self.message_lineEdit.setText("")

    
    def get_key(self):
        print("get_key")
        try:
            file = open('login.key', 'rb')
            #file = open('F:\\login.key', 'rb')
            key = file.read()
            file.close()
            return key
        except FileNotFoundError:
            print("File does not exist")
            key = "None"
            return key    

    def generate_key(self):
        print("the_key")
        # generate key
        key = Fernet.generate_key()
        file = open('login.key', 'wb')
        #file = open('F:\\login.key', 'wb')
        file.write(key)
        file.close()
        print(key)

        
            
    def get_encrypted_message(self): 
        file = open('personal_message.txt', 'rb')
        msg = file.read()
        file.close()
        #print(msg)
        return msg
    def decrypt_message(self, fetched_message, fetched_key):
        print("decrypt_message")
        print(fetched_message)
        print(fetched_key)
        # decrypt the encrypted message
        f2 = Fernet(fetched_key)
        decrypted = f2.decrypt(fetched_message)
        print(decrypted)
        # decodeconvert from bytes object to string
        original_message = decrypted.decode()
        print(original_message)
        return original_message
    
        
        
         

        


        

        
    
        




        
if __name__=='__main__':
    app = qtw.QApplication([])

    widget = LoginWindow()
    widget.show()

    app.exec_()
            
