import Crypto
import Crypto.Random
from Crypto.PublicKey import RSA
import binascii
from Crypto.Cipher import PKCS1_OAEP

random_generator = Crypto.Random.new().read

private_key = RSA.generate(1024, random_generator)
public_key = private_key.publickey()

#Exportamos las claves objetos RSA
private_key = private_key.export_key(format='DER')
public_key = public_key.export_key(format='DER')


#Convertimos a codigo ascii utf8
private_key = binascii.hexlify(private_key).decode('utf8')
public_key = binascii.hexlify(public_key).decode('utf8')


#Convertir las llaves texto en objetos RSA:
private_key = RSA.import_key(binascii.unhexlify(private_key)) 
public_key = RSA.import_key(binascii.unhexlify(public_key))

mensaje = 'Taller de criptografia algoritmo RSA'
print("\n")
print(mensaje)
print("\n")
mensaje = mensaje.encode()

#Encriptar mensaje
cipher = PKCS1_OAEP.new(public_key)
mensaje_encriptado = cipher.encrypt(mensaje)
print(mensaje_encriptado)
print("\n")
#Desencriptar mensaje
cipher = PKCS1_OAEP.new(private_key)
mensaje_desencriptado = cipher.decrypt(mensaje_encriptado)
print(mensaje_desencriptado)
