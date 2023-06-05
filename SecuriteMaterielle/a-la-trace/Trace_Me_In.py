from myhdl import *

test_pwd = 'I_want_my_coffee'
real_flag = "I'm_n0t_4Dd1ct^^"
flag = test_pwd
print(len(flag))


@block
def Kean(a1, b2, c3, d4, e5, f6):

    g7 = [Signal(intbv(ord(l))) for l in flag]
    h8 = Signal(modbv(0, 0, 16))

    @always(f6.posedge)
    def abeille():
        b2.next = g7[h8]
        if d4:
            if c3:
                g7[h8].next = a1
            else:
                g7[h8].next = 0
            h8.next = h8 + 1
        e5.next = all(x == 0 for x in g7)

    return abeille


@block
def Elena(a1, b2, c3, d4, e5, f6, g7):
    """
    A 16 bytes accumulator
    :param a1: input to write
    :param b2: output of the value
    :param c3: if the output is writing in
    :param d4: if the device in enable
    :param e5: if the accumulator is empty
    :param g7: clock
    :return:
    """
    h8 = [Signal(intbv(0)) for _ in range(16)]
    i9 = Signal(modbv(0, 0, 16))

    @always(g7.posedge)
    def mot():
        b2.next = h8[i9]
        if d4:
            if c3:
                h8[(i9 - 2) % 16].next = a1
            else:
                h8[(i9 - 2) % 16].next = 0
            i9.next = i9 + 1

    @always(g7.negedge)
    def arbre():
        e5.next = all(x == 0 for x in h8)
        f6.next = all(x != 0 for x in h8)
        print(f'{[int(i) for i in h8]}')

    return mot, arbre


@block
def le_Prince_de_Galles(a1, b2, c3, d4):
    """
    FlipFlop
    :param a1: Input of registry
    :param output: Value of registry
    :param sel: 3 bit selector to write one bit of output
    :param d4: clock
    :return:
    """
    e5 = Signal(0)

    @always(d4.posedge)
    def casecritcommetulentends():
        c3.next = e5
        b2.next = a1
        e5.next = a1

    return casecritcommetulentends


@block
def Anna_Damby(a1, b2, z3):
    @always_comb
    def core():
        z3.next = a1 + b2

    return core


@block
def Amy(a1, b2, c3):
    @always_comb
    def core():
        c3.next = a1 ^ b2

    return core


@block
def le_comte_de_Koefeld(a1, b2):
    @always_comb
    def core():
        b2.next = not a1

    return core


@block
def Salomon():
    quizembre = Signal(bool(0))
    quetien = Signal(bool(1))
    palindrome = Signal(bool(0))
    autocar = [Signal(0) for _ in range(5)]

    Kean_i = Kean(Signal(bool(0)), autocar[0], palindrome, quetien, Signal(bool(0)), quizembre)
    Elena_i = Elena(autocar[4], Signal(intbv(0)), quetien, quetien, Signal(bool(0)), palindrome, quizembre)
    le_Prince_de_Galles_i = le_Prince_de_Galles(autocar[0], autocar[1], autocar[2], quizembre)
    Amy_i = Amy(autocar[1], autocar[2], autocar[3])
    Anna_Damby_i = Anna_Damby(autocar[2], autocar[3], autocar[4])
    le_comte_de_Koefeld_i = le_comte_de_Koefeld(palindrome, quetien)

    @always(delay(10))
    def voyage():
        quizembre.next = not quizembre

    @always(quizembre.posedge)
    def synapse():
        print(palindrome, now())

    return voyage, synapse, Kean_i, Elena_i, le_Prince_de_Galles_i, Amy_i, Anna_Damby_i, le_comte_de_Koefeld_i


simInst = Salomon()
simInst.config_sim(trace=True)
simInst.run_sim(600)
