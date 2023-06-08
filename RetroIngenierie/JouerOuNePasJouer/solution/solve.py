# Remerciements à https://github.com/kinnay pour l'écriture de ce script, fait à l'origine pour l'algorithme sead::Random réellement utilisé sur la Switch/Wii U.
# Adaptée par toyohr pour utiliser des u64 au lieu de u32.

# Placer les valeurs données par le .nro
s0 = 15323416860013248078
s1 = 2038102213101842551
s2 = 9039777371918867651
s3 = 5323617266019954679

# Reconstitution du tableau d'état d'origine
for i in range(8):
    temp = s3
    s3 = s2
    s2 = s1
    s1 = s0
    
    temp ^= s3 >> 19
    temp ^= s3

    # Reverse temp ^= temp >> 8
    temp ^= (temp & 0xFF00000000000000) >> 8
    temp ^= (temp & 0xFF000000000000) >> 8
    temp ^= (temp & 0xFF0000000000) >> 8
    temp ^= (temp & 0xFF00000000) >> 8
    temp ^= (temp & 0xFF000000) >> 8
    temp ^= (temp & 0xFF0000) >> 8
    temp ^= (temp & 0xFF00) >> 8
    
    # Reverse temp ^= temp << 11
    temp ^= (temp & 0x7FF) << 11
    temp ^= (temp & 0x3FF800) << 11
    temp ^= (temp & 0x1FFC00000) << 11
    temp ^= (temp & 0xFFE00000000) << 11
    temp ^= (temp & 0x1FF00000000000) << 11
    s0 = temp

print(s0)
print(s1)
print(s2)
print(s3)

# Reverse mt_constant * seed + 1
seed = ((s0 - 1) * pow(0x6C0789656C078965, -1, 1 << 64)) & 0xFFFFFFFFFFFFFFFF
# Reverse seed ^ (seed >> 30u)
seed ^= (seed & 0xFFFFFFFC00000000) >> 30
seed ^= (seed & 0x3C0000000) >> 30
print(seed)
