import nacl.encoding as enc
import nacl.hash as hashing
import nacl.secret as secret
import nacl.utils as utils
import nacl.pwhash as pwhash
import nacl.signing as signing



def encrypt(stringput):
    return hashing.blake2b(bytes(stringput, 'utf-8'), encoder=enc.HexEncoder)



