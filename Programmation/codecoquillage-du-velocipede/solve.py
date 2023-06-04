import sys

def generate_bc():
    code =  b"\x01\x09shellcode\x02"
    code += b"#C" + (0x42424242).to_bytes(4, byteorder="little")
    code += b"#A" + (836611 ^ 0x42424242).to_bytes(4, byteorder="little")
    code += b"^AC"
    code += b"#B" + (4372 ^ 0x42424242).to_bytes(4, byteorder="little")
    code += b"^BC"
    code += b')'

    return code

sys.stdout.buffer.write(generate_bc() + b'\n')