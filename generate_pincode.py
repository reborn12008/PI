from random import randrange
import sqlite3
from sqlite3 import Error

import base64
from Crypto.Cipher import AES
from Crypto import Random

bs = AES.block_size

def decrypt(enc, key):
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return _unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

def _unpad(s):
    return s[:-ord(s[len(s)-1:])]


def encrypt(raw, key):
    raw = _pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode()))

def _pad(s):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)


def get_encryptdecrypt_password(filename):
    f = open(filename, "r")
    return f.read()

def create_connection(database_file):
    conn = None
    try:
        conn = sqlite3.connect(database_file)
    except Error as e:
        print(e)

    return conn


def update_task(c):
    password = get_encryptdecrypt_password('chave_encriptacao')

    cur = c.cursor()
    number_of_regists = cur.execute("SELECT * FROM source_acesso;")
    for i in number_of_regists.fetchall():
        pin = randrange(9999)
        ciphertext = encrypt(str(pin), password)
        
        print('Texto original: ' + str(pin))
        print('Texto encriptado: ' + str(ciphertext))
        print('Texto desencriptado: '+ decrypt(ciphertext, password))

        sql = """UPDATE source_acesso SET pincode = ? where id = ?"""
        val = (ciphertext, str(i[0]))
        cur.execute(sql, val)
    c.commit()


def main():
    database = r"db.sqlite3"
    conn = create_connection(database)
    with conn:
        update_task(conn)


if __name__ == '__main__':
    main()
