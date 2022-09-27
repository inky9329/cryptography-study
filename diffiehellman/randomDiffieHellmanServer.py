import Crypto.Util.number

#set all randomly generated data to 64 bits (up this for more secure keys)
len = 64

#generate keys P and G (Prime and Generator)
print("Creating (P)rime and (G)eneration keys.")
P = int(Crypto.Util.number.getPrime(len))
print("Prime = " + str(P))
G = int(Crypto.Util.number.getRandomNBitInteger(len))
print("Generator = " + str(G))

#generate your Private Key
print("Generating Private Key")
privkey = int(Crypto.Util.number.getRandomNBitInteger(len))
print("Your private key is: " + str(privkey))

#generate your Public Key based on the algorithm (G^privkey) MOD P
print("Generating Public Key")
public = int(pow(G, privkey, P))
print("Your public key is: " + str(public))

#input your friend's Public Key they shared with you, and calculate the final shared secret with the algorithm (friendpub^privkey) MOD P
friendpub= int(input("Input your friend's public key: "))
calc = int(pow(friendpub, privkey, P))
print("Final key is" + str(calc))