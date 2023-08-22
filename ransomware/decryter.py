import pyaes
import os

file_name = "teste_troll.txt"
with open(file_name, "rb") as file:
        file_data = file.read()




key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

os.remove(file_name)

with open("teste.txt", "wb") as new_file:
        new_file.write(decrypt_data)
