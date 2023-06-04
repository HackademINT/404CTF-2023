# Assembleur fait à la va-vite. Pas de garde fous, donc attention à ce que vous codez.

import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()

prgm = []

regs = {
    'r0' : '0',
    'r1' : '1',
    'r2' : '2',
    'r3' : '3',
    'tos': '4',
    'r4' : '5',
    'r5' : '6',
    'r6' : '7',
    'r7' : '8'
}

offsets = {
    'movi' : 3,
    'mov'  : 3,
    'xori' : 3,
    'xor'  : 3,
    'andi' : 3,
    'and'  : 3,
    'ori'  : 3,
    'or'   : 3,
    'addi' : 3,
    'add'  : 3,
    'subi' : 3,
    'sub'  : 3,
    'muli' : 3,
    'mul'  : 3,
    'divi' : 3,
    'div'  : 3,
    'pushi': 2,
    'push' : 2,
    'pop'  : 2,
    'movmi': 3,
    'movm' : 3,
    'jmp'  : 3,
    'jz'   : 4,
    'jnz'  : 4,
    'jgei' : 5,
    'jlei' : 5,
    'jei'  : 5,
    'jnei' : 5,
    'jne'  : 5,
    'ret'  : 1,
    'call' : 3,
    'readm': 3,
    'out'  : 2,
    'end'  : 1
}

ops = {
    'movi' : 9,
    'mov'  : 90,
    'xori' : 10,
    'xor'  : 100,
    'andi' : 11,
    'and'  : 110,
    'ori'  : 12,
    'or'   : 120,
    'addi' : 13,
    'add'  : 130,
    'subi' : 14,
    'sub'  : 140,
    'muli' : 15,
    'mul'  : 150,
    'divi' : 16,
    'div'  : 160,
    'pushi': 17,
    'push' : 170,
    'pop'  : 18,
    'movmi': 19,
    'movm' : 190,
    'jmp'  : 20,
    'jz'   : 21,
    'jnz'  : 22,
    'jgei' : 23,
    'jlei' : 24,
    'jei'  : 25,
    'jnei' : 26,
    'jne'  : 126,
    'ret'  : 27,
    'call' : 28,
    'readm': 29,
    'out'  : 254,
    'end'  : 255
}

labels = {}
length = 0
for line in data:
    if ':' in line:
        labels = {line.strip()[:-1] : str(length)} | labels
    else:
        if line.strip() == '':
            continue
        length += offsets[line.strip().split(' ')[0].strip()]
for line in data:
    if ':' not in line and line.strip() != '':
        tokens = line.strip().split(' ')
        # if offsets[tokens[0]] != len(tokens):
        #     print(f'Wrong number of arguments for {tokens[0]}')
        #     exit(0)
        for i in range(1, len(tokens)):
            if tokens[i] in labels.keys():
                l = int(labels[tokens[i]])
                tokens[i] = str((l//256)) + '; ' + str(l%256)
        
            if tokens[i] in regs.keys():
                tokens[i] = regs[tokens[i]]

        tokens[0] = str(ops[tokens[0]])
        prgm += tokens

print('[' + '; '.join(prgm) + ']')