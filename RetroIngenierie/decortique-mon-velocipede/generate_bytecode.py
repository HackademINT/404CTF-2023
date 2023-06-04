# REVERSE MY VM :

xor_key = b"p4ck"
pck_key = b"b4ByG1rl"

rev_flag = b"404CTF{P4ck1ng_1s_H3ll!}"
rev_flag_xored = []
for i in range(len(rev_flag)):
    rev_flag_xored.append(rev_flag[i] ^ xor_key[i % len(xor_key)])
rev_flag_xored = bytes(rev_flag_xored)

s_enter_key = b"Please enter the key: \x00"
s_enter_pass = b"Now, enter the passcode: \x00"
s_congrats = b"Congrats! Your flag is: "

tupac = b"\x01\x09check_key\x02" + \
        b"|" + len(s_enter_pass).to_bytes(4, byteorder="little") + s_enter_pass + \
        b":AS$" + \
        b"#B" + (256).to_bytes(4, byteorder='little') + \
        b"%<F" + \
        b"|" + (2).to_bytes(4, byteorder="little") + b"\n\x00" + \
        b"|" + len(rev_flag_xored).to_bytes(4, byteorder="little") + rev_flag_xored + \
        b":ES" + \
        b"#A" + (6).to_bytes(4, byteorder='little') + \
        b"#B" + (1).to_bytes(4, byteorder='little') + \
        b"#C" + (4).to_bytes(4, byteorder='little') + \
        b"<D^DF>D" + \
        b"+SC-AB" + \
        b"!" + (-14).to_bytes(4, byteorder='little', signed=True) + \
        b":SE|" + len(s_congrats).to_bytes(4, byteorder="little") + s_congrats + \
        b":AS$" + \
        b"^AA. SWAG" # SWAG à la fin c'est juste du padding, t'façon y a un exit avant

print(tupac)

packed = []
for i in range(len(tupac)):
    packed.append(tupac[i] ^ pck_key[i % len(pck_key)])
packed = bytes(packed)

code =  b"\x01\x04main\x02" + \
        b"|" + len(s_enter_key).to_bytes(4, byteorder="little") + s_enter_key + \
        b":AS$" + \
        b"#B" + (256).to_bytes(4, byteorder='little') + \
        b"%:DS" + \
        b"|" + len(packed).to_bytes(4, byteorder="little") + packed + \
        b"^EE#A" + (len(packed) // len(pck_key) * 2).to_bytes(4, byteorder='little') + \
        b":BS:SD+SE<C:SB" + \
        b"<B^BC>B" + \
        b"#F" + (4).to_bytes(4, byteorder='little') + \
        b"+SF+EF&EF" + \
        b"#F" + (1).to_bytes(4, byteorder='little') + \
        b"-AF!" + (-46).to_bytes(4, byteorder='little', signed=True) + \
        b"#F" + (256).to_bytes(4, byteorder='little') + \
        b"-SF" + \
        b"(\x09check_key"

FILE_NAME = "reverse_my_vm"

with open(FILE_NAME + ".vmr", "wb+") as f:
    f.write(code)
