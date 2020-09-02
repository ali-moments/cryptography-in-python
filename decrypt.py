import pyAesCrypt

print("<Decrypt>")

bufferSize = 64 * 1024

file = input("File Name : ")
password = input("Password : ")

try:
    pyAesCrypt.decryptFile(file,file+"_decrypted",password,bufferSize)
    print("File Decrypted !")

except Exception as error:
    print(error)
    exit(1)
