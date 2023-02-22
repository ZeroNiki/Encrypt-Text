import pyAesCrypt

passwd = input('Введите пароль для файлов: ')

# Encrypt
pyAesCrypt.encryptFile('name.txt', 'NameEncryptFile.aes', passwd)

# Decrypt
pyAesCrypt.decryptFile('NameEncryptFile.aes', 'NameTxt.txt', passwd)