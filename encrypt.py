import pyAesCrypt
print("<Encrypt>")
bufferSize = 64 * 1024

file = input("File Name : ")
password = input("Password : ")

pyAesCrypt.encryptFile(file,file+".aes",password,bufferSize)

print("File Encrypted !")
