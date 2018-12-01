from Crypto.Cipher import AES
import binascii
keystring = '00000000000000000000000000000000'
iostoken = 'xxxx1d1872c33126bf41c2b56c59816d5731be97da02bf8c3ce60e77c61f603d0143db63ee66b0cdff9f69917680151e'
key = bytes.fromhex(keystring)
cipher = AES.new(key, AES.MODE_ECB)
token = cipher.decrypt(bytes.fromhex(iostoken[:64]))
print(token)
