from hashlib import md5 as hash
from dataclasses import dataclass
import json, os, asyncio

# in bits
BLOCK_SIZE = 4
CHECKSUM_SIZE = 2*BLOCK_SIZE
MESSAGE_SIZE = 64*BLOCK_SIZE

FLAG = os.getenv('FLAG')


def pad_msg(data: bytes, size: int):
    return data + b'\x00' * (size - len(data))

def convol_hash(data: bytes, power: int):
    acc = data
    for _ in range(power):
        acc = hash(acc).digest()
    return acc

def checksum(data: bytes, block_size: int, checksum_size: int, message_size: int):
    bindata = f'{int.from_bytes(data, "big"):0b}'.zfill(message_size)
    acc = 0
    for i in range(0, message_size, block_size):
        acc += 2**block_size - int(bindata[i:i+block_size], 2) - 1
    acc %= 2**checksum_size
    return acc.to_bytes(checksum_size // 8, 'big')

@dataclass
class WinternitzPrivKey:
    secrets: list[bytes]
    block_size: int = BLOCK_SIZE
    checksum_size: int = CHECKSUM_SIZE

    def public_key(self):
        return WinternitzPubKey([convol_hash(s, 2**self.block_size) for s in self.secrets], self.block_size, self.checksum_size)

    def sign(self, data: bytes):
        signature_size = len(self.secrets)*self.block_size
        data_size = signature_size - self.checksum_size
        assert len(data) * 8 < data_size, "The message you want to sign is too long"
        padded_data = pad_msg(data, data_size // 8)
        cksum = checksum(padded_data, self.block_size, self.checksum_size, data_size)
        plaintext = padded_data + cksum
        binpt = f'{int.from_bytes(plaintext, "big"):0b}'.zfill(signature_size)
        sig = []
        for i in range(0, signature_size, self.block_size):
            x = convol_hash(self.secrets[i//self.block_size], int(binpt[i:i+self.block_size], 2))
            sig.append(x)
        return sig

@dataclass
class WinternitzPubKey:
    public: list[bytes]
    block_size: int = BLOCK_SIZE
    checksum_size: int = CHECKSUM_SIZE

    def verify(self, data: bytes, sig: list[bytes]):
        signature_size = len(self.public)*self.block_size
        data_size = signature_size - self.checksum_size
        assert len(sig) == len(self.public), "Signature size does not match key size"
        assert len(data) * 8 <= data_size, "The message you want to verify is too long"
        padded_data = pad_msg(data, data_size // 8)
        cksum = checksum(padded_data, self.block_size, self.checksum_size, data_size)
        plaintext = padded_data + cksum
        bindata = f'{int.from_bytes(plaintext, "big"):0b}'.zfill(signature_size)
        for i in range(0, len(bindata), self.block_size):
            exp = 2**self.block_size - int(bindata[i:i+self.block_size], 2)
            if convol_hash(sig[i//self.block_size], exp) != self.public[i//self.block_size]:
                return False
        return True




async def challenge(reader, writer):
    privkey = WinternitzPrivKey([hash(os.urandom(32)).digest() for i in range((MESSAGE_SIZE + CHECKSUM_SIZE) // BLOCK_SIZE)])
    pubkey = privkey.public_key()
    msg = b"SALUT CA VA?"
    sig = [x.hex() for x in privkey.sign(msg)]
    initial = json.dumps({"msg": msg.hex(), "sig": sig})
    initial += '\n'
    writer.write(initial.encode('utf8'))
    await writer.drain()

    try:
        request = json.loads((await reader.read(4096)).decode('utf8'))
        data = bytes.fromhex(request["msg"])
        sig = [bytes.fromhex(x) for x in request["sig"]]
        if data.startswith(b'gimme flagz'):
            valid = pubkey.verify(data, sig)
            if valid:
                response = json.dumps({"flag": FLAG})
            else:
                response = json.dumps({"error": "The signature is not valid"})
        else:
            response = json.dumps({"error": "Your message is not interesting, sorry"})
        response += '\n'
        writer.write(response.encode('utf8'))
        await writer.drain()
    except Exception as e:
        response = json.dumps({"error": "An unexpected error occurred"})
        response += '\n'
        writer.write(response.encode('utf8'))
    finally:
        await writer.drain()
        writer.close()

async def run_server():
    server = await asyncio.start_server(challenge, '0.0.0.0', 5000)
    async with server:
        print("Challenge running on port 5000")
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(run_server())
