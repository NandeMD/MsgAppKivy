import socket
from threading import Thread
from pickle import dumps, loads
from dataclasses import dataclass
from random import choice
from encrypt import EncryptDecrypt


@dataclass(frozen=False)
class Message:
    name: bytes
    msg: bytes


class SocketServer:
    def __init__(self, ids, name, address, buffer):
        self.FERNET = EncryptDecrypt()
        self.is_connected = False
        self.ids = ids
        self.__names = {}
        self.__colors = ["FFFF00", "FFA500", "FF69B4", "40E0D0", "D3D3D3"]
        ids.mainlabel.text += f"\n[color=#ffff00]<INIT>[/color]    Connection initializing..."
        self.NAME = name
        ids.mainlabel.text += f"\n[color=#ffff00]<INIT>[/color]    Name set to [color=#0000ff]{self.NAME}[/color]"
        self.ADDR = address
        ids.mainlabel.text += f"\n[color=#ffff00]<INIT>[/color]    Address set to [color=#0000ff]{self.ADDR}[/color]"
        self.BUFFER = buffer
        ids.mainlabel.text += f"\n[color=#ffff00]<INIT>[/color]    Buffer set to [color=#0000ff]{self.BUFFER}[/color]"
        self.CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ids.mainlabel.text += f"\n[color=#ffff00]<INIT>[/color]    Socket created."

    def __listen(self):
        while self.is_connected:
            whole = self.CLIENT.recv(self.BUFFER)
            data = whole.replace(b"\xff", b"")
            print(len(data))
            try:
                data = loads(self.FERNET.decrypt_whole(data))
                data.name = self.FERNET.decrypt_name(data.name).decode('utf-8')
                data.msg = self.FERNET.decrypt_msg(data.msg).decode('utf-8')
                if not self.__names.get(data.name):
                    self.__names[data.name] = choice(self.__colors)

                self.ids.mainlabel.text += f"\n[color=#{'00FF00' if data.name == self.NAME else self.__names[data.name]}]{data.name}[/color]>> {data.msg}"
            except:
                pass

    def __connect(self):
        self.CLIENT.connect(self.ADDR)
        self.is_connected = True
        self.ids.mainlabel.text += f"\n[color=#ffff00]<CONN>[/color]    Client connected."
        Thread(target=self.__listen, daemon=True).start()

    def send(self, message: str):
        if message == "":
            return
        msg = Message(self.FERNET.encrypt_name(self.NAME.encode("utf-8")), self.FERNET.encrypt_msg(message.encode("utf-8")))
        msg = self.FERNET.encrypt_whole(dumps(msg))
        msg += b"\xff" * (self.BUFFER - len(msg))
        Thread(target=self.CLIENT.send, args=(msg,), daemon=True).start()

    def start(self):
        Thread(target=self.__connect, daemon=True).start()
