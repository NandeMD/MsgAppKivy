# Basic Messaging App With Kivy GUI

***


This is a socket client written by me for fun purposes. You can take the code and use wherever you want.

You can use [`server.py` in my gists](https://gist.github.com/NandeMD/64e2ad9c7c824d8127a4ac572a558370 "Gist Link"). If you use it, messages are encrypted in device, then send to server. Server only distributes messages to other active clients. Server can't see your messages. Received messages are decrypted in client as well.

I didn't include my `.num`, `.name` and `.msg` files. Those files contain encryption keys. If you want to encrypt your messages, you need to run `generatekeys.py` file. That will generate the keys you will need.

Kivy is a cross-platform module, so you can alter the code and create a package with [Buildozer](https://buildozer.readthedocs.io/en/latest/ "Buildozer Docs") for Android and IOS. You can also bundle a desktop package with [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/ "PyInstaller Docs").
For packaging, please look at [this link](https://kivy.org/doc/stable/guide/packaging.html "Kivy Packaging Manual").

## External modules used in project:
- [cryptography](https://cryptography.io/en/latest/) (for encrypting and decrypting messages)
    * > pip install cryptography
- [kivy](https://kivy.org/#home) (for GUI)
    * > pip install kivy[base]