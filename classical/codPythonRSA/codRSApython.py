# NOTĂ-1 - codul de mai jos a fost testat utilizând versiunea de python 3.7
# NOTĂ-2 - apriori rulării codului, este necesară instalarea librăriei „pycryptodome”. Aceasta se poate face utilizând comanda „pip install pycryptodome”
# Librăria „pycryptodome” - low-level cryptographic primitives (hashes, MAC codes, key-derivation, symmetric and asymmetric ciphers, digital signatures)

# Concept de testare a algoritmului RSA, cheie publică - cheie privată

from Crypto.PublicKey import RSA                                    # pentru generarea setului de cheii și utilizarea algoritmului RSA, din modulul „Crypto.PublicKey” se importă algoritmul RSA 
from Crypto.Cipher import PKCS1_OAEP                                # pentru îmbunătățirea securității, din modulul „Crypto.Cipher”, se importă librăria „PKCS1_OAEP”, OAEP - Optimal Asymmetric Encryption Padding
import binascii                                                     # se importă modulul binar ASCII 

# Generarea cheii RSA
keyPair = RSA.generate(3072)                                        # 3072-bit – actual, considerat a fi „standard” în ceea ce privește securitatea unui mesaj

pubKey = keyPair.publickey()                                        # definirea setului de chei, publică-privată
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")       # definirea cheii publice și afișarea în terminal în format hexadecimale
pubKeyPEM = pubKey.exportKey()                                      
print(pubKeyPEM.decode('ascii'))                                    # afișarea cheii publice în format ASCII

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")      # definirea cheii private și afișarea rezultatului în terminal, în format hexadecimal
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))                                   # afișarea cheii private în format ASCII

# Criptarea mesajului
mesaj = b'Mesaj pentru verificarea algoritmului RSA'                # scrierea mesajului ce dorește a se fi transmis prin intermediul algoritmului RSA
criptare = PKCS1_OAEP.new(pubKey)                                   # se adaugă schema de padding pentru criptare folosind cheia publică
criptat = criptare.encrypt(mesaj)                                   # mesaj criptat
print("Criptat:", binascii.hexlify(criptat))                        # afișează în terminal mesajul expediat, criptat

# Decodificarea mesajului
decodificare = PKCS1_OAEP.new(keyPair)                              # decodificare
decodificat = decodificare.decrypt(criptat)                         # decodificat
print('Decodificat:', decodificat)                                  # afișează în terminal mesajul recepționat, decodificat