import z3

s = z3.Solver()

flag = [z3.BitVec(f'f_{i}', 8) for i in range(48)]

s.add(flag[0] + flag[1] + 518 * flag[2] == 35329)
s.add(flag[0] + 518 * flag[1] + flag[2] == 17234)
s.add(flag[3] + flag[4] + 518 * flag[5] == 40542)
s.add(flag[3] + 518 * flag[4] + flag[5] == 19862)
s.add(flag[6] + flag[7] + 518 * flag[8] == 27099)
s.add(flag[6] + 518 * flag[7] + flag[8] == 61221)
s.add(flag[9] + flag[10] + 518 * flag[11] == 49360)
s.add(flag[9] + 518 * flag[10] + flag[11] == 18857)
s.add(flag[12] + flag[13] + 518 * flag[14] == 59202)
s.add(flag[12] + 518 * flag[13] + flag[14] == 25080)
s.add(flag[15] + flag[16] + 518 * flag[17] == 58164)
s.add(flag[15] + 518 * flag[16] + flag[17] == 27661)
s.add(flag[18] + flag[19] + 518 * flag[20] == 54540)
s.add(flag[18] + 518 * flag[19] + flag[20] == 51438)
s.add(flag[21] + flag[22] + 518 * flag[23] == 54563)
s.add(flag[21] + 518 * flag[22] + flag[23] == 39570)
s.add(flag[24] + flag[25] + 518 * flag[26] == 51973)
s.add(flag[24] + 518 * flag[25] + flag[26] == 26640)
s.add(flag[27] + flag[28] + 518 * flag[29] == 58159)
s.add(flag[27] + 518 * flag[28] + flag[29] == 25071)
s.add(flag[30] + flag[31] + 518 * flag[32] == 35402)
s.add(flag[30] + 518 * flag[31] + flag[32] == 57633)
s.add(flag[33] + flag[34] + 518 * flag[35] == 17228)
s.add(flag[33] + 518 * flag[34] + flag[35] == 43078)
s.add(flag[36] + flag[37] + 518 * flag[38] == 26073)
s.add(flag[36] + 518 * flag[37] + flag[38] == 25556)
s.add(flag[39] + flag[40] + 518 * flag[41] == 46239)
s.add(flag[39] + 518 * flag[40] + flag[41] == 27627)
s.add(flag[42] + flag[43] + 518 * flag[44] == 35842)
s.add(flag[42] + 518 * flag[43] + flag[44] == 26019)
s.add(flag[45] + flag[46] + 518 * flag[47] == 29161)
s.add(flag[45] + 518 * flag[46] + flag[47] == 39501)

s.add(flag[0] + flag[1] + 1292 * flag[2] == 87961)
s.add(flag[0] + 1292 * flag[1] + flag[2] == 42776)
s.add(flag[3] + flag[4] + 1292 * flag[5] == 100914)
s.add(flag[3] + 1292 * flag[4] + flag[5] == 49274)
s.add(flag[6] + flag[7] + 1292 * flag[8] == 67347)
s.add(flag[6] + 1292 * flag[7] + flag[8] == 152553)
s.add(flag[9] + flag[10] + 1292 * flag[11] == 122890)
s.add(flag[9] + 1292 * flag[10] + flag[11] == 46721)
s.add(flag[12] + flag[13] + 1292 * flag[14] == 147438)
s.add(flag[12] + 1292 * flag[13] + flag[14] == 62232)
s.add(flag[15] + flag[16] + 1292 * flag[17] == 144852)
s.add(flag[15] + 1292 * flag[16] + flag[17] == 68683)
s.add(flag[18] + flag[19] + 1292 * flag[20] == 135810)
s.add(flag[18] + 1292 * flag[19] + flag[20] == 128064)
s.add(flag[21] + flag[22] + 1292 * flag[23] == 135833)
s.add(flag[21] + 1292 * flag[22] + flag[23] == 98394)
s.add(flag[24] + flag[25] + 1292 * flag[26] == 129373)
s.add(flag[24] + 1292 * flag[25] + flag[26] == 66114)
s.add(flag[27] + flag[28] + 1292 * flag[29] == 144847)
s.add(flag[27] + 1292 * flag[28] + flag[29] == 62223)
s.add(flag[30] + flag[31] + 1292 * flag[32] == 88034)
s.add(flag[30] + 1292 * flag[31] + flag[32] == 143547)
s.add(flag[33] + flag[34] + 1292 * flag[35] == 42770)
s.add(flag[33] + 1292 * flag[34] + flag[35] == 107320)
s.add(flag[36] + flag[37] + 1292 * flag[38] == 64773)
s.add(flag[36] + 1292 * flag[37] + flag[38] == 63482)
s.add(flag[39] + flag[40] + 1292 * flag[41] == 115125)
s.add(flag[39] + 1292 * flag[40] + flag[41] == 68649)
s.add(flag[42] + flag[43] + 1292 * flag[44] == 89248)
s.add(flag[42] + 1292 * flag[43] + flag[44] == 64719)
s.add(flag[45] + flag[46] + 1292 * flag[47] == 72505)
s.add(flag[45] + 1292 * flag[46] + flag[47] == 98325)

for i in range(48):
    s.add(flag[i] > 30)
    s.add(flag[i] >> 7 == 0)

while s.check() == z3.sat:
    m = s.model()
    possible = ""
    for i in range(48):
        possible += chr(m[flag[i]].as_long())
    if len(possible) == 48:
        print(possible)
    s.add(z3.Or([flag[i] != m[flag[i]] for i in range(48)])) 


