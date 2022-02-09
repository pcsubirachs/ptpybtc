#from pycoin.symbols.btc import network
from pycoin import *
from pycoin.symbols.btc import network

key = network.keys.private(secret_exponent=1)  # this is a terrible key because it's very guessable
print(key.wif())
print(key.sec())
print(key.address())
print(key.address(is_compressed=False))

same_key = network.parse.private(key.wif())
print(same_key.address())