import Crypto.Util.number

#input Public Keys P and G
print("Please Input the (P)rime and (G)eneration keys.")
P = int(input("Input key P: "))
G = int(input("Input key G: "))

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