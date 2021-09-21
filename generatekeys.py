from cryptography.fernet import Fernet


fnames = [".num", ".name", ".msg"]


def generate_keys():
    for name in fnames:
        with open(name, "wb") as file:
            file.write(Fernet.generate_key())


if __name__ == "__main__":
    generate_keys()
