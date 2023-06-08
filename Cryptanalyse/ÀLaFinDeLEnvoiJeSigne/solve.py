import socket
import json
import math
from hashlib import md5 as hash

class Netcat:

    """ Python 'netcat like' module """

    def __init__(self, ip, port):

        self.buff = b""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length = 1024):

        """ Read 1024 bytes off the socket """

        return self.socket.recv(length)
 
    def read_until(self, data):

        """ Read data into the buffer until we have data """

        while not data in self.buff:
            self.buff += self.socket.recv(1024)
 
        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]
 
        return rval
 
    def write(self, data):

        self.socket.send(data)
    
    def close(self):

        self.socket.close()


def checksum(data: bytes, block_size: int):
    bindata = f'{int.from_bytes(data, "big"):0b}'.zfill(64*block_size)
    acc = 0
    for i in range(0, len(bindata), block_size):
        acc += 2**block_size - int(bindata[i:i+block_size], 2) - 1
    acc %= 256
    return acc.to_bytes(1, 'big')

def convol_hash(data: bytes, power: int):
    acc = data
    for _ in range(power):
        acc = hash(acc).digest()
    return acc



nc = Netcat("challenges.404ctf.fr", 30724)
initial = json.loads(nc.read_until(b'\n\n').decode())

initial_message = bytes.fromhex(initial['msg'])
initial_sig = [bytes.fromhex(x) for x in initial['sig']]

initial_message_padded = initial_message + b'\x00' * (32 - len(initial_message))
bininitial_message_padded = f'{int.from_bytes(initial_message_padded, "big"):0b}'.zfill(256)

initial_checksum = checksum(initial_message_padded, 4)
print(initial_checksum[0])

target = b'gimme flagz'
bintarget = f'{int.from_bytes(target, "big"):0b}'.zfill(8*len(target))
new_sig = []
binnew_msg = bintarget


for i in range(0, len(bintarget), 4):
    diff = int(bintarget[i:i+4], 2) - int(bininitial_message_padded[i:i+4], 2)
    print(diff)
    assert diff >= 0
    new_sig.append(convol_hash(initial_sig[i//4], diff))

while len(new_sig) < len(initial_sig) - 2:
    _binnew_msg = binnew_msg + "0000" * ((len(binnew_msg)%8)//4)
    print("Block number", len(binnew_msg)//4)
    new_msg = int(_binnew_msg, 2).to_bytes(len(_binnew_msg) // 8, "big")
    new_msg_padded = new_msg + b'\x00' * (32 - len(new_msg))
    checksum_diff = (checksum(new_msg_padded, 4)[0] - initial_checksum[0]) % 256
    bininit_message_part = bininitial_message_padded[len(binnew_msg):len(binnew_msg)+4]
    print(bininit_message_part)
    print(new_msg_padded.hex())
    if checksum_diff > (0xf - int(bininit_message_part, 2)):
        binnew_msg += "1111"
        print("Appending 1111")
        new_sig.append(convol_hash(initial_sig[len(new_sig)], (0xf - int(bininit_message_part, 2))))
    else:
        app = int(bininit_message_part, 2) + checksum_diff
        app = bin(app)[2:]
        app = "0"*(4-len(app)) + app
        binnew_msg += app
        print("Appending "+app)
        new_sig.append(convol_hash(initial_sig[len(new_sig)], checksum_diff))

# Pour la checksum (qui a la meme signature vu que les checksums des deux messages sont egales)
new_sig.extend(initial_sig[-2:])


new_msg = int(binnew_msg, 2).to_bytes(len(binnew_msg) // 8, "big")

nc.write(json.dumps({"msg": new_msg.hex(), "sig": [x.hex() for x in new_sig]}).encode() + b'\n')
flag = json.loads(nc.read_until(b'\n').decode().strip())
print(flag)
