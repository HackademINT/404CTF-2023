import os
from jinja2 import Template
import random as rd

N = 100

with open('stagemodel.c.j2', 'r') as f:
    t = Template(f.read())

key = os.urandom(rd.randint(1024, 2048))

os.system('gcc -o stages/stage0_clear -s stage0.c')
with open('stages/stage0', 'wb') as f, open('stages/stage0_clear', 'rb') as c, open('stages/key0', 'wb') as k:
    b = bytearray(c.read())
    for i in range(len(b)):
        b[i] ^= key[i % len(key)]
    f.write(bytes(b))
    k.write(key)
os.system('xxd -i stages/stage0 > stages/stage0.h')
os.system('xxd -i stages/key0 >> stages/stage0.h')

for i in range(N):
    key = os.urandom(rd.randint(1024, 2048))

    with open(f'stages/stage{i + 1}.c', 'w') as f:
        f.write(t.render(n=i, rickroll=False))
    os.system(f'gcc -o stages/stage{i + 1}_clear -s -I stages stages/stage{i + 1}.c')

    with open(f'stages/stage{i + 1}', 'wb') as f, open(f'stages/stage{i + 1}_clear', 'rb') as c, open(f'stages/key{i + 1}', 'wb') as k:
        b = bytearray(c.read())
        for j in range(len(b)):
            b[j] ^= key[j % len(key)]
        f.write(bytes(b))
        k.write(key)
    os.system(f'xxd -i stages/stage{i + 1} > stages/stage{i + 1}.h')
    os.system(f'xxd -i stages/key{i + 1} >> stages/stage{i + 1}.h')

    os.system(f'rm stages/stage{i}*  stages/key{i}')
    print(i)


with open('introspection.c', 'w') as f:
    f.write(t.render(n=N, rickroll=True))
os.system(f'gcc -o introspection -s -I stages introspection.c')
os.system('rm stages/stage* stages/key*')