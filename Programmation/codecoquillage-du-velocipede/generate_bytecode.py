# SHELLCODE MY VM :

enter_shellcode = b"Please enter your shellcode: \x00"
conditions = b"Conditions not met, not showing flag.\n\x00"
# filename = b"Eont3ih4"
filename = b"FAKENAME"

# Conditions:
# reg_A = 4372
# reg_B = 836611
# reg_A * reg_B = 3657663292 -> used as XOR key for filename
# reg_A + reg_B = 840983

xor_key = (3657663292).to_bytes(4, byteorder="little")
xorred_filename = bytes([filename[i] ^ xor_key[i % 4] for i in range(len(filename))])

code = b"\x01\x09read_flag\x02" + \
       b":FS" + \
       b":CA" + \
       b"#D" + (840983).to_bytes(4, byteorder="little") + \
       b"+AB" + \
       b"-AD !" + (108).to_bytes(4, byteorder="little") + \
       b":AB" + \
       b"#D" + (1).to_bytes(4, byteorder="little") + \
       b"^BB" + \
       b"+BC" + \
       b"-AD!" + (-7).to_bytes(4, byteorder="little", signed=True) + \
       b"#D" + (3657663292).to_bytes(4, byteorder="little") + \
       b":AB-AD !" + (67).to_bytes(4, byteorder="little") + \
       b"|" + (9).to_bytes(4, byteorder="little") + b"\x00"*9 + \
       b"#D" + (8).to_bytes(4, byteorder="little") + \
       b"+SD" + \
       b"#C" + xorred_filename[4:] + b"^CB>C" + \
       b"#C" + xorred_filename[:4] + b"^CB>C" + \
       b":AS" + \
       b"#B" + (37).to_bytes(4, byteorder="little") + \
       b"/:AS$" + \
       b":SF)" + \
       b"|" + len(conditions).to_bytes(4, byteorder="little") + conditions + \
       b":AS$." + \
       b"\x01\x08ask_code\x02" + \
       b":FS" + \
       b"|" + len(enter_shellcode).to_bytes(4, byteorder="little") + enter_shellcode + \
       b":AS$" + \
       b"#B" + (1000).to_bytes(4, byteorder="little") + \
       b"%" + \
       b":SF)" + \
       b"\x01\x04main\x02" + \
       b"(\x08ask_code" + \
       b"(\x09shellcode" + \
       b"(\x09read_flag" + \
       b'^AA.'


FILE_NAME = "shellcode_my_vm_redacted"

with open(FILE_NAME + ".vmr", "wb+") as f:
    f.write(code)
