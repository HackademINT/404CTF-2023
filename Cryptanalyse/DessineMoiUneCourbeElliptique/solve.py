from Crypto.Cipher import AES
import hashlib

x1 = 93808707311515764328749048019429156823177018815962831703088729905542530725
y1 = 144188081159786866301184058966215079553216226588404139826447829786378964579
x2 = 139273587750511132949199077353388298279458715287916158719683257616077625421
y2 = 30737261732951428402751520492138972590770609126561688808936331585804316784

p = 231933770389389338159753408142515592951889415487365399671635245679612352781

ciphertext = bytes.fromhex('8233d04a29befd2efb932b4dbac8d41869e13ecba7e5f13d48128ddd74ea0c7085b4ff402326870313e2f1dfbc9de3f96225ffbe58a87e687665b7d45a41ac22')
iv = bytes.fromhex('00b7822a196b00795078b69fcd91280d')

#Les versions récentes de pythons acceptent un deuxième argument négatif pour la fonction pow si cette fonction à trois arguments (ie que l'on travaille modulo le troisième argument), mais cette fonction est très simple à refaire à la main grâce au petit théorème de Fermat 
a = (y1**2 - y2**2 - (x1**3 - x2**3)) * pow((x1 -x2), -1, p)
#Ne pas oublier que l'on travaille modulo p
a %= p
b = y1**2 - x1**3 - a*x1  
b %= p 

key = str(a) + str(b)
aes = AES.new(hashlib.sha1(key.encode()).digest()[:16], AES.MODE_CBC, iv=iv)
flag = aes.decrypt(ciphertext)
print(flag)
