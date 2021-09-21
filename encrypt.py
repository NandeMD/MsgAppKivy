from cryptography.fernet import Fernet


class EncryptDecrypt:
    def __init__(self):
        self.NUM = ".num"
        self.NAME = ".name"
        self.MSG = ".msg"

    @staticmethod
    def load_key(which):
        with open(which, "rb") as file:
            key = file.read()
        return key

    def encrypt_whole(self, whole):
        key = self.load_key(self.NUM)
        fernet = Fernet(key)
        encrypted = fernet.encrypt(whole)
        return encrypted

    def encrypt_name(self, name):
        key = self.load_key(self.NAME)
        fernet = Fernet(key)
        encrypted = fernet.encrypt(name)
        return encrypted

    def encrypt_msg(self, msg):
        key = self.load_key(self.MSG)
        fernet = Fernet(key)
        encrypted = fernet.encrypt(msg)
        return encrypted

    def decrypt_whole(self, whole):
        key = self.load_key(self.NUM)
        fernet = Fernet(key)
        decrypted = fernet.decrypt(whole)
        return decrypted

    def decrypt_name(self, name):
        key = self.load_key(self.NAME)
        fernet = Fernet(key)
        decrypted = fernet.decrypt(name)
        return decrypted

    def decrypt_msg(self, msg):
        key = self.load_key(self.MSG)
        fernet = Fernet(key)
        decrypted = fernet.decrypt(msg)
        return decrypted
