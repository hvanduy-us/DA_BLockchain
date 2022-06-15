
import Libraries as lib



class Client:
   def __init__(self):
      random = lib.Crypto.Random.new().read
      self._private_key = lib.RSA.generate(1024, random)
      self._public_key = self._private_key.publickey()
      self._signer = lib.PKCS1_v1_5.new(self._private_key)

   @property
   def identity(self):
      return lib.binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

Dinesh = Client()
print (Dinesh.identity)