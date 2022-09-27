#input your own keys P and G
P = int(input("Input a prime number: "))
print("Prime = " + str(P))
G = int(input("Input the generator: "))
print("Gen = "  + str(G))

#input your Private Key
priv = int(input("Input Your Private Key: "))
print("Your private key is:" + str(priv))

#generate your Public Key based on the algorithm (G^privkey) MOD P
public = int(pow(G, priv, P))
print("Your public key is: " + str(public))

#input your friend's Public Key they shared with you, and calculate the final shared secret with the algorithm (friendpub^privkey) MOD P
friendpub = int(input("Input your friend's public key: "))
secret = int(pow(friendpub, priv, P))
print("Final key is" + str(secret))